#!/usr/bin/env python

from sys import argv
from getpass import os
import mysql.connector

def gethost():
    if len(argv) > 1:
        return sys.argv[1]

    return 'localhost'


def main():
    uid = os.getuid()
    db_user = os.getlogin()
    db_host = gethost()
    db_password = 'UEf4JBvAfY'
    db_name = 'insdb'
    db_table = db_name + '.uniqid'
    def_values = (uid, db_user, 0)

    db_access = {
            'user': db_user,
            'password': db_password,
            'host': db_host,
            'database': db_name
            }

    sql_create_table = (
            'CREATE TABLE IF NOT EXISTS {} ('
                'uid int(255) NOT NULL UNIQUE,'
                'username varchar(31) NOT NULL,'
                'counter int(255) NOT NULL'
            ');'.format(db_table)
            )

    sql_insert_row = (
            'INSERT INTO {} VALUES {};'.format(db_table, def_values)
            )

    sql_read_counter = (
            'SELECT counter FROM {} WHERE uid = {};'.format(db_table, uid)
            )

    sql_update_counter = 'UPDATE {} set counter = {} WHERE uid = {};'

    db_connect = mysql.connector.connect(**db_access)
    db_cursor = db_connect.cursor()
    db_cursor.execute(sql_create_table)

    try:
        db_cursor.execute(sql_insert_row)
    except:
        db_cursor.execute(sql_read_counter)
        counter = db_cursor.fetchall()[0]
        db_cursor.execute(sql_update_counter.format(db_table,
            counter[0] + 1, uid))

    db_cursor.close()
    db_connect.close()

if __name__ == '__main__':
    main()
