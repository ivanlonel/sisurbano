# -*- coding: utf-8 -*-

"""
***************************************************************************
    densityPopulation.py
    ---------------------
    Date                 : July 2019
    Copyright            : (C) 2019 by Llactalab
    Email                : fastuller88 at gmail dot com
***************************************************************************
"""

__author__ = 'Johnatan Astudillo'
__date__ = 'July 2019'
__copyright__ = '(C) 2019, Llactalab'

from qgis.core import QgsProcessing
import processing

def calculateArea(input, field, context, feedback,
                  output=QgsProcessing.TEMPORARY_OUTPUT):
    if feedback.isCanceled():
        return {}
    alg_params = {
        'FIELD_LENGTH': 16,
        'FIELD_NAME': field,
        'FIELD_PRECISION': 3,
        'FIELD_TYPE': 0,
        'FORMULA': ' $area ',
        'INPUT': input,
        'NEW_FIELD': True,
        'OUTPUT': output
    }
    result = processing.run('qgis:fieldcalculator', alg_params,
                            context=context, feedback=feedback,
                            is_child_algorithm=True)
    return result


def createGrid(params, context, feedback,
               output=QgsProcessing.TEMPORARY_OUTPUT):
    if feedback.isCanceled():
        return {}
    alg_params = {
        'CRS': 'ProjectCrs',
        'EXTENT': params['BLOCKS'],
        'HOVERLAY': 0,
        'HSPACING': params['CELL_SIZE'],
        'TYPE': 4,
        'VOVERLAY': 0,
        'VSPACING': params['CELL_SIZE'],
        'OUTPUT': output
    }
    result = processing.run('qgis:creategrid', alg_params, context=context,
                            feedback=feedback, is_child_algorithm=True)
    return result


def calculateField(input, field, formula, context, feedback,
                   output=QgsProcessing.TEMPORARY_OUTPUT, type=0):
    if feedback.isCanceled():
        return {}
    alg_params = {
        'FIELD_LENGTH': 10,
        'FIELD_NAME': field,
        'FIELD_PRECISION': 3,
        'FIELD_TYPE': type,
        'FORMULA': formula,
        'INPUT': input,
        'NEW_FIELD': True,
        'OUTPUT': output
    }
    result = processing.run('qgis:fieldcalculator', alg_params,
                            context=context,
                            feedback=feedback,
                            is_child_algorithm=True)
    return result


def intersection(input, inputOverlay,
                 inputFields, inputOverlayFields,
                 context, feedback,
                 output=QgsProcessing.TEMPORARY_OUTPUT):
    if feedback.isCanceled():
        return {}
    # validar que exista el campo pobacion
    alg_params = {
        'INPUT': input,
        'INPUT_FIELDS': inputFields,
        'OVERLAY': inputOverlay,
        'OVERLAY_FIELDS': inputOverlayFields,
        'OUTPUT': output
    }
    result = processing.run('native:intersection', alg_params,
                            context=context,
                            feedback=feedback,
                            is_child_algorithm=True)
    return result


def makeSureInside(input, context, feedback,
                   output=QgsProcessing.TEMPORARY_OUTPUT):
    # if feedback.isCanceled():
    #     return {}

    # alg_params = {
    #     'FIELD': ['id_grid'],
    #     'INPUT': input,
    #     'OUTPUT': output
    # }
    # result = processing.run('native:dissolve', alg_params,
    #                         context=context,
    #                         feedback=feedback,
    #                         is_child_algorithm=True)
    alg_params = {
        'DISSOLVE': False,
        'DISTANCE': -1,
        'END_CAP_STYLE': 0,
        'INPUT': input,
        'MITER_LIMIT': 2,
        'SEGMENTS': 5,
        'JOIN_STYLE': 0,
        'OUTPUT': output
    }
    result = processing.run('native:buffer', alg_params,
                            context=context,
                            feedback=feedback, is_child_algorithm=True)
    return result


def joinByLocation(input, inputJoin, fields, context, feedback,
                   output=QgsProcessing.TEMPORARY_OUTPUT):
    if feedback.isCanceled():
        return {}

    alg_params = {
        'DISCARD_NONMATCHING': True,
        'INPUT': input,
        'JOIN': inputJoin,
        'JOIN_FIELDS': fields,
        'PREDICATE': [1],  # 4:solapa, 0: Intesecta, 1: Contiene
        'SUMMARIES': 5,  # suma
        'OUTPUT': output
    }
    result = processing.run('qgis:joinbylocationsummary', alg_params,
                            context=context,
                            feedback=feedback, is_child_algorithm=True)
    return result