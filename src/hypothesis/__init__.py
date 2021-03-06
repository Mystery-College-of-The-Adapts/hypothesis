# coding=utf-8

# Copyright (C) 2013-2015 David R. MacIver (david@drmaciver.com)

# This file is part of Hypothesis (https://github.com/DRMacIver/hypothesis)

# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at http://mozilla.org/MPL/2.0/.

# END HEADER

"""Hypothesis is a library for writing unit tests which are parametrized by
some source of data.

It verifies your code against a wide range of input and minimizes any
failing examples it finds.

"""

from __future__ import division, print_function, absolute_import, \
    unicode_literals

from hypothesis.searchstrategy import strategy
from hypothesis.settings import Settings, Verbosity
from hypothesis.version import __version_info__, __version__
from hypothesis.core import given, assume, find, example

# Force strategy extensions to be loaded here
import hypothesis.strategies as unused
[unused]

__all__ = [
    'Settings',
    'Verbosity',
    'assume',
    'given',
    'strategy',
    'find',
    'example',
    '__version__',
    '__version_info__',
]
