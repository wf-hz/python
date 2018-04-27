#!/usr/bin/python
# -*- coding: utf-8 -*-
# @wufeng 2018-04-27

import random

number = random.randint(0,99)
guess = int(input("please input a number: "))
if guess == number:
    print("Well done. You're right.")
    print("and so ...?")
elif guess < number:
    print("No, it is a little higher than that.")
else:
    print("No, it is a little lower than that.")

print('End')


