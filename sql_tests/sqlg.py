# executemany() method

# import the sqlite3 library
import sqlite3

# create a new database it the database doesn't aleady exist
with sqlite3.connect("new.db") as conn:
    # get the cursor object used to execute SQL commands
    c = conn.cursor()
     
    c.execute("""SELECT population.city, population.population, regions.region 
                FROM population, regions WHERE population.city = regions.city
                ORDER by population.city ASC""")

    rows = c.fetchall()

    for r in rows:
        print "City: "+ r[0]
        print "Population: " + str(r[1])
        print "Region: " + r[2]
        print 
