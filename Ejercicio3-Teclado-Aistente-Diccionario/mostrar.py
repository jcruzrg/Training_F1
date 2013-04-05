'''
Created on Apr 4, 2013

@author: jc
'''
from MainZoDb import Manejo_Db

db = Manejo_Db('Dataprueba.fs')
dbroot = db.dbroot
for key in dbroot.keys():
    print key + ':', dbroot[key]
db.close()
