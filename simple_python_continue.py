#!/usr/bin/python
# -*- coding: utf-8 -*-
# @wufeng 2018-04-27

while True:
    text = input("plese enter someting :")
    if text == 'quit':
        break
    if len(text) < 3:
        print("it's too short.")
        continue
    print("the length of the words are : " ,len(text))
