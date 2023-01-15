from collections import deque
import numpy
import random
def tekeracisigenerator():
    global teker_acisi
    global stack
    stack = []
    for i in range(255):
        teker_acisi = random.randint(0, 255)
        stack.append(teker_acisi)
    print(stack)
    return teker_acisi,stack
lidar = []
def mesafegenerator():
    global lidar_mesafe
    global lidar
    lidar_mesafe = random.randint(40,100)
    lidar.append(lidar_mesafe)
    print(lidar)
    return lidar_mesafe
def geriteker(): 
    global geri
    geri = stack[::-1]
    print(geri)
    return geri
tekeracisigenerator()
mesafegenerator()
geriteker()
for i in range(250):
    gta = geri.pop(0)
    print(gta)
if lidar[0]<50:
    print("Yavaş la çarptın.Şimdi geri çıkman lazım")
    print("Kalan mesafe: ",lidar[0])
    ta = gta
    v = 110 #geri çıkma hızı
    print("Geri çıkılıyor, hızınız 110")
    print("Geri teker açınız: ",ta)
else:
    print("koda devam et")







       






# for i in gta:
#     print(gta(i))
    





# ta = [130,135,140,245] #teker açısı
# #45 cm kalınca çarpıyor
# lnu = [100,70,60,50,45] #lidarin nesneye uzaklığı(cm)
# v = 140 #çarpma hızı-önemsiz?
# def Ters(ta): 
#     ta.reverse() 
#     return ta 
# gta = ta
# print("Geri teker açısı:")
# print(Ters(gta))
# for i in lnu:
#     x = i
#     if x<50:
#         ta=gta
#         print(ta)
#         print("yavaş çarptın")
#     else:
#         print("aferin böyle devam")

