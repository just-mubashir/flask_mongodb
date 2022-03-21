from turtle import update
import pymongo

# FOR FLASK
if __name__=="__main__":
# FOR FLASK
    print("mongodb")
# DATABASE CONNECT
client = pymongo.MongoClient("mongodb://localhost:27017/")
# DATABASE CONNECT
print(client)


db = client ["employee"]
collection = db["data_of_employee"]

find_1 = {"name":"alpha_employee"}
update_1 = {"$set":{"location":"mars"}}
collection.update_one(find_1, update_1)
# update >>> update only works with $ operators
#  {$set:{dict}}
# example "{"$set":{"location":"mars"}}"

'''
#  IN MONGODB COMPASS
_id
:
1
name
:
"alpha_employee"
age
:
"34"
dept
:
"it"
location
:
"mars"
subjects
:
"computers"
'''

#  UPDATE MANY

db = client ["student"]
collection = db["data_of_students"]

find_2 = {"name":"alpha"}
update_2 = {"$set": {"age":"0"}}
collection.update_many(find_2, update_2)

'''
output

_id
:
6238d3f27080622c2767593c
name
:
"alpha"
age
:
"0"

_id
:
6238d68be4a7409cb98936e1
name
:
"alpha"
age
:
"0"
dept
:
"it"
location
:
"mumbai"
subjects
:
"computers"'''
