import pymongo
uri = "mongodb+srv://abhishek:devilnat007@cluster0.nualpoa.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)
db = client.test
print(db)
a = {
        "name": 'abhishek',
        "roll": 191500039,
        "email": 'abhishek.singh2_cs19@gmal.com'
    }
b= {
    "name": 'abhishek singh',
    "roll": 191500038,
    "email": 'abhishek.singh_cs19@gmal.com'
}
mongodb = client['mongotest']
coll = mongodb['test']
coll.insert_one(b)