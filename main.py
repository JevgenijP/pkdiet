import time
import uuid
import pickle
import random


class Person:
    def __init__(self):
        self.id = uuid.uuid4()

    pain_level = {}
    ketone_level = {}
    glucose_level = {}




#Functions which generate test data to fill instances of Person
#

def gen_pain(N):
    res = {}
    for i in range(0,N,1):
        a = {int(time.time()): random.randint(0,10) }
        res.update(a)
        time.sleep(random.randint(1,5))
    return res

def gen_ketone(N):
    res = {}
    for i in range(0,N,1):
        a = {int(time.time()): round(random.uniform(0.0, 6.0), 1) }
        res.update(a)
        time.sleep(random.randint(1,5))
    return res

def gen_glucose(N):
    res = {}
    for i in range(0,N,1):
        a = {int(time.time()): round(random.uniform(3.0, 6.0), 1) }
        res.update(a)
        time.sleep(random.randint(1,5))
    return res

