'''
Created on Apr 4, 2013

@author: jc
'''
from ZODB import FileStorage, DB
import transaction


class Manejo_Db(object):
    def __init__(self, path):
        self.storage = FileStorage.FileStorage(path)
        self.db = DB(self.storage)
        self.connection = self.db.open()
        self.dbroot = self.connection.root()

    def close(self):
        self.connection.close()
        self.db.close()
        self.storage.close()
