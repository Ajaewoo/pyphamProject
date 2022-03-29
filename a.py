from random import randint

import matplotlib.pyplot as plt
import pygal

class Dice():
    def __init__(self, num=6):
        self.num=num

    def roll(self):
        return randint(1, self.num)




































