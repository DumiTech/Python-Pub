import sqlite3
import random

random_fingerprint = random.randint(999999999999, 999999999999999899)
db_path = "database/myquotes_{}.db".format(random_fingerprint)

conn = sqlite3.connect(db_path)
print()
print(conn)
print()

curs = conn.cursor()


# curs.execute(
#     """create table quotes(
#     id int,
#     title text,
#     author text,
#     tags text
# )"""
# )

# curs.execute("""insert into quotes values (1, 'Python The King', 'Py', '.py')""")
# curs.execute("""insert into quotes values (2, 'Java is a beast', 'Java', '.java')""")

conn.commit()
conn.close()
