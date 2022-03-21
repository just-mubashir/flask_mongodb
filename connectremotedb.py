import pymongo
import urllib
# FOR FLASK
if __name__=="__main__":
# FOR FLASK
    print("mongodb")
# DATABASE CONNECT
client = pymongo.MongoClient(urllib.parse.quote_plus("mongodb+srv://codeatemail:<password>@cluster0.sb7o2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"))
# DATABASE CONNECT
print(client)

'''
output

mongodb
MongoClient(host=['mongodb%2bsrv%3a%2f%2fcodeatemail%3a%3cpassword%3e%40cluster0.sb7o2.mongodb.net%2fmyfirstdatabase%3fretrywrites%3dtrue%26w%3dmajority:27017'], document_class=dict, tz_aware=False, connect=True)

CONNECTED
'''