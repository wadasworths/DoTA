#-*- encoding:utf-8 -*-

import dota2api
import json

api = dota2api.Initialise('8E3AABDF2D35489943328933DAE44DBE')

heroesInfo = api.get_heroes()

print (heroesInfo)




