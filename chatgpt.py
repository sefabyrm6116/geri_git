from collections import deque
import numpy
import random
def whell_angle_sensor():
    global wheel_angle
    global stack
    stack = []
    for i in range(255):
        wheel_angle = random.randint(0, 255)
        stack.append(wheel_angle)
    print(stack)
    return wheel_angle,stack
lidar = []
def lidar_distance():
    global lidar_distance
    global lidar
    lidar_distance = random.randint(40,100)
    lidar.append(lidar_distance)
    print(lidar)
    return lidar_distance
def back_wheel_angel(): 
    global back
    back = stack[::-1]
    print(back)
    return back
whell_angle_sensor()
lidar_distance()
back_wheel_angel()



# çarpma için eşik mesafesi
threshold_distance = 50 

# tekerlek açısı verilerini al
print("Wheel angle: ", wheel_angle)    
# lidar verilerini al
lidar_distance 
print("LIDAR distance: ", lidar_distance)    
# çarpışmayı kontrol et
if lidar_distance < threshold_distance:
    # arabayı durdur
    v = 128 # hız sıfır
    print("Çarptın!Aracı durdur.")
    # geri çekilme işlemi başlat
    v = 61 # geri hız
    retreat_distance = 2 # metrede
    print("Geri çıkıldı")
else:
    # sürmeye devam et
    print("161 hızla yola devam ediliyor")
    v = 161