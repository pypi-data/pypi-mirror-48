# -*- coding: utf-8 -*-

# Copyright 2015-2019 Mike Fährmann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""Downloader modules"""

import importlib

modules = [
    "http",
    "text",
    "ytdl",
]


def find(scheme):
    """Return downloader class suitable for handling the given scheme"""
    try:
        return _cache[scheme]
    except KeyError:
        klass = None
        try:
            if scheme in modules:  # prevent unwanted imports
                module = importlib.import_module("." + scheme, __package__)
                klass = module.__downloader__
        except (ImportError, AttributeError, TypeError):
            pass
        _cache[scheme] = klass
        return klass


# --------------------------------------------------------------------
# internals

_cache = {}
