import pymongo

# FOR FLASK
if __name__=="__main__":
# FOR FLASK
    print("mongodb")
# DATABASE CONNECT
client = pymongo.MongoClient("mongodb://localhost:27017/")
# DATABASE CONNECT
print(client)

# to list all data base
# client.list_database_name()

list_all_db = client.list_database_names()
print(f"Here is the list of databasesbelow:\n {list_all_db}")

'''
output
Here is the list of databasesbelow:
 ['admin', 'config', 'employee', 'local', 'student']
'''
