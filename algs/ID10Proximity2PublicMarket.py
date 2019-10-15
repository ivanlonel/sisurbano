# -*- coding: utf-8 -*-

"""
/***************************************************************************
 Sisurbano
                                 A QGIS plugin
 Cáculo de indicadores urbanos
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2019-10-01
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
__date__ = '2019-10-01'
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

class ID10Proximity2PublicMarket(QgsProcessingAlgorithm):
    """
    Mide la distancia desde la vivienda a puntos de venta de
    comida asequible. Se entiende como cercano y asequible,
    aquellas viviendas ubicadas a 300 metros o menos de mercados públicos.
    El objetivo de un sistema alimentario es promover y consolidar puntos
    de venta de alimentos saludables, para diversas zonas de la ciudad,
    de manera que se llegue a todos los ciudadanos.    
    Formula: (Viviendas con proximidad a mercados públicos /
              Viviendas totales)*100
    """
    EQUIPMENT = 'EQUIPMENT'
    BLOCKS = 'BLOCKS'
    FIELD_POPULATION = 'FIELD_POPULATION'
    FIELD_HOUSING = 'FIELD_HOUSING'
    CELL_SIZE = 'CELL_SIZE'    
    OUTPUT = 'OUTPUT'
    STUDY_AREA_GRID = 'STUDY_AREA_GRID'



    def initAlgorithm(self, config):

        currentPath = getCurrentPath(self)
        FULL_PATH = buildFullPathName(currentPath, nameWithOuputExtension(NAMES_INDEX['ID10'][1]))           
          
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
            QgsProcessingParameterField(
                self.FIELD_HOUSING,
                self.tr('Viviendas'),
                'viviendas', 'BLOCKS'
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
            QgsProcessingParameterFeatureSource(
                self.EQUIPMENT,
                self.tr('Mercados públicos'),
                [QgsProcessing.TypeVectorAnyGeometry]
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
      totalStpes = 14
      fieldPopulation = params['FIELD_POPULATION']
      fieldHousing = params['FIELD_HOUSING']
      DISTANCE_WALKABILITY = 300

      feedback = QgsProcessingMultiStepFeedback(totalStpes, feedback)

      """
      -----------------------------------------------------------------
      Calcular las facilidades a espacios pubicos abiertos
      -----------------------------------------------------------------
      """

      steps = steps+1
      feedback.setCurrentStep(steps)
      blocksWithId = calculateField(params['BLOCKS'], 'id_block', '$id', context,
                                    feedback, type=1)

      steps = steps+1
      feedback.setCurrentStep(steps)
      equipmentWithId = calculateField(params['EQUIPMENT'], 'idx', '$id', context,
                                      feedback, type=1)


      steps = steps+1
      feedback.setCurrentStep(steps)
      centroidsBlocks = createCentroids(blocksWithId['OUTPUT'], context,
                                        feedback)

      steps = steps+1
      feedback.setCurrentStep(steps)
      blockBuffer4GreenSapace = createBuffer(centroidsBlocks['OUTPUT'], DISTANCE_WALKABILITY,
                                            context,
                                            feedback)

      steps = steps+1
      feedback.setCurrentStep(steps)
      counterGreenSpace = joinByLocation(blockBuffer4GreenSapace['OUTPUT'],
                                        equipmentWithId['OUTPUT'],
                                        'idx',[CONTIENE], [COUNT],
                                        False,
                                        context,
                                        feedback)

      steps = steps+1
      feedback.setCurrentStep(steps)
      blocksJoined = joinByAttr(blocksWithId['OUTPUT'], 'id_block',
                                counterGreenSpace['OUTPUT'], 'id_block',
                                'idx_count',
                                False,
                                'gsp_',
                                context,
                                feedback)

      """
      -----------------------------------------------------------------
      Calcular numero de viviendas por hexagano
      -----------------------------------------------------------------
      """
      steps = steps+1
      feedback.setCurrentStep(steps)
      if not OPTIONAL_GRID_INPUT: params['CELL_SIZE'] = P_CELL_SIZE
      grid, isStudyArea = buildStudyArea(params['CELL_SIZE'], params['BLOCKS'],
                                         params['STUDY_AREA_GRID'],
                                         context, feedback)
      gridNeto = grid  
      
      steps = steps+1
      feedback.setCurrentStep(steps)
      segments = intersection(blocksJoined['OUTPUT'], gridNeto['OUTPUT'],
                              'gsp_idx_count;' + fieldHousing,
                              'id_grid',
                              context, feedback)

      # Haciendo el buffer inverso aseguramos que los segmentos
      # quden dentro de la malla
      steps = steps+1
      feedback.setCurrentStep(steps)
      facilitiesForSegmentsFixed = makeSureInside(segments['OUTPUT'],
                                                  context,
                                                  feedback)
      # Con esto se saca el total de viviendas
      steps = steps+1
      feedback.setCurrentStep(steps)
      gridNetoAndSegments = joinByLocation(gridNeto['OUTPUT'],
                                           facilitiesForSegmentsFixed['OUTPUT'],
                                           'gsp_idx_count;' + fieldHousing,
                                           [CONTIENE], [SUM], UNDISCARD_NONMATCHING,                 
                                           context,
                                           feedback)

      #descartar NULL para obtener el total de viviendas que cumple
      steps = steps+1
      feedback.setCurrentStep(steps)
      facilitiesNotNullForSegmentsFixed = filter(facilitiesForSegmentsFixed['OUTPUT'],
                                                 'gsp_idx_count', NOT_NULL,
                                                 '', context, feedback)

      steps = steps+1
      feedback.setCurrentStep(steps)
      gridNetoAndSegmentsNotNull = joinByLocation(gridNetoAndSegments['OUTPUT'],
                                                  facilitiesNotNullForSegmentsFixed['OUTPUT'],
                                                  fieldHousing,
                                                  [CONTIENE], [SUM], UNDISCARD_NONMATCHING,               
                                                  context,
                                                  feedback)

      steps = steps+1
      feedback.setCurrentStep(steps)
      formulaProximity = '(coalesce('+fieldHousing+'_sum_2,0) /  coalesce('+fieldHousing+'_sum,0))*100'
      proximity2OpenSpace = calculateField(gridNetoAndSegmentsNotNull['OUTPUT'], NAMES_INDEX['ID10'][0],
                                        formulaProximity,
                                        context,
                                        feedback,  params['OUTPUT'])

      return proximity2OpenSpace




        # Return the results of the algorithm. In this case our only result is
        # the feature sink which contains the processed features, but some
        # algorithms may return multiple feature sinks, calculated numeric
        # statistics, etc. These should all be included in the returned
        # dictionary, with keys matching the feature corresponding parameter
        # or output names.
        #return {self.OUTPUT: dest_id}

    def icon(self):
        return QIcon(os.path.join(pluginPath, 'sisurbano', 'icons', 'fruit.png'))

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'D10 Cercanía y asequibilidad a alimentos'

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
        return ID10Proximity2PublicMarket()

