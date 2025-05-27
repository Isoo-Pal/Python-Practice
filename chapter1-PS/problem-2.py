# write a program to print all the contents in a directory using os module function

import os

#below line takes the directory where you want to list all the content
path = '/Users'

#list all the content in contents variable
contents = os.listdir(path)

#iterating over every content 
for content in contents:
    print(content)