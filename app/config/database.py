""" Settings to database conection."""

#Database
import os
import mysql.connector
from mysql.connector import errorcode

#Settings
from .settings import config, DB_NAME, TABLES




class DatabaseManagement:
    """Class it has the methods to manage the database in mysql."""


    def create_database(self, cursor):
        """Create database if not exists."""
        try:
            cursor.execute(
                f"CREATE DATABASE {DB_NAME} DEFAULT CHARACTER SET 'utf8'"
            )
        except mysql.connector.Error as err:
            print(f"Failed creating database: {err}")
            exit(1)

    def use_database(self, cursor):
        """Function to focus in the database."""
        try: 
            cursor.execute(f"USE {DB_NAME}")
        except mysql.connector.Error as err:
            print(err)
            exit(1)

    def create_tables(self, cursor):
        """Create the neccesary tables products and registers."""
        for table_name in TABLES:
            table_desciption = TABLES[table_name]
            try:
                print(f"Creating table{table_name}", end ='')
                cursor.execute(table_desciption)
            except mysql.connector.Error as err:
                print(err.msg)
            else:
                print("OK")
    
    def connect_to_database(self):
        """connection to database."""
        try:
            cnx = mysql.connector.connect(**config)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
                cnx = mysql.connector.connect(user='root', password='Protection1989')
                cursor = cnx.cursor()
                self.create_database(cursor)
                self.use_database(cursor)
                self.create_tables(cursor)
                cursor.close()
            else:
                print(err)
        else:
            cnx.close()
    
    def proof_database(self):
        try:
            cnx = mysql.connector.connect(**config)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            else:
                print(err)
        return cnx