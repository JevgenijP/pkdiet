import time
import uuid
import pickle
import random
from pathlib import Path


class Person:
    def __init__(self, user):
        self.exist = False
        self.id = uuid.uuid4()
        self.username = user
        self.path_to_data = self.create_storage(user)
        if not self.exist:
            pain_level = {}
            ketone_level = {}
            glucose_level = {}

    #Methods to write/read data
    def create_storage(self, user):
        path = Path('./' + user)
        # Need to rewrite total bulshit!!!!
        if path.is_dir():
            print("Already exists, reading pickled object")
            self.path_to_data = path
            self.read_inst(str(user + 'current'))
            self.exist = True
            return path

        else:
            path.mkdir()
            return path

    def write_inst(self):
        f = open(self.path_to_data.name + '/' + str(self.username) + 'current', 'wb')
        pickle.dump(self, f)
        f.close()
    #Need to rewrite total bulshit!!!!
    def read_inst(self, fname):
        f = open(self.path_to_data.name + '/' + str(fname), 'rb')
        someperson = pickle.load(f)
        f.close()
        return someperson

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

    p1 = Person("ivan")
    p2 = Person('user')

