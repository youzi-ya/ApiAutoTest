'''
数据库的操作
'''
import pymysql

class Mysql:
    def connect(self,db):
        '''
        连接数据库
        :param db: 字典格式
        :return:
        '''
        ip=db['ip']
        port=int(db['port'])
        name=db['name']
        user=db['user']
        pwd=db['pwd']
        try:
            comn=pymysql.connect(host=ip,port=port,user=user,password=pwd,
                            charset='utf8',database=name)
            print(f"连接数据库{ip}:{port}成功")
            return comn
        except Exception as e:
            print(f"连接数据库异常，异常信息为{e}")

    def execute(self,comn,sql):
        try:
            cursor=comn.cursor=comn.cursor()#获取游标
            cursor.execute(sql)    #使用游标执行sql
            comn.commit()
            cursor.close()
            print(f"执行sql 语句{sql}")

        except Exception as e:
            print(f"执行sql 语句异常，异常信息为{e}")

    def disconnect(self,comn):
        '''
        断开连接
        :param comn:
        :return:
        '''
        try:
            comn.close()
        except Exception as e:
            print(f"断开数据库异常，异常信息为{e}")



if __name__ == '__main__':
    db={"ip":"192.168.150.52","port":"3306","name":"apple","user":"root","pwd":"123456"}
    mysql=Mysql()
    conn=mysql.connect(db)
    # print(conn)
    mysql.execute(conn,"delete from member where mobilephone=15510092369;")
    mysql.disconnect(conn)