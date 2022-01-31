#! /usr/bin/python

import sys
import os

os.system('git clone https://github.com/CDPS-ETSIT/practica_creativa2.git')

os.system('pip3 install -r practica_creativa2/bookinfo/src/productpage/requirements.txt')

GROUP_NUMBER = os.environ['GROUP_NUMBER']

os.system('cp practica_creativa2/bookinfo/src/productpage/templates/productpage.html practica_creativa2/bookinfo/src/productpage/templates/pp2.html')

original = open('practica_creativa2/bookinfo/src/productpage/templates/productpage.html', 'r')
copia = open('practica_creativa2/bookinfo/src/productpage/templates/pp2.html', 'w')

for line in original:
    if("BookInfo Sample" in line) :
        copia.write(line.replace("BookInfo Sample", "BookInfo Sample " + GROUP_NUMBER))
    else:
        copia.write(line)
copia.close()
original.close()

os.system('rm practica_creativa2/bookinfo/src/productpage/templates/productpage.html')
os.system('mv practica_creativa2/bookinfo/src/productpage/templates/pp2.html practica_creativa2/bookinfo/src/productpage/templates/productpage.html')

os.system('python3 practica_creativa2/bookinfo/src/productpage/productpage_monolith.py 9080')
