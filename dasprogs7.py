print('=== Kalkulator Sederhana ===')
print('menu')
print('1. Hitung luas Segitiga ')
print('2. Hitung Luas Persegi Panjang')
print('3. Tentukan Bilangan Ganjil dan Genap')
print('4. quit')
while True: 
    m = input('Input 1/2/3/4:   ')

 #1. Hitung Luas Segitiga
    if m=='1':
        a = float(input('Masukan Alas: '))
        t = float(input('Masukan Tinggi: '))
        luas = 0.5*a*t
        print("Luas Segitiga adalah = %0.2f" % luas)

 #2. Hitung Luas Persegi Panjang   
    elif m=='2':
          p = float(input('Masukan Panjang: '))
          l = float(input('Masukan Lebar:  '))
          luas = p * l
          print("Luas Persegi Panjang:  ",luas)

 #3. Tentukan angka ganjil dan genap 
    elif m=='3':
          v = int(input('Masukan Variabel:    '))
          if v %2 == 0:
              print('{0} Bilangan Genap'. format(v))
          else:
              print('{0} Bilangan Ganjil'. format(v)) 
    elif m=='4':
          print('Thank you!')
          break
    else:
        print('invalid data')