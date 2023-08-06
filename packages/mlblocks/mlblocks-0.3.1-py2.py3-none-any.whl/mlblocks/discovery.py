# -*- coding: utf-8 -*-

"""
Primitives and Pipelines discovery module.

This module contains functions to load primitive and pipeline
annotations, as well as to configure how MLBlocks finds the
primitives and pipelines.
"""

import json
import logging
import os
import sys

import pkg_resources

LOGGER = logging.getLogger(__name__)

_PRIMITIVES_PATHS = [
    os.path.join(os.getcwd(), 'mlprimitives'),
    os.path.join(sys.prefix, 'mlprimitives'),
    os.path.join(os.getcwd(), 'mlblocks_primitives'),    # legacy
    os.path.join(sys.prefix, 'mlblocks_primitives'),    # legacy
]
_PIPELINES_PATHS = [
    os.path.join(os.getcwd(), 'mlpipelines'),
]


def _add_lookup_path(path, paths):
    """Add a new path to lookup.

    The new path will be inserted in the first place of the list,
    so any element found in this new folder will take precedence
    over any other element with the same name that existed in the
    system before.

    Args:
        path (str):
            path to add
        paths (list):
            list where the new path will be added.

    Raises:
        ValueError:
            A ``ValueError`` will be raised if the path is not valid.

    Returns:
        bool:
            Whether the new path was added or not.
    """
    if path not in paths:
        if not os.path.isdir(path):
            raise ValueError('Invalid path: {}'.format(path))

        paths.insert(0, os.path.abspath(path))
        return True

    return False


def add_primitives_path(path):
    """Add a new path to look for primitives.

    The new path will be inserted in the first place of the list,
    so any primitive found in this new folder will take precedence
    over any other primitive with the same name that existed in the
    system before.

    Args:
        path (str):
            path to add

    Raises:
        ValueError:
            A ``ValueError`` will be raised if the path is not valid.
    """
    added = _add_lookup_path(path, _PRIMITIVES_PATHS)
    if added:
        LOGGER.debug('New primitives path added: %s', path)


def add_pipelines_path(path):
    """Add a new path to look for pipelines.

    The new path will be inserted in the first place of the list,
    so any primitive found in this new folder will take precedence
    over any other pipeline with the same name that existed in the
    system before.

    Args:
        path (str):
            path to add

    Raises:
        ValueError:
            A ``ValueError`` will be raised if the path is not valid.
    """
    added = _add_lookup_path(path, _PIPELINES_PATHS)
    if added:
        LOGGER.debug('New pipelines path added: %s', path)


def _load_entry_points(entry_point_name, entry_point_group='mlblocks'):
    """Get a list of folders from entry points.

    This list will include the value of any entry point named after the given
    ``entry_point_name`` published under the given ``entry_point_group``.

    An example of such an entry point would be::

        entry_points = {
            'mlblocks': [
                'primitives=some_module:SOME_VARIABLE'
            ]
        }

    where the module ``some_module`` contains a variable such as::

        SOME_VARIABLE = os.path.join(os.path.dirname(__file__), 'jsons')

    Args:
        entry_point:
            The name of the ``entry_point`` to look for.

    Returns:
        list:
            The list of folders.
    """
    lookup_paths = list()
    entry_points = pkg_resources.iter_entry_points(entry_point_group)
    for entry_point in entry_points:
        if entry_point.name == entry_point_name:
            paths = entry_point.load()
            if isinstance(paths, str):
                lookup_paths.append(paths)
            elif isinstance(paths, (list, tuple)):
                lookup_paths.extend(paths)

    return lookup_paths


def get_primitives_paths():
    """Get the list of folders where primitives will be looked for.

    This list will include the values of all the entry points named ``primitives``
    published under the entry point group ``mlblocks``.

    Also, for backwards compatibility reasons, the paths from the entry points
    named ``jsons_path`` published under the ``mlprimitives`` group will also
    be included.

    An example of such an entry point would be::

        entry_points = {
            'mlblocks': [
                'primitives=some_module:SOME_VARIABLE'
            ]
        }

    where the module ``some_module`` contains a variable such as::

        SOME_VARIABLE = os.path.join(os.path.dirname(__file__), 'jsons')

    Returns:
        list:
            The list of folders.
    """
    paths = _load_entry_points('primitives') + _load_entry_points('jsons_path', 'mlprimitives')
    return _PRIMITIVES_PATHS + paths


def get_pipelines_paths():
    """Get the list of folders where pipelines will be looked for.

    This list will include the values of all the entry points named ``pipelines``
    published under the entry point group ``mlblocks``.

    An example of such an entry point would be::

        entry_points = {
            'mlblocks': [
                'pipelines=some_module:SOME_VARIABLE'
            ]
        }

    where the module ``some_module`` contains a variable such as::

        SOME_VARIABLE = os.path.join(os.path.dirname(__file__), 'jsons')

    Returns:
        list:
            The list of folders.
    """
    return _PIPELINES_PATHS + _load_entry_points('pipelines')


def _load(name, paths):
    """Locate and load the JSON annotation in any of the given paths.

    All the given paths will be scanned to find a JSON file with the given name,
    and as soon as a JSON with the given name is found it is returned.

    Args:
        name (str):
            name of the JSON to look for. The name should not contain the
            ``.json`` extension, as it will be added dynamically.
        paths (list):
            list of paths where the primitives will be looked for.

    Returns:
        dict:
            The content of the JSON annotation file loaded into a dict.
    """
    for base_path in paths:
        parts = name.split('.')
        number_of_parts = len(parts)

        for folder_parts in range(number_of_parts):
            folder = os.path.join(base_path, *parts[:folder_parts])
            filename = '.'.join(parts[folder_parts:]) + '.json'
            json_path = os.path.join(folder, filename)

            if os.path.isfile(json_path):
                with open(json_path, 'r') as json_file:
                    LOGGER.debug('Loading %s from %s', name, json_path)
                    return json.load(json_file)


def load_primitive(name):
    """Locate and load the primitive JSON annotation.

    All the primitive paths will be scanned to find a JSON file with the given name,
    and as soon as a JSON with the given name is found it is returned.

    Args:
        name (str):
            name of the JSON to look for. The name should not contain the
            ``.json`` extension, as it will be added dynamically.

    Returns:
        dict:
            The content of the JSON annotation file loaded into a dict.

    Raises:
        ValueError:
            A ``ValueError`` will be raised if the primitive cannot be found.
    """
    primitive = _load(name, get_primitives_paths())
    if not primitive:
        raise ValueError("Unknown primitive: {}".format(name))

    return primitive


def load_pipeline(name):
    """Locate and load the pipeline JSON annotation.

    All the pipeline paths will be scanned to find a JSON file with the given name,
    and as soon as a JSON with the given name is found it is returned.

    Args:
        name (str):
            name of the JSON to look for. The name should not contain the
            ``.json`` extension, as it will be added dynamically.

    Returns:
        dict:
            The content of the JSON annotation file loaded into a dict.

    Raises:
        ValueError:
            A ``ValueError`` will be raised if the pipeline cannot be found.
    """
    pipeline = _load(name, get_pipelines_paths())
    if not pipeline:
        raise ValueError("Unknown pipeline: {}".format(name))

    return pipeline
