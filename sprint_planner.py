#!/usr/bin/python

###############
### Imports ###
###############
import argparse
import sqlite3
###############
###############

class sprint_data_store:
    def __init__(self, *args, **kwargs):
        self._dbconnection = sqlite3.connect('sprint_data.db')
        self._cursor = self._dbconnection.cursor()

    def enumerate_teams(self):
        pass

    def validate_data_store(self):
        validation_query = self.return_query_output("SELECT name FROM sqlite_master WHERE type='table' AND name='teams'")
        if validation_query:
            pass
        else:
            self.initialize_table_structure()

    def return_query_output(self, select_query):
        self._cursor(select_query)
        data_rows = self._cursor.fetchall()
        return data_rows

    def run_transaction(self, insert_or_update):
        self._cursor.execute(insert_or_update)
        self._dbconnection.commit()

    def initialize_table_structure(self):
        pass

class agile_sprint:
    def __init__(self):
        self._data = sprint_data_store()
    


if __name__ == '__main__':
    pass

