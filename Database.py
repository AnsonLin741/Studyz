import sqlite3
import time


class Database:
    def __init__(self, db):
        self._database = db
        self.create_table()

    @property
    def database(self):
        return self._database

    @database.setter
    def database(self, db):
        self._database = db

    def create_table(self):
        """create a data base"""
        connect = sqlite3.connect(self._database)
        cursor = connect.cursor()
        sql = "CREATE TABLE IF NOT EXISTS data(username TEXT, password TEXT, created_time TEXT)"
        cursor.execute(sql)
        if not self.is_has('admin'):  # admin username must be 'admin'
            created_time = self.get_time()
            default = "INSERT INTO data(username, password, created_time) VALUES('admin', 'admin123', ?)"  # default admin password and username
            cursor.execute(default, (created_time,))
        connect.commit()
        connect.close()

    def insert_table(self, username, password):
        connect = sqlite3.connect(self._database)
        cursor = connect.cursor()
        if self.is_has(username):
            # print("Already exits username {}".format(username))  # 测试使用
            return True  # 已经有该元素的时候返回一个 True 提供外界接口
        else:
            created_time = self.get_time()
            sql = 'INSERT INTO data (username, password, created_time) VALUES(?,?,?)'
            cursor.execute(sql, (username, password, created_time))
            connect.commit()
        connect.close()

    def read_table(self):
        """读取数据库中的所有元素"""
        connect = sqlite3.connect(self._database)
        cursor = connect.cursor()
        sql = 'SELECT * FROM data ORDER BY username'
        result = cursor.execute(sql)
        data = result.fetchall()
        connect.commit()
        connect.close()
        return data

    def update_table(self, username, password):
        """更新数据库中的数据"""
        connect = sqlite3.connect(self._database)
        cursor = connect.cursor()
        sql = 'UPDATE data SET password =? WHERE username=? '
        cursor.execute(sql, (password, username))
        connect.commit()
        connect.close()

    def find_password_by_username(self, username):
        """根据用户名来查找用户的密码"""
        connect = sqlite3.connect(self._database)
        cursor = connect.cursor()
        sql = 'SELECT password FROM data WHERE username=?'
        result = cursor.execute(sql, (username,))
        connect.commit()
        found_data = result.fetchall()
        connect.close()
        return found_data

    def delete_table_by_username(self, username):
        """通过用户名称删除数据"""
        connect = sqlite3.connect(self._database)
        cursor = connect.cursor()
        sql = 'DELETE FROM data WHERE  username=?'
        cursor.execute(sql, (username,))
        connect.commit()
        connect.close()

    def is_has(self, username):
        """判断数据库中是否包含用户名信息"""
        connect = sqlite3.connect(self._database)
        cursor = connect.cursor()
        sql = 'SELECT * FROM data WHERE username=?'
        result = cursor.execute(sql, (username,))
        connect.commit()
        all_data = result.fetchall()
        connect.close()
        if all_data:
            return True
        else:
            return False

    def clear(self):
        """clear all data in database"""
        connect = sqlite3.connect(self._database)
        cursor = connect.cursor()
        sql = "DELETE FROM data"
        cursor.execute(sql)
        connect.commit()
        connect.close()

    @staticmethod
    def get_time():
        date = time.localtime()
        created_time = "{}-{}-{}-{}:{}:{}".format(date.tm_year, date.tm_mon,
                                                  date.tm_mday,
                                                  date.tm_hour, date.tm_min,
                                                  date.tm_sec)
        return created_time


if __name__ == '__main__':
    data = Database('./data.db')
    # data.insert_table('admin', 'password')
    data_ = data.read_table()
    print(data_)
    # for i in range(23):  
    #     data.insert_table(chr(i + 65) * 5, chr(i + 65) + chr(i + 66) * 5)
