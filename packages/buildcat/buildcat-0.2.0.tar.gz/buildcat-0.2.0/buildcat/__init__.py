# Copyright 2018 Timothy M. Shead
#
# This file is part of Buildcat.
#
# Buildcat is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Buildcat is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Buildcat.  If not, see <http://www.gnu.org/licenses/>.

"""Provides the Buildcat public API."""

from __future__ import absolute_import, division, print_function

import logging
import os

__version__ = "0.2.0"

formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s:%(name)s:%(message)s", datefmt="%H:%M:%S")

handler = logging.StreamHandler()
handler.setFormatter(formatter)

log = logging.getLogger(__name__)
log.setLevel(os.environ.get("BUILDCAT_LOG_LEVEL", logging.INFO))
log.addHandler(handler)

