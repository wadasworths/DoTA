#-*- encoding:utf-8 -*-

import dota2api
import json
import pymysql

db = pymysql.connect('localhost','root','******','test')

cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS HEROES_INFO")

sql="""CREATE TABLE HEROES_INFO (
       hero_id int(5) primary key not null COMMENT 'id',
       hero_name varchar(50) default null COMMENT 'name',
	   localized_name varchar(100) default null COMMENT 'npc_name',
	   url_full_portrait varchar(100) default null COMMENT 'full_pic_url',
	   url_vertical_portrait varchar(100) default null COMMENT 'vert_pic_url',
	   url_large_portrait varchar(100) default null COMMENT 'large_pic_url',
	   url_small_portrait varchar(100) default null COMMENT 'small_pic_url')"""

cursor.execute(sql)
db.close()

api = dota2api.Initialise('8E3AABDF2D35489943328933DAE44DBE')

heroesList = api.get_heroes().get('heroes')

for hero in heroesList:
    name = hero.get('name')
    url_full_portrait = hero.get('url_full_portrait')
    url_vertical_portrait=hero.get('url_vertical_portrait')
    url_large_portrait=hero.get('url_large_portrait')
    url_small_portrait=hero.get('url_small_portrait')
    id = hero.get('id')
    localized_name = hero.get('localized_name')
    

