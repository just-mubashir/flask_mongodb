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
# DICT FOR ADDING DATA TO MONGO DB
stud_dict_db = [
    {"name":"alpha", "age":"34", "dept": "it", "location": "mumbai", "subjects": "computers"},
    
    {"name":"beta", "age":"33", "dept": "commerce", "location": "hyderabad", "subjects": "economics"},
    
    {"name":"gamma", "age":"31", "dept": "science", "location": "chennai", "subjects": "genetics"},
    
    {"name":"delta", "age":"29", "dept": "arts", "location": "kolkata", "subjects": "music"},
    
    {"name":"penta", "age":"38", "dept": "mass", "location": "banglore", "subjects": "media"},
    
    {"name":"hexa", "age":"37", "dept": "arts", "location": "delhi", "subjects": "painting"}
    ]

collection.insert_many(stud_dict_db)

# it automatically gives an id for every documnet, we can ad it manually by following

db = client ["employee"]
collection = db["data_of_employee"]
emp_dict_db = [
    {"_id":1,"name":"alpha_employee", "age":"34", "dept": "it", "location": "mumbai", "subjects": "computers"},
    
    {"_id":2,"name":"beta_employee", "age":"33", "dept": "commerce", "location": "hyderabad", "subjects": "economics"},
    
    {"_id":3,"name":"gamma_employee", "age":"31", "dept": "science", "location": "chennai", "subjects": "genetics"},
    
    {"_id":4,"name":"delta_employee", "age":"29", "dept": "arts", "location": "kolkata", "subjects": "music"},
    
    {"_id":5,"name":"penta_employee", "age":"38", "dept": "mass", "location": "banglore", "subjects": "media"},
    
    {"_id":6,"name":"hexa_employee", "age":"37", "dept": "arts", "location": "delhi", "subjects": "painting"}
    ]
collection.insert_many(emp_dict_db)

# first database is students
# second id emmployee