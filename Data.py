import os 
import math

DataW = open('Data.txt','a',encoding='utf-8')
DataW.write('Hello World\n')
DataW.close()

DataR = open('Data.txt','r',encoding='utf-8')
s = DataR.read()
print(s)
DataR.close()