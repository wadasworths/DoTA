''''' 
Insert dict into database 
@author: longfellow 
''' 
#-*- encoding:utf-8 -*-
 
import pymysql 
  
def InsertData(TableName,dic):   
	try: 
		db = pymysql.connect('localhost','root','******','testdb')
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
			db.commit()
			db.close()
		except:
			db.rollback()
	except:
		print("异常报错！")

if __name__ == '__main__':
	dic={"a":"b","c":"d"}
	InsertData('test',dic)
