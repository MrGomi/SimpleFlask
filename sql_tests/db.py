import sqlite3

connection = sqlite3.connect("test_database.db")
#connection = sqlite3.connect(':memory:')

c = connection.cursor()

c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")

c.execute("INSERT INTO People VALUES('Martin', 'Tscholl', 33)")

#c.execute("DROP TABLE IF EXISTS People")

connection.commit()

connection.close()

################################# or more like this ########################################
from __future__ import unicode_literals # to store strings as unicode by default.
import sqlite3

# perform any SQL operations using connection here
with sqlite3.connect("test_database.db") as connection:
    c = connection.cursor()
    c.executescript("""
        DROP TABLE IF EXISTS People;
        CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
        INSERT INTO People VALUES('Martin', 'Tscholl', '33');
        """)

people_values = (
    ('Omid', 'Khorramshahi', 34),
    ('Ulrike', 'Strum', 28)
)

c.executemany("INSERT INTO People VALUES(?,?,?)", people_values)

# select all first and last names from people over age 30
c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
for row in c.fetchall():
    print row

# If we wanted to loop over our result rows one at a time instead of fetching them all at once:
c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
while True:
    row = c.fetchone()
    if row is None:
        break
    print row
