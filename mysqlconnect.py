from sshtunnel import SSHTunnelForwarder
from common.get_config import Get_config
import pymysql, json

# 连接信息
ssh = json.loads(Get_config().get_data("mysql", "ssh_connect"))
local = json.loads(Get_config().get_data("mysql", "local_connect"))


class mysql_connetc():
    def __ssh(self, addr, ssh_username, ssh_private_key_password, remote_bind_address, user, passwd):
        server = SSHTunnelForwarder(
            eval(addr),
            ssh_username=ssh_username,
            ssh_private_key_password=ssh_private_key_password,
            # 私钥文件位置
            ssh_pkey='F:/Python_file/Test_work/config/testuser',
            remote_bind_address=eval(remote_bind_address))
        return server, user, passwd

    # 通过ssh连接数据库
    def connect_ssh(self, db, sql, ssh_data=ssh, console_num=0):
        """
            :param console_num 查询结果数据量，默认输出全部
            :param ssh_data 连接ssh的数据，以解包的形式传入
            :param sql sql语句
            :param db  连接的数据库
        """
        server, user, passwd = self.__ssh(**ssh_data)
        server.start()
        conn = pymysql.connect(host='127.0.0.1', port=server.local_bind_port, user=user, passwd=passwd, db=db)
        # 创建游标
        cur = conn.cursor()
        # 执行sql
        cur.execute(sql)
        # 输出结果,console_num控制输出的查询结果条数，默认为输出全部
        if console_num == 0:
            res = cur.fetchall()
        elif console_num == 1:
            res = cur.fetchone()
        else:
            res = cur.fetchmany(console_num)
        # 关闭服务
        cur.close()
        conn.close()
        server.close()
        return res

    # 直接通过IP进行数据库连接
    def connect_db(self, db, sql, console_num=0, connect_data=local):
        host = connect_data["host"]
        port = int(connect_data["port"])
        user = connect_data["user"]
        passwd = connect_data["passwd"]

        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)
        cur = conn.cursor()
        cur.execute(sql)

        # 输出结果,console_num控制输出的查询结果条数，默认为输出全部
        if console_num == 0:
            res = cur.fetchall()
        elif console_num == 1:
            res = cur.fetchone()
        else:
            res = cur.fetchmany(console_num)

        # 关闭服务
        cur.close()
        conn.close()
        return res

