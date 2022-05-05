import sqlite3

conn = sqlite3.connect("database/myquotes.db")
curs = conn.cursor()

# curs.execute(
#     """create table quotes(
#     title text,
#     author text,
#     tags text
# )"""
# )

curs.execute("""insert into quotes values ('Python the King', 'Python', 'py')""")

conn.commit()
conn.close()
