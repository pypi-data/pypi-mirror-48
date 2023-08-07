# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2019 Bitergia
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# Authors:
#   Valerio Cosentino <valcos@bitergia.com>
#

from .mbox import Mapping, MBoxOcean


class GroupsioOcean(MBoxOcean):
    """Groups.io Ocean feeder"""

    mapping = Mapping

    @classmethod
    def get_arthur_params_from_url(cls, url):
        # In the url the uri and the data dir are included
        params = url.split()

        return {"group_name": params[0], "dirpath": "/tmp"}
