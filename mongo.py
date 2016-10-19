# -*- coding: utf-8 -*-
"""
Created on 2016-08-20
@author: wangwei
"""
from tgrocery import Grocery
import sys
import os

import datetime
from pymongo import MongoClient
from pymongo import MongoReplicaSetClient
from pymongo import DESCENDING
from message import Message


def findcollections():
	client1 =  MongoReplicaSetClient("mongodb-3:27017",connect=False)
    client1.hydra.authenticate('work', 'ziyNrh9LnQfCGglDylFX')
    db =  self.client1.hydra
    print "the result is :",db.collection_name.find(user_short_message)


if __name__=='__main__':

 	findcollections()