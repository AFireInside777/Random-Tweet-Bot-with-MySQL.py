import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy.sql import func
import pymysql
import random
from twitter import *
import time

conn = "mysql+pymysql://stegulardev7:TrivieTime203@stegulardev7.mysql.pythonanywhere-services.com/stegulardev7$TriviaDB2" #Database URL

app = Flask(__name__)
app.config['SECRET_KEY'] = "bx0eKxecxd2xfaxb8x89x8bDel" #For use with sessions and cookies
app.config["SQLALCHEMY_DATABASE_URI"] = conn
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

api = Twitter(auth=OAuth(
token='1286447442775375877-qVh2SyyNg1g1uJq2pz2cd3KK1yhcui', #APIKey
token_secret='h2SMmEnK5EFBTzAjFMTROZFBvLgBE86CLeFnwTOLuY5z3', #APIKeySecret
consumer_key='Ywz0LJrAQtdB9JvlBQsbGk7E8', #BearerToken
consumer_secret='HoZ6O0IzZ0rO294dYsej72zPnolF3a2mZPfXpYOyaBFBodk2eS' #AccessTokenandSecret
))

class TriviaFacts(db.Model):
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    triviafact = db.Column(db.String(2500))

    def __init__(self, triviaobject):
        self.triviafact = triviaobject

engine = sqlalchemy.create_engine(conn)

meta_data = sqlalchemy.MetaData(bind=engine)

sqlalchemy.MetaData.reflect(meta_data)

trivia_table = meta_data.tables['trivia_facts']

result = sqlalchemy.select([sqlalchemy.func.count()]).select_from(trivia_table).scalar()


def gettriv(theid):
    s = trivia_table.select().where(trivia_table.c.id==theid)
    engineconnect = engine.connect()
    newresult = engineconnect.execute(s)

    for triv in newresult:
        finalresult = triv[1]
    return finalresult

def posttweet():
    idselect = random.randrange(0, result)
    tweet = gettriv(idselect)
    newstatus = api.statuses.update(status=tweet)

posttweet()


# @app.route("/gamingtriv")
# def getgaming():
#     gaminglist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
#     21, 23, 24, 25, 26, 27, 30, 32, 33, 34, 35, 36, 37, 38, 40, 42, 43, 44, 45, 48, 50, 
#     51, 54, 55, 56, 57, 58, 59, 60, 61]
#     selecttriv2 = gettriv(random.choice(gaminglist))
#     return selecttriv2

# @app.route("/techtriv")
# def gettech():
#     techlist = [22, 28, 29, 31, 32, 39, 41, 46, 47, 49,
#     52, 53, 64, 69, 76, 77, 78, 79, 86, 88,
#     92, 93, 94, 95, 96, 97, 98, 99, 100, 101,
#     102, 104, 108, 109, 110, 111, 112, 116, 118, 119,
#     121, 125, 132, 133, 134, 135, 136, 137, 138, 141]
#     selecttriv3 = gettriv(random.choice(techlist))
#     return selecttriv3

#db.create_all()
#db.session.commit()

