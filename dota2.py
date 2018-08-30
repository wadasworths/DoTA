#-*- encoding:utf-8 -*-

import dota2api
import json
from time import sleep

api = dota2api.Initialise('8E3AABDF2D35489943328933DAE44DBE')

#heroesInfo = api.get_heroes()

heroesList = api.get_heroes().get('heroes')

_hero_list = []
for item in heroesList:
	_hero_list.append(item['localized_name'])

#print(_hero_list)

hist = api.get_match_history(account_id=172905095).get('matches')

match_id_list = []
for i in hist:
	match_id_list.append(i['match_id'])
	match = api.get_match_details(match_id=i['match_id'])
	
	play_list = match.get('players')
	print(type(play_list))
