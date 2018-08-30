#-*- encoding:utf-8 -*-

import dota2api
import json
from time import sleep
from pymongo import MongoClient

api = dota2api.Initialise('8E3AABDF2D35489943328933DAE44DBE')

heroesList = api.get_heroes().get('heroes')
_hero_list = []
for item in heroesList:
	_hero_list.append(item['localized_name'])

# print(_hero_list)

hist = api.get_match_history(account_id=101695162).get('matches')

myclient = MongoClient("mongodb://localhost:27017/")
db = myclient.dota2
db.authenticate("dota", "dota#12")

#hist = api.get_match_history(account_id=172905095).get('matches')
match_id_list = []
for i in hist:
	match_id_list.append(i['match_id'])
	#print(match_id_list)
	
	# 获取联赛信息
	match = api.get_match_details(match_id=i['match_id'])
	
	match_id = db.match_player_fy.insert_one(match).inserted_id
	#play_list = match.get('players')
	print(match_id)


# print(match_id_list)
