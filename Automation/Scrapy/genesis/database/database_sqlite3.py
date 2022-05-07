import sqlite3


conn = sqlite3.connect("database/myquotes.db")
curs = conn.cursor()


# curs.execute(
#     """create table quotes(
#     id int,
#     title text,
#     author text,
#     tags text
# )"""
# )

curs.execute("""insert into quotes values (1, 'Python The King', 'Py', '.py')""")
curs.execute("""insert into quotes values (2, 'Java is a beast', 'Java', '.java')""")

conn.commit()
conn.close()
