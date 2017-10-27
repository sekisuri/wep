import pymysql
import sys

#mysql end
def InsertName(avname):
    #print(sys.stdin.encoding)

    conn = pymysql.connect(host='localhost', port=3306, user='devuser', passwd='jong',
                                     db='devuser', charset ='utf8')
    cur = conn.cursor()


    sql = "insert into init_av (av_name) "
    sql += "values ('{}')".format(avname)

    cur.execute(sql)
    cur.close()
    conn.close()
