# -*- coding: utf-8 -*-
# Copyright © 2015-2017 Carl Chenet <carl.chenet@ohmytux.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/

# Get values of the configuration file for Mastodon
'''Get values of the configuration file for Mastodon'''

# standard library imports
import sys

def parsemastodon(config):
   # mastodon section
    section = 'mastodon'
    mastodonconf = {}
    if config.has_section(section):
        possibleoptions = ['instance_url', 'user_credentials', 'client_credentials', 'visibility']
        for confkey in possibleoptions:
            if config.has_option(section, confkey):
                mastodonconf[confkey] = config.get(section, confkey)
            else:
                sys.exit('You should define a "{confkey}" parameter in the [{section}] section'.format(confkey=confkey, section=section))
    return mastodonconf
