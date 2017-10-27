import pymysql
import sys

#mysql end
def InsertRank(model):
    #print(sys.stdin.encoding)

    conn = pymysql.connect(host='localhost', port=3306, user='devuser', passwd='xxxx',
                                     db='devuser', charset ='utf8')
    cur = conn.cursor()


    sql = "insert into mpb_rank ( rank_id, av_krName,rank_year,rank_month) "
    sql += "values ('{}','{}','{}',{})".format(
            model['rank_id'],model['krName'],
            model['rank_year'],model['rank_month'])

    cur.execute(sql)
    cur.close()
    conn.close()
