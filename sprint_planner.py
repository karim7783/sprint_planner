#!/usr/bin/python

###############
### Imports ###
###############
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
        pass



if __name__ == '__main__':
    pass