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
find_one_document = collection.find_one({"name":"alpha_employee"})
print (find_one_document)

'''
output

{'_id': 1,
 'name': 'alpha_employee',
  'age': '34', 'dept': 'it',
   'location': 'mumbai',
    'subjects': 'computers'}
    '''
find_all_document = collection.find({"dept":"arts"})
for item in find_all_document:
    print (item)
'''
output
{'_id': 1, 'name': 'alpha_employee', 'age': '34', 'dept': 'it', 'location': 'mumbai', 'subjects': 'computers'}
{'_id': 4, 'name': 'delta_employee', 'age': '29', 'dept': 'arts', 'location': 'kolkata', 'subjects': 'music'}
{'_id': 6, 'name': 'hexa_employee', 'age': '37', 'dept': 'arts', 'location': 'delhi', 'subjects': 'painting'}
'''
#  if user want yo exclude any column

find_all_document = collection.find({"dept":"arts"}, {"age":0,"_id":1})
for item in find_all_document:
    print (item)
for item in find_all_document:
    print(f"this is count {find_all_document.count}")
'''
# THIS IS COMMING FROM PREVIOUS PRINT STAT
# {'_id': 1, 'name': 'alpha_employee', 'age': '34', 'dept': 'it', 'location': 'mumbai', 'subjects': 'computers'}
# {'_id': 4, 'name': 'delta_employee', 'age': '29', 'dept': 'arts', 'location': 'kolkata', 'subjects': 'music'}
# {'_id': 6, 'name': 'hexa_employee', 'age': '37', 'dept': 'arts', 'location': 'delhi', 'subjects': 'painting'}

# Here it gives the output excluding "age" hence is assigned "=0" i.e to hide, where "=1" is to show

{'_id': 4, 'name': 'delta_employee', 'dept': 'arts', 'location': 'kolkata', 'subjects': 'music'}
{'_id': 6, 'name': 'hexa_employee', 'dept': 'arts', 'location': 'delhi', 'subjects': 'painting'}
'''
#  to count

#  to count 
# 