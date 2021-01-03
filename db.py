import sqlite3


class Database(object):

    __DB_LOCATION = "test.db"

    def __init__(self):
        self.connection = sqlite3.connect(self.__DB_LOCATION)
        self.cursor = self.connection.cursor()


    def __exit__(self, ext_type, exc_value, traceback):

        self.cursor.close()

        if isinstance(exc_value, Exception):

            self.connection.rollback()

        else:

            self.connection.commit()

        self.connection.close()


    def __enter__(self):

        return self

    # Creates Necessary Databases
    def create_loan_databases(self):

        self.execute('''CREATE TABLE IF NOT EXISTS  LOAN
         (ID INTEGER PRIMARY KEY AUTOINCREMENT   NOT NULL,
         EMAIL           TEXT    NOT NULL,
         LOAN_AMOUNT    DOUBLE     NOT NULL,
         INTEREST_RATE       DOUBLE     NOT NULL,
         REPAYMENT_TERMS INT NOT NULL,
         CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL);''')

        self.execute('''CREATE TABLE IF NOT EXISTS LOAN_DETAILS
         (ID INTEGER PRIMARY KEY AUTOINCREMENT   NOT NULL,
         TERM_NO INT NOT NULL,
         EMAIL           TEXT    NOT NULL,
         PRINCIPAL    DOUBLE     NOT NULL,
         INTEREST        DOUBLE     NOT NULL,
         TOTAL_AMOUNT DOUBLE NOT NULL,
         PAYMENT_DUE_DATE TIMESTAMP  NOT NULL,
         PAYMENT_TIME TIMESTAMP  NULL,
         LOAN_STATUS BOOL DEFAULT 0 ,
         CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL);''')

        self.commit()


    def close(self):
        """close sqlite3 connection"""
        self.connection.close()


    # execute funtion to execute query  efficiently
    def execute(self, new_query):
        """execute a row of data to current cursor"""

        try:
            self.cursor.execute(new_query)

        except Exception as err:
            print('Query Failed: %s\nError: %s' % (new_query, str(err)))

        finally:
            self.commit()


   # commit funtion to commit  efficiently
    def commit(self):
        """commit changes to database"""
        self.connection.commit()


# _DEFAULT = Database()


# def Default():
#   """Returns the default Database."""
#   return _DEFAULT
