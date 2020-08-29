import json
from pymongo import MongoClient
import pandas as pd
import numpy as np


def create_collection():
    client = MongoClient("mongodb+srv://asdf:@cluster0.ekw47.mongodb.net/?retryWrites=true&w=majority")
    mydatabase = client["mess"]
    global df1
    df1 = mydatabase["food"]
    print(mydatabase.list_collection_names())


def show():
    myd = df1.find()
    for i in myd :
        print(i)


def find_item(x) :
    myq = 	{'Food Item' : x}
    myd = 	df1.find(myq)
    print(f"Your food item {x} is ")
    for i in myd :
        print(i)


def max_taken():
    mydoc = df1.find().sort("Total people" , +1)
    print("This is in ascending order of the food items that people took")
    for x in mydoc :
          print(x)


def min_taken():
    mydoc = df1.find().sort("Total people" , -1)
    print("This is in descending order of the food items that people took")
    for x in mydoc :
          print(x)


def max_liked():
    mydoc = df1.find().sort("Total people" , +1)
    print("This is in ascending order of the food items that people liked")
    for x in mydoc :
          print(x)


def min_liked():
    mydoc = df1.find().sort("Total people" , -1)
    print("This is in descending order of the food items that people liked")
    for x in mydoc :
          print(x)


def add_upd_item():
    food = input("Enter the food item to add or update")
    myq =    {'Food Item' : food}
    myd = 	df1.find(myq)
    if (myd.count() == 0):
        takenf = float(input("Enter the fraction of people who took it  "))
        likedf = float(input("Enter the fraction of people (among the ones who took it only) who liked it  "))
        att = int(input("Enter the number of people who came to mess "))
        taken = float(takenf *att)
        liked = float(taken*likedf)
        new = {"Food Item" : food  , "%people(Ate)" : takenf , "%people(Like it)" : likedf , "Total people" : taken ,  "Number of people liking" : liked , "Attendence" : att}
        x = df1.insert_one(new)
        print(x)
        print("The new dataset is ")
        show()
    else :
        a = int(input("New attendence "))
        tp = int(input(f"Number of people who took {food} item "))
        lp = int(input(f"Number of people who liked {food} item"))
        tf = float(tp/a)
        lf = float(lp/tp)
        my = {'Food Item' : food}
        newq = {"$set" : {"%people(Ate)" : tf , "%people(Like it)" : lf , "Total people" : tp , "Number of people liking" : lp , "Attendence" : a}}
        df1.update_one(my,newq)
    i = int(input("->Do u want to delete any other collection? - 1 ->Do u want to update/add any collection? - 2  Press any other key to exit"))
    if (i == 1) :
        del_item()
    elif (i==2) :
        add_upd_item()


def del_item():
    c = input("Enter Food Item name")
    myq = {"Food Item" : c}
    df1.delete_one(myq)
    print(f"After deleting data with Food item {c} this dataset")
    show()
    i = int(input("->Do u want to delete any other collection? - 1 ->Do u want to update/add any collection? - 2  Press any other key to exit"))
    if (i == 1) :
          del_item()
    elif (i==2) :
          add_upd_item()


def main():
   create_collection()
   show()
   s = input("Enter food item")
   find_item(s)
   max_taken()
   min_taken()
   max_liked()
   min_liked()
   i = int(input("-> Do u want to add/update a food item? - 1 -> Do u want to delete a food item? - 2  Press any other key to exit"))
   if ( i == 1) :
         add_upd_item()
   elif (i==2) :
         del_item()


if __name__ == '__main__':
   main()
