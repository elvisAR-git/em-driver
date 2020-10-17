
import sqlite3
"""
    Authored by Elvis moraa,
    This program was witten by me in aim of attempting to make a database driver application
    This can be ued to create and access databases using python's in built module
"""


class DatabaseModel:
    """
        The Database model class, contains methods for CRUD operations. It is the main 
        module that allows interfacing with the database file. other modules can perform queries
        to the database via its methods.       

        Attributes
        --
        \n
        None
        \n
        Methods
        ---
        create_table(database_name) ::
        \n
        example:
        \tcreate_table("Students")
        Creates a table in the database using a fieldset
        \n
        insert(table_name, fieldset) :: \n
        enters records into a table in the database
        \n
        update(self, table, data, condition):: \n
        updates a record or records based off a condition
        \n
        delete(self, table, condition):: \n
        Deletes a record from a table in the database based off a condition
        \n
        drop_table(self, table):: \n
        Deletes a table from the database completely
        \n
        get_all_from(self, table):: \n
        Returns all records from a table
        \n
        get_set_from(self, table, count):: \n
        Returns a number of records from a table
        \n
        filter_all_from(self, table, condition)::\n
        Returns a list of all records from the table that meet the specified condition
        \n
        filter_set_from(self, table, condition, count)::\n
        Returns a number of records from the table that meet the specified condition
        \n
    """

    def __init__(self, database_name):
        """
            Inputs
            ---------
            database_name : string
                \n
                the name of the database file to connect to
            \n
            Attributes
            ---------
            self.connection : sqlite connection object
                \n
            self.cursor : sqlite.cursor object
        """
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, field_set):
        """Creates a table in the database 

        Args:
        --
            table_name (str): string name for the table
            field_set (list): a list of fileds and attributes e.g
            ['id INTEGER PRIMARY KEY', 'name TEXT','age INTEGER']

        Returns:
        --
            [bool]: True=success
        """
        query = ""
        for field in field_set:
            if field_set.index(field) < (len(field_set)-1):
                query += field + ","
            else:
                query += field

        try:
            self.cursor.execute(f"Create TABLE {table_name} ({query})")
            self.connection.commit()
            return True
        except sqlite3.OperationalError as e:
            print(e.__str__())
            return False

    def insert(self, table, data):
        """Insert data into an existing table

        Args:
        ---
            table (str): table name
            data (tuple): data tuple to populate e.g (12,'Mary','2005-02-19')

        Returns:
        --
            bool: True=success
        """
        query = ""
        i = 0
        for d in data:
            if i < (len(data) - 1):
                try:
                    _ = int(d)
                    if type(d) == int:
                        d = str(d)
                except:
                    d = f'"{d}"'
                query += d + ","
            else:
                try:
                    _ = int(d)
                    if type(d) == int:
                        d = str(d)
                except:
                    d = f'"{d}"'
                query += d
            i += 1
        try:
            self.cursor.execute(f'INSERT INTO {table} VALUES ({query})')
            self.connection.commit()
            return True
        except sqlite3.OperationalError as e:
            print(e.__str__())
            return False

    def update(self, table, data, condition):
        """Updates a record in a table

        Args:
        --
            table (str): table name
            data (str): strings that present assignment
            condition (list): a list of conditions to be met for a record to be updates

        Returns:
        --
            bool: True=success
        """
        try:
            self.cursor.execute(f'UPDATE {table} SET {data} WHERE {condition}')
            self.connection.commit()
            return True
        except sqlite3.OperationalError as e:
            print(e.__str__())
            return False

    def delete(self, table, condition):
        """Deletes a single record from a table in the database based on the condition

        Args:
        --
            table (str): table name
            condition (list): a list of conditions

        Returns:
        --
            bool: True=success
        """
        try:
            query = f'DELETE FROM {table} WHERE {condition}'
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except sqlite3.OperationalError as e:
            print(e.__str__())
            return False

    def drop_table(self, table):
        """Deletes a table from the database

        Args:
        --
            table (str): table name

        Returns:
        --
            bool: True=success
        """
        try:
            query = f'DROP TABLE {table}'
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except sqlite3.OperationalError as e:
            print(e.__str__())
            return False

    def get_all_from(self, table):
        """Gets all records from the table

        Args:
        --
            table (str): table

        Returns:
        --
            data(list): a list of records
            or
            bool:False=fail
        """
        try:
            query = f'SELECT * FROM {table}'
            data = self.cursor.execute(query).fetchall()
            return data
        except sqlite3.OperationalError as e:
            print(e.__str__())
            return False

    def get_set_from(self, table, count):
        """Gets a number of records from a table

        Args:
        --
            table (str): table name
            count (int): number of records

        Returns:
        --
            list: records
        """
        try:
            query = f'SELECT * FROM {table}'
            data = self.cursor.execute(query).fetchmany(count)
            return data
        except sqlite3.OperationalError as e:
            print(e.__str__())
            return False

    def filter_all_from(self, table, condition):
        """Returns all records that meet the given conditions

        Args:
        --
            table (str): table name
            condition (str): a fomarted string of conditions

        Returns:
        --
            list: records
        """
        try:
            query = f'SELECT * FROM {table} WHERE {condition}'
            data = self.cursor.execute(query).fetchall()
            return data
        except sqlite3.OperationalError as e:
            print(e.__str__())
            return False

    def filter_set_from(self, table, condition, count):
        """Returns a set of records that meet the given condition

        Args:
        --
            table (str): table name
            condition (str): fomarted string of conditions
            count (int): number of records

        Returns:
        ---
            list: records
        """
        try:
            query = f'SELECT * FROM {table} where {condition}'
            data = self.cursor.execute(query).fetchmany(count)
            return data
        except sqlite3.OperationalError as e:
            print(e.__str__())
            return False
