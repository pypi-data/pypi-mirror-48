# -*- coding: utf-8 -*-
# copyright 2014 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
# contact http://www.logilab.fr -- mailto:contact@logilab.fr
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 2.1 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.

"""cubicweb-sentry views/forms/actions/components for web ui"""


from cubicweb_sentry.patches import add_sentry_support
import logging


def registration_callback(vreg):
    config = vreg.config
    sentry_dsn = config['sentry-dsn']
    log_level_choice = config['sentry-log-level']
    if log_level_choice:
        log_level = getattr(logging, log_level_choice.upper())
    else:
        log_level = None

    released_cube = config.cubes()[0]
    release = '.'.join(map(str, config.cube_version(released_cube)))

    if sentry_dsn:
        add_sentry_support(sentry_dsn, log_level, release)
