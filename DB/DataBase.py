"""
    Test with database
    - Curently have the basic elements of creation, appending data and deleting

    - Will ultimatly use to store the AI side of the data for each run

    - Add in try except for each - example https://pynative.com/python-sqlite-delete-from-table/
"""
import sqlite3 as sl

con = sl.connect("my-test.db")


class DataBase:
    def __init__(self):
        pass

    def CreateTableAnimal(self) -> None:
        """Create the base Animal Table in the DB"""

        with con:
            con.execute(
                """
                CREATE TABLE ANIMAL(
                    id INTERGER NOT NULL PRIMARY KEY,
                    animal_type TEXT,
                    alive TEXT
                );
            """
            )

    def AppendToTable(self) -> None:
        sql = "INSERT INTO ANIMAL (id, animal_type, alive) values (?,?,?)"
        data = [(1, "FOX", "YES"), (2, "WOLF", "YES"), (3, "FOX", "NO")]
        with con:
            con.execute(sql, data)

    def DeleteFromTable(self) -> None:
        with con:
            con.execute("DELETE FROM ANIMAL WHERE id=2")

    def PrintTable(self) -> None:
        with con:
            data = con.execute("SELECT * FROM ANIMAL")
            for row in data:
                print(row)
