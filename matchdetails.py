import dota2api	
import json
import pymysql

def InsertData(TableName,dic):
    try:
        db = pymysql.connect('localhost','root','3660033','dota')
        cursor = db.cursor()
        COLstr=''   #列的字段  
        ROWstr=''  #行字段  

        ColumnStyle=' VARCHAR(20)'
        for key in dic.keys():
            COLstr=COLstr+' '+key+ColumnStyle+','
            ROWstr=(ROWstr+'"%s"'+',')%(dic[key])

        try:
            cursor.execute("SELECT * FROM  %s"%(TableName))
            cursor.execute("INSERT INTO %s VALUES (%s)"%(TableName,ROWstr[:-1]))
        except:
			cur.execute("CREATE TABLE %s (%s)"%(TableName,COLstr[:-1]))
			cur.execute("INSERT INTO %s VALUES (%s)"%(TableName,ROWstr[:-1]))

		db.commit()
		db.close()
    except:
        print("异常报错！")

api = dota2api.Initialise('8E3AABDF2D35489943328933DAE44DBE')
match = api.get_match_details(match_id=3687702200)

match.pop('players')
#print(match)

InsertData('test_table',match)

print("插入完成！")
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

