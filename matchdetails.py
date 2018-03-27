import dota2api	
import json

api = dota2api.Initialise('8E3AABDF2D35489943328933DAE44DBE')

match = api.get_match_details(match_id=3687702200)

match_id=match.get('match_id')

print(match_id)

exit()
heroesList = api.get_heroes().get('heroes')

matchHeroes=[]

for i in range(0,10):
	hid=match.get('players')[i].get('hero_id')
	for hero in heroesList:
		if(hero.get('id')==hid):
			name=hero.get('name')
			break
	matchHeroes.append(name)    

print(matchHeroes)

