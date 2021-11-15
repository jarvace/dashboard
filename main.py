import MySQLdb


# 连接数据库
def fetch_db():
    # 连接
    db = MySQLdb.connect(host='localhost', user='root', passwd='root', db='mysql_model', port=3306, charset='utf8')
    # 获取操作游标
    cursor = db.cursor()
    try:
        # 查询data表
        cursor.execute("select * from data")
        data = cursor.fetchall()
        # 查询forcast表
        cursor.execute("select * from forcast")
        forecast = cursor.fetchall()
    except:
        print("Error: unable to fetch data")
    # 函数返回值
    return data, forecast


# 主函数
if __name__ == '__main__':
    data, forecast = fetch_db()
    print(data)



