import os
import random
import string
data = dict()
while True:
    os.system("clear")
    print(f" {'DATA NOVEL':_^35}")
    keyFinal = "".join(random.choice(string.ascii_uppercase) for i in range (3))
    drakor1 = input("Novel pertama\t:")
    drakor2 = input("Novel favorit\t:")
    drakor3 = input("Novel paling bagus\t:")
    data [ keyFinal ] = { keyFinal : { 'novel1key' : novel1, 'novel2key' : novel2, 'novel3key' : novel3}}
    print(data)

    opsi = input("input data LAGI (y/t) :").lower()
    if opsi == 't':
        break

print("-"*40)
print(f"key\t Mariposa\t Zenolya\t Lavender\t")

