'''
跟业务数据库相关的操作
'''
from jinRongzonghe.caw.Mysql import Mysql

class DbOp:
    def delete_user(self,db,mobilephone):
        '''
        根据手机号删除用户
        :param db:
        :param mobilephoe:
        :return:
        '''

        mysql = Mysql()
        conn = mysql.connect(db)
        # print(conn)
        mysql.execute(conn, f"delete from member where mobilephone={mobilephone};")
        mysql.disconnect(conn)