# -*- coding: utf-8 -*-

from scrapy.exceptions import DropItem
from pymysql import MySQLError
import logging
import pymysql
import settings

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class SespiderPipeline(object):
    def __init__(self):
        self.file = open('urls.txt', 'wb')
        self.connect = pymysql.connect(host=settings.MYSQL_HOST,
                                         user=settings.MYSQL_USER,
                                         password=settings.MYSQL_PASSWD,
                                         db=settings.MYSQL_DBNAME,
                                         charset='utf8',
                                         use_unicode=True)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        # self.file.write(item['title'][0] + ', ' + item['url'][0] + ', ' + "".join(item['snippet']) + '\n')
        # self.file.write(item['query'] + item['title'][0] + '\n')
        try:
            sql = "INSERT INTO DOCUMENTS (idx, query, title, url, snippet) VALUES (%s, %s, %s, %s, %s)"
            params = [item['idx'], 
                        self.connect.escape_string(item['query']), 
                        self.connect.escape_string(item['title']), 
                        self.connect.escape_string(item['url']),
                        self.connect.escape_string(item['snippet'])]
            
            self.cursor.execute(sql, params)
            self.connect.commit()
        except MySQLError as e:
            print('Got error {!r}, errno is {}'.format(e, e.args[0]))
        return item
