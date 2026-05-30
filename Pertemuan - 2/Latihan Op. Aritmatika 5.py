print("Menghitung jarak antara dua titik pada permukaan bumi")

print()

import math

longitudeTitikA = float(input("Masukkan LongitudeTitikA: "))
latitudeTitikA = float(input("Masukkan latitudeTitikA: "))
longitudeTitikB = float(input("Masukkan longitudeTitikB: "))
latitudeTitikB = float(input("Masukkan latitudeTitikB: "))

#Jari-jari bumi (km)
R = 6371

#Konversi ke radian
lon1 = math.radians(longitudeTitikA)
lat1 = math.radians(latitudeTitikA)
lon2 = math.radians(longitudeTitikB)
lat2 = math.radians(latitudeTitikB)

#Selisih Lintang dan Bujur
dlat = lat2 - lat1
dlon = lon2 - lon1

#Rumus HaverSine
a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

#jarak
jarak = R * c

print("Jarak antara titik A dan titik B " + str(jarak) + "km")