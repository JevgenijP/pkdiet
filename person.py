import time
import uuid
import pickle
import random
from pathlib import Path


class Person:
    def __init__(self, user):
        self.id = uuid.uuid4()
        self.username = user
        self.p_to_datastore = './' + user
        self.datastore()
        self.read_inst()


    #Data structure to store user data
    datastruct = {'user_data': {},
                   'pain_level': {},
                   'ketone_level': {},
                   'glucose_level': {}
                   }


    #Methods to work with datastore
    def datastore(self):
        path = Path(self.p_to_datastore)
        if not Path(self.p_to_datastore).is_dir():
            #Initialize datastore for user.
            #Create dir and serializeempty user data structure into it
            path.mkdir()
            self.write_inst()

    def write_inst(self):
        f = open(self.p_to_datastore + '/' + str(self.username) + 'current', 'wb')
        pickle.dump(self.datastruct, f)
        f.close()


    def read_inst(self):
        f = open(self.p_to_datastore + '/' + str(self.username) + 'current', 'rb')
        self.datastruct = pickle.load(f)
        f.close()


    def delete_inst(self, fname):
        pass


if __name__ == "__main__":

    #Function which generate some data to fill instances of Person
    # to make tests
    def gen_data(N):
        pain, ketones, glucose = {}
        for i in range(0, N, 1):
            pain.update({int(time.time()): random.randint(0,10) })
            ketones.update({int(time.time()): round(random.uniform(0.0, 6.0), 1) })
            glucose.update({int(time.time()): round(random.uniform(3.0, 6.0), 1) })
            time.sleep(random.randint(1, 5))
        return pain, ketones, glucose





