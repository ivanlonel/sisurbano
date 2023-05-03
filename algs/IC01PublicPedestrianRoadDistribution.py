# -*- coding: utf-8 -*-

"""
/***************************************************************************
 Sisurbano
                                 A QGIS plugin
 Cáculo de indicadores urbanos
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2019-09-16
        copyright            : (C) 2019 by LlactaLAB
        email                : johnatan.astudillo@ucuenca.edu.ec
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Johnatan Astudillo'
__date__ = '2019-09-23'
__copyright__ = '(C) 2019 by LlactaLAB'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os

from qgis.PyQt.QtCore import QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.core import (QgsProcessing,
                       QgsProcessingMultiStepFeedback,
                       QgsFeatureSink,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterField,
                       QgsProcessingParameterNumber,
                       QgsProcessingParameterFeatureSink)
from .ZProcesses import *
from .Zettings import *
from .ZHelpers import *

#pluginPath = os.path.split(os.path.split(os.path.dirname(__file__))[0])[0]

class IC01PublicPedestrianRoadDistribution(QgsProcessingAlgorithm):
    """
    Mide el porcentaje del espacio viario destinado al peatón, considerando que
    los espacios con acceso restringido al automovil son favorables para
    actividades de vida en comunidad, que repercuten directa y positivamente
    en la calidad urbana y la calidad de vida. Relación del espacio público
    peatonal con respecto al viario público general.
    Se entiende como viario público: calles, veredas, caminos peatonales, ciclovías.
    Formula: (Área del viario público peatonal / Área del viario público)*100
    """
    WALK_ROAD = 'WALK_ROAD'
    ROADS = 'ROADS'
    # FIELD_POPULATION = 'FIELD_POPULATION'
    # FIELD_HOUSING = 'FIELD_HOUSING'
    CELL_SIZE = 'CELL_SIZE'    
    OUTPUT = 'OUTPUT'
    STUDY_AREA_GRID = 'STUDY_AREA_GRID'    

    def initAlgorithm(self, config):
        currentPath = getCurrentPath(self)
        FULL_PATH = buildFullPathName(currentPath, nameWithOuputExtension(NAMES_INDEX['IC01'][1]))            

        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.ROADS,
                self.tr('Viario público'),
                [QgsProcessing.TypeVectorPolygon]
            )
        )

        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.WALK_ROAD,
                self.tr('Viario público peatonal'),
                [QgsProcessing.TypeVectorPolygon]
            )
        )


        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.STUDY_AREA_GRID,
                self.tr(TEXT_GRID_INPUT),
                [QgsProcessing.TypeVectorPolygon],
                '', OPTIONAL_GRID_INPUT
            )
        )         

        if OPTIONAL_GRID_INPUT:
            self.addParameter(
                QgsProcessingParameterNumber(
                    self.CELL_SIZE,
                    self.tr('Tamaño de la malla'),
                    QgsProcessingParameterNumber.Integer,
                    P_CELL_SIZE, False, 1, 99999999
                )
            )          


        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT,
                self.tr('Salida'),
                QgsProcessing.TypeVectorAnyGeometry,
                str(FULL_PATH)                
            )
        )

    def processAlgorithm(self, params, context, feedback):
        steps = 0
        totalStpes = 13
        # fieldPopulation = params['FIELD_POPULATION']

        feedback = QgsProcessingMultiStepFeedback(totalStpes, feedback)

        feedback.setCurrentStep(steps)
        if not OPTIONAL_GRID_INPUT: params['CELL_SIZE'] = P_CELL_SIZE
        grid, isStudyArea = buildStudyArea(params['CELL_SIZE'], params['ROADS'],
                                           params['STUDY_AREA_GRID'],
                                           context, feedback)
        gridNeto = grid  

          # CALCULAR VIARIO
        steps += 1
        feedback.setCurrentStep(steps)
        segments = intersection(params['ROADS'], gridNeto['OUTPUT'],
                                [],
                                'id_grid;area_grid',
                                context, feedback)

        steps += 1
        feedback.setCurrentStep(steps)
        segmentsArea = calculateArea(segments['OUTPUT'], 'area_road', context,
                                     feedback)

        steps += 1
        feedback.setCurrentStep(steps)
        segmentsFixed = makeSureInside(segmentsArea['OUTPUT'],
                                       context,
                                       feedback)

        steps += 1
        feedback.setCurrentStep(steps)
        gridNetoAndSegments = joinByLocation(gridNeto['OUTPUT'],
                                             segmentsFixed['OUTPUT'],
                                             [],
                                             [CONTIENE], [SUM],    
                                             UNDISCARD_NONMATCHING,                               
                                             context,
                                             feedback)
          # CALCULAR AREA CAMINOS PEATONALES
        steps += 1
        feedback.setCurrentStep(steps)
        walkRoads = intersection(params['WALK_ROAD'], gridNeto['OUTPUT'],
                                [],
                                [],
                                context, feedback)    



        steps += 1
        feedback.setCurrentStep(steps)
        walkArea = calculateArea(walkRoads['OUTPUT'],
                                  'area_walk',
                                  context, feedback)


        steps += 1
        feedback.setCurrentStep(steps)
        walkAreaFixed = makeSureInside(walkArea['OUTPUT'],
                                        context,
                                        feedback)    

        steps += 1
        feedback.setCurrentStep(steps)
        walkAreaAndRoads = joinByLocation(gridNetoAndSegments['OUTPUT'],
                                          walkAreaFixed['OUTPUT'],
                                          'area_walk',
                                          [CONTIENE], [SUM],
                                          UNDISCARD_NONMATCHING,                              
                                          context,
                                          feedback)


        steps += 1
        feedback.setCurrentStep(steps)
        formulaSurfaceWalk = 'coalesce((area_walk_sum/area_road_sum)*100, "")'
        return calculateField(
            walkAreaAndRoads['OUTPUT'],
            NAMES_INDEX['IC01'][0],
            formulaSurfaceWalk,
            context,
            feedback,
            params['OUTPUT'],
        )


    def icon(self):
        return QIcon(os.path.join(pluginPath, 'walkroad.jpeg'))

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'C01 Reparto del viario público peatonal'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr(self.name())

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr(self.groupId())

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'C Movilidad urbana'

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return IC01PublicPedestrianRoadDistribution()

    def shortHelpString(self):
        return  "<b>Descripción:</b><br/>"\
                "<span>Mide el porcentaje del espacio viario destinado al peatón, considerando que los espacios con acceso restringido al automovil son favorables para actividades de vida en comunidad, que repercuten directa y positivamente en la calidad urbana y la calidad de vida. Relación del espacio público peatonal con respecto al viario público general.</span>"\
                "<br/><br/><b>Justificación y metodología:</b><br/>"\
                "<span>Se entiende como viario público: calles, veredas, caminos peatonales, ciclovías.</span>"\
                "<br/><br/><b>Formula:</b><br/>"\
                "<span>(Área del viario público peatonal / Área del viario público)*100<br/>"             

