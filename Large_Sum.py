dosya = 'numbers.txt'
with open(dosya, "r") as ins:
    sayi = []
    for line in ins:
        sayi.append(line)

yeni_sayi = []
for i in sayi:
    yeni_sayi.append(int(i))


array_toplam = sum(yeni_sayi)
print (str(array_toplam)[:10])