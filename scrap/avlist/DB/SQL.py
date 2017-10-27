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
