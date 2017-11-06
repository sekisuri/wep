import pymysql
import sys
from .user import USER,PASS,DB
#mysql end
def InsertName(avname):
    #print(sys.stdin.encoding)

    conn = pymysql.connect(host='localhost', port=3306, user=USER, passwd=PASS,
                                     db=DB, charset ='utf8')
    cur = conn.cursor()


    sql = "insert ignore into av_index (index_name) "
    sql += "values ('{}')".format(avname)

    cur.execute(sql)
    cur.close()
    conn.close()

def InsertProfile(data):
	conn = pymysql.connect(host='localhost', port=3306, user=USER, passwd=PASS, db=DB, charset ='utf8')
	sqlconn = conn.cursor()

	sql = "insert ignore into av_profile (avdb_id,hentaku_name, av_krName, av_enName, av_jaName,"
	sql += "av_height, av_size, av_bustcup, av_birthday, av_debut, main_pic,"
	sql += "av_pic1, av_pic2, av_pic3, av_pic4, av_pic5 ) "
	sql += "values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
		data['avdb'],data['hentaku'],data['krname'],data['enname'],data['janame'],
		data['height'],data['size'],
		data['bustcup'],data['birthday'],data['debut'],data['mainpic'],data['pic1'],
		data['pic2'],data['pic3'],data['pic4'],data['pic5'])
		
	sqlconn.execute(sql)
	sqlconn.close()
	conn.close()
	