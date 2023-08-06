# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
# Copyright © 2017-2018 Carl Chenet <carl.chenet@ohmytux.com>
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
# along with this program.  If not, see <http://www.gnu.org/licenses/>

'''Store the pair db entry id / twitter status id'''

# standard libraries imports
import logging

# 3rd party libraries imports
import redis

def store_status_id(redisconf, dbid, statusid):
    '''Store the pair db entry id / twitter status id'''
    try:
        r = redis.StrictRedis(host=redisconf['host'], port=redisconf['port'],db=redisconf['db'], charset="utf-8", decode_responses=True)
        r.sadd(dbid, statusid)
    except redis.exceptions.ConnectionError as err:
        logging.error(err)
