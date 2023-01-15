
ta = [130,135,140,245] #teker açısı
#45 cm kalınca çarpıyor
lnu = [100,70,60,50,45] #lidarin nesneye uzaklığı(cm)
v = 140 #çarpma hızı-önemsiz?
x = lnu[::-1]
for i in x:
    if x[i]<50:
        gta = ta.pop
        print(gta)
