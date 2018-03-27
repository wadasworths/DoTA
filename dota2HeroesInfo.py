#-*- encoding:utf-8 -*-

import dota2api
import json
import pymysql

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
    db = pymysql.connect('localhost','root','******','test')
    cursor = db.cursor()
    sql="INSERT INTO HEROES_INFO values ('%d', '%s', '%s', '%s', '%s', '%s', '%s' )" % (id,name,localized_name,url_full_portrait,url_vertical_portrait,url_large_portrait,url_small_portrait)
    try:
	    cursor.execute(sql)
	    db.commit()
    except:
	    db.rollback()
	
    db.close()
