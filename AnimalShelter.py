from pymongo import MongoClient
import urllib.parse
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        #USER = urllib.parse.quote_plus(username)
        #PASS = urllib.parse.quote_plus(password)
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32202
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (username,password,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data=None):
    
        if data is not None:
            # data should be dictionary
            self.database.animals.insert_one(data)
            # requirement of the rubric to return True
            return True
        
        else:
        
            raise Exception("Nothing to save, because data parameter is empty")
            # requirement of the rubric to return False
            return False

# Create method to implement the R in CRUD.
    def read(self, output=None):
    
        if output is not None:
            # data should be dictionary
            o = list(self.database.animals.find(output)) 
            # requirement of the rubric to return data
            return o
        
        else:
        
            raise Exception("Nothing to find, because data parameter is empty")

# Create method to implement the U in CRUD.
    def update(self, find=None, update=None):
    
        if find is not None:
            # data should be dictionary
            o = self.database.animals.update_one(find, update)
            # requirement of the rubric to return data   
            return o.modified_count
        
        else:
        
            raise Exception("Nothing to update, because data parameter is empty")
    
# Create method to implement the D in CRUD.
    def delete(self, output=None):
    
        if output is not None:
            # data should be dictionary
            o = self.database.animals.delete_one(output)
            # requirement of the rubric to return data        
            return o.deleted_count
        
        else:
        
            raise Exception("Nothing to delete, because data parameter is empty")
