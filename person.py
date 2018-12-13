import time
import uuid
import pickle
import random
import shutil
from pathlib import Path


class Person:
    def __init__(self, user):
        self.id = uuid.uuid4()
        self.username = user
        self.p_to_datastore = './' + user
        self.datastore()
        self.read_ds()


    #Data structure to store user data
    datastructure = {'data_scheme': {'user_info': ['username'],
                                     'records':  [['timestamp', 'ketone_level', 'glucose_level', 'pain_level']]},
                     'user_info': [],
                     'records': []
                    }


    #Methods to work with datastore
    def datastore(self):
        if not Path(self.p_to_datastore).is_dir():
            #Initialize datastore for user.
            #Create dir and serialize empty user data structure inside this dir
            Path(self.p_to_datastore).mkdir()
            self.write_ds()

    def write_ds(self):
        f = open(self.p_to_datastore + '/' + str(self.username) + 'current', 'wb')
        pickle.dump(self.datastructure, f)
        f.close()


    def read_ds(self):
        f = open(self.p_to_datastore + '/' + str(self.username) + 'current', 'rb')
        self.datastructure = pickle.load(f)
        f.close()


    def delete_ds(self):
        #delete data store
        shutil.rmtree(self.p_to_datastore)


    #Methods to work with user data  in datastruct dictionary
    def addrecord(self, key, value):
        if key in self.datastructure:
            self.datastructure[key].update(value)
        else:
            print("Wrong key was given. Acceptable keys: ", list(self.datastructure.keys()) )






if __name__ == "__main__":

    #Function which generate some data to fill instances of Person
    # to make tests
    def gen_data(n, u='ivan'):
        d = {'user_info': [u],
             'records': []
            }
        #d= { 'user_data': { 'user': u}, 'pain_level': {}, 'ketones_level': {}, 'glucose_level': {}}
        for i in range(0, n, 1):
            d['records'].append([int(time.time()), round(random.uniform(3.0, 6.0), 1),  round(random.uniform(0.0, 6.0), 1), random.randint(0, 10) ])
            time.sleep(random.randint(1, 5))
        return d
    #print("Running")
    #p1 = Person('test')
    #p1.datastructure





