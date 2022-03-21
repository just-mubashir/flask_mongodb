# to delete a db
import pymongo

# FOR FLASK
if __name__=="__main__":
# FOR FLASK
    print("mongodb")
# DATABASE CONNECT
    client = pymongo.MongoClient("mongodb://localhost:27017/")
# DATABASE CONNECT
    print(client)

db = client ["student"]
collection = db["data_of_students"]
# delete one
del_db_1 = {"name":"penta"}
collection.delete_one(del_db_1)
# deleted pentafrom data base

# delete many
del_from = {"name":"alpha"}
del_db_many = collection.delete_many(del_from)
print(f"EXECUTED:\n {del_from}")
'''
output

EXECUTED:
 {'name': 'alpha'}
 
 deleted alpha'''