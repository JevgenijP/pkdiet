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


if __name__ == "__main__":

    #Function which generate some data to fill instances of Person
    #
    def gen_data(N):
        pain, ketones, glukose = {}
        for i in range(0, N, 1):
            pain.update({int(time.time()): random.randint(0,10) })
            ketones.update({int(time.time()): round(random.uniform(0.0, 6.0), 1) })
            glukose.update({int(time.time()): round(random.uniform(3.0, 6.0), 1) })
            time.sleep(random.randint(1, 5))
        return pain, ketones, glukose

