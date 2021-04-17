import sqlite3
import argparse

# second commit

# write decorator function for connection
def create_table(db_name, table_name):
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    cur.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} (name text, price real)''')
    con.commit()
    con.close()


# implementation this function
def insert_into_table(db_name, table_name, args):
    pass


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--command', help='command name')
parser.add_argument('--arguments', default="", help='command name')
parser.add_argument('--table', help='Table name')
parser.add_argument('--db', help='db name')


args = parser.parse_args()
locals()[args.command](args.db, args.table)

# python3 pysqlite.py --table "menu" --db "bla2.db" --command create_table




# # Insert a row of data
# cur.execute("INSERT INTO menu (price, name) VALUES (2000, 'pide')")
# # cur.execute("INSERT INTO menu VALUES ('ost', 2500)")
# # Save (commit) the changes
#
# a = cur.execute("SELECT * FROM menu").fetchall()
# print(a)
# # We can also close the connection if we are done with it.
# # Just be sure any changes have been committed or they will be lost.

# second branch
# second commit
