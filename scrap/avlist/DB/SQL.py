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
	conn = pymysql.connect(host='localhost', port=3306, user=USER, passwd=PASS,
                                     db=DB, charset ='utf8')
    cur = conn.cursor()

	sql = "insert ignore into mpb_rank ( rank_id, hentaku_name,av_krName,av_enName,av_jaName,"
	sql += "av_height,av_bust,av_waist,av_hip,av_bustcup) "
    sql += "values ('{}','{}','{}',{})".format(
            model['rank_id'],model['krName'],
            model['rank_year'],model['rank_month'])
    cur.execute(sql)
    cur.close()
    conn.close()
	