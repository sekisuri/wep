#mysql
import pymysql
import sys
#mysql end
def InsertProfile(model):
    #print(sys.stdin.encoding)

    conn = pymysql.connect(host='localhost', port=3306, user='devuser', passwd='jong',
                                     db='devuser', charset ='utf8')
    cur = conn.cursor()


    sql = "insert into av_model ( av_krName, av_enName,av_jaName,"
    sql += "av_height,av_bust,av_waist,av_hip,"
    sql += "av_bustcup,av_birthday,av_debut,av_sns1) "
    sql += "values ('{}','{}','{}',{},{},{},{},'{}','{}','{}','{}')".format(
            model['krName'],model['enName'],model['jaName'],
            model['Height'],model['Bust'],model['Waist'],model['Hip'],
            model['CupSize'],model['Birthday'],model['Debut'],model['SnS1'])

    cur.execute(sql)
    cur.close()
    conn.close()

def InsertTitle(title):
    conn = pymysql.connect(host='localhost', port=3306, user='devuser', passwd='jong',
                                     db='devuser', charset ='utf8')
    cur = conn.cursor()
    sql = "insert into av_title ( av_id, title_name,release_date,"
    sql += "komaker,title_age,mosaic) "
    sql += "values ({},'{}','{}','{}',{},'{}')".format(
            title['avId'],title['titleName'],title['releaseDate'],
            title['koMaker'],title['titleAge'],title['Mosaic'])

    cur.execute(sql)
    cur.close()
    conn.close()
