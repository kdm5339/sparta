from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.db스파르타

matrix = db.movies.find_one({'title':'매트릭스'})


same_matrix = list(db.movies.find({'star':matrix['star']}))
for movie in same_matrix:
    print(movie['title'])

db.movies.update_many({'star':matrix['star']},{'$set':{'star':0}})