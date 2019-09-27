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
__date__ = '2019-09-16'
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

pluginPath = os.path.split(os.path.split(os.path.dirname(__file__))[0])[0]

class ID11Theft(QgsProcessingAlgorithm):
    """
    Mide la concentración de habitantes y evidencia indirectamente la demanda
    de movilidad, productos y servicios. Número de habitantes por la
    superficie de suelo de naturaleza urbana (no incluye vías
    y equipamientos).
    Formula: Número de habitantes / Superficie efectiva neta en hectareas
    """

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.
    BLOCKS = 'BLOCKS'
    FIELD_POPULATION = 'FIELD_POPULATION'
    NUMBER_HABITANTS = 'NUMBER_HABITANTS'
    THEF = 'THEF'
    CELL_SIZE = 'CELL_SIZE'
    OUTPUT = 'OUTPUT'


    def initAlgorithm(self, config):

        currentPath = getCurrentPath(self)
        FULL_PATH = buildFullPathName(currentPath, nameWithOuputExtension(NAMES_INDEX['ID11'][1]))

        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.BLOCKS,
                self.tr('Manzanas'),
                [QgsProcessing.TypeVectorPolygon]
            )
        )

        self.addParameter(
            QgsProcessingParameterField(
                self.FIELD_POPULATION,
                self.tr('Población'),
                'poblacion', 'BLOCKS'
            )
        )        

        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.THEF,
                self.tr('Robos'),
                [QgsProcessing.TypeVectorPoint]
            )
        )

        self.addParameter(
            QgsProcessingParameterNumber(
                self.CELL_SIZE,
                self.tr('Tamaño de la malla'),
                QgsProcessingParameterNumber.Integer,
                P_CELL_SIZE, False, 1, 99999999
            )
        )        


        self.addParameter(
            QgsProcessingParameterNumber(
                self.NUMBER_HABITANTS,
                self.tr('Por cada número de habitantes'),
                QgsProcessingParameterNumber.Integer,
                100000, False, 1, 99999999
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
        totalStpes = 12
        fieldPopulation = params['FIELD_POPULATION']
        fieldHab = params['NUMBER_HABITANTS']

        feedback = QgsProcessingMultiStepFeedback(totalStpes, feedback)

        blocks = calculateArea(params['BLOCKS'], 'area_bloc', context,
                               feedback)

        steps = steps+1
        feedback.setCurrentStep(steps)
        grid = createGrid(params['BLOCKS'], params['CELL_SIZE'], context,
                          feedback)    

        # Eliminar celdas efecto borde
        gridNeto = grid

        steps = steps+1
        feedback.setCurrentStep(steps)
        gridNeto = calculateArea(gridNeto['OUTPUT'], 'area_grid', context,
                                 feedback)

        steps = steps+1
        feedback.setCurrentStep(steps)
        gridNeto = calculateField(gridNeto['OUTPUT'], 'id_grid', '$id', context,
                                  feedback, type=1)

        steps = steps+1
        feedback.setCurrentStep(steps)
        segments = intersection(blocks['OUTPUT'], gridNeto['OUTPUT'],
                                'area_bloc;' + fieldPopulation,
                                'id_grid;area_grid',
                                context, feedback)


        # Haciendo el buffer inverso aseguramos que los segmentos
        # quden dentro de la malla
        steps = steps+1
        feedback.setCurrentStep(steps)
        segments = makeSureInside(segments['OUTPUT'],
                                                    context,
                                                    feedback)

        steps = steps+1
        feedback.setCurrentStep(steps)
        gridNetoAndSegments = joinByLocation(gridNeto['OUTPUT'],
                                             segments['OUTPUT'],
                                              fieldPopulation,                                   
                                              [CONTIENE], [SUM],
                                              DISCARD_NONMATCHING,
                                              context,
                                              feedback)   


        # Calcular cuantos robos hay en cada grid

        steps = steps+1
        feedback.setCurrentStep(steps)
        thef = calculateField(params['THEF'], 'idx', '$id', context,
                                         feedback, type=1)


        steps = steps+1
        feedback.setCurrentStep(steps)        
        gridNetoAndSegments = joinByLocation(gridNetoAndSegments['OUTPUT'],
                                              thef['OUTPUT'],
                                              ['idx'],                                   
                                              [CONTIENE], [COUNT],
                                              UNDISCARD_NONMATCHING,
                                              context,
                                              feedback)           

        # steps = steps+1
        # feedback.setCurrentStep(steps)
        # formulaThefPerHab = 'idx_count/' + str(fieldHab)
        # thefPerHab = calculateField(gridNetoAndSegments['OUTPUT'],
        #                            NAMES_INDEX['ID11'][0],
        #                            formulaThefPerHab,
        #                            context,
        #                            feedback, params['OUTPUT'])


        steps = steps+1
        feedback.setCurrentStep(steps)
        formulaThefPerHab = 'coalesce(idx_count/' + fieldPopulation + '_sum, 0)'
        thefPerHab = calculateField(gridNetoAndSegments['OUTPUT'],
                                   NAMES_INDEX['ID11'][0],
                                   formulaThefPerHab,
                                   context,
                                   feedback, params['OUTPUT'])        


        return thefPerHab

        # Return the results of the algorithm. In this case our only result is
        # the feature sink which contains the processed features, but some
        # algorithms may return multiple feature sinks, calculated numeric
        # statistics, etc. These should all be included in the returned
        # dictionary, with keys matching the feature corresponding parameter
        # or output names.
        #return {self.OUTPUT: dest_id}

    def icon(self):
        return QIcon(os.path.join(pluginPath, 'sisurbano', 'icons', 'thief.png'))

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'D11 Robos por número de habitantes'

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
        return 'D Dinámicas Socio-espaciales'

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return ID11Theft()

