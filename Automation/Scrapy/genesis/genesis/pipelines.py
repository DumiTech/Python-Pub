# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
import random

random_fingerprint = random.randint(999999999999, 999999999999999899)
db_path = "database/myquotes_{}.db".format(random_fingerprint)


class GenesisPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect(db_path)
        self.curs = self.conn.cursor()

    def create_table(self):
        self.curs.execute(
            """
            DROP TABLE IF EXISTS quotes_tb
            """)
        self.curs.execute(
            """create table quotes_tb(
            title text,
            author text,
            tags text)"""
        )

    def process_item(self, item, spider):
        self.store_db(item)
        print("Pipeline: " + item["title"][0])
        return item

    def store_db(self, item):
        self.curs.execute("""INSERT INTO quotes_tb VALUES (?,?,?)""",(
            item['title'][0],
            item['author'][0],
            item['tags'][0],
        ))
        self.conn.commit()