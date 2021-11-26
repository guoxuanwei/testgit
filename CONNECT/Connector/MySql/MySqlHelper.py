import pymysql
import configparser
import os


class MySql:
    def __init__(self):
        conf = configparser.ConfigParser()
        dirname = os.path.join(os.path.dirname(__file__), 'confing')
        conf.read(dirname + "\config.ini")
        self.host = conf.get('TEST_DB', 'host')
        self.port = conf.get('TEST_DB', 'port')
        self.username = conf.get('TEST_DB', 'username')
        self.password = conf.get('TEST_DB', 'password')
        self.charset = conf.get('TEST_DB', 'charset')
        self.database = conf.get('TEST_DB', 'database')

        # 连接数据库
        try:
            self.con = pymysql.connect(host=self.host, port=int(self.port), user=self.username, password=self.password,
                                       database=self.database, charset=self.charset)
            # 创建游标
            self.cur = self.con.cursor()
        except BaseException as e:
            print(f'连接数据库失败{e}')

    # 关闭连接
    def close(self):
        self.con.close()

    # 查询一条
    def get_one(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchone()
        self.close()
        return result

    # 查询所有数据
    def get_all(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchall()
        self.close()
        return result

    # 编辑操作
    def edit(self, sql):
        try:
            self.cur.execute(sql)
            self.con.commit()
            self.count = self.cur.rowcount
            self.close()
            return f'受影响行数{self.count}'
        except BaseException as e:
            print(f'操作发生错误{e}')

    # 插入数据
    def insert(self, sql):
        return self.edit(sql)

    # 更新数据
    def update(self, sql):
        return self.edit(sql)

    # 删除数据
    def delete(self, sql):
        return self.edit(sql)


if __name__ == '__main__':
    my = MySql()
    sql = 'delete from s where sname="张三"'
    print(my.delete(sql))
