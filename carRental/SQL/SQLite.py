import sqlite3
conn = sqlite3.connect("carRental.db")
c = conn.cursor()

# c.execute("CREATE TABLE CAR (carId INTEGER PRIMARY KEY, color TEXT, brand TEXT, model TEXT, numPlate TEXT)")
# c.execute("CREATE TABLE PLACE (placeId INTEGER PRIMARY KEY, name TEXT, cap INTEGER)")
# c.execute("CREATE TABLE CARxPLACE ( carId INTEGER, placeId INTEGER)")
# c.execute("DELETE FROM CAR")
#c.execute("DELETE FROM PLACE")
# c.execute("INSERT INTO CAR VALUES(1, 'red', 'Tesla', 'X', 'hg 44 978')")
# c.execute("INSERT INTO CAR VALUES(2, 'blue', 'opel', 'e', 'hg 65 578')")
# conn.commit()
c.execute("SELECT numPlate FROM CAR")
#
print(c.fetchall())


# conn.commit()
