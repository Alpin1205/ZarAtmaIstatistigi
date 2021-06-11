import random

binlik = 0
ortbinlik = 0
üçelli = 0
üçorta = 0
değil = 0
uçukb = 0
uçukk = 0

for i in range(0,1000):
    for b in range(0,10):
        for p in range(0, 100):
            binlik += random.randint(1, 6)
        x = binlik / 100
        binlik = 0
        print(str(i) + str(b) +". defa ortalaması " +str(x))
        ortbinlik += x
        if x <= 3.59 and x >= 3.50:
            üçelli += 1
        if x <= 3.55 and x >= 3.46:
            üçorta += 1
        if x <= 3:
            uçukk += 1
        if x >= 4:
            uçukb += 1
        else:
            değil += 1

print("""
Ortalama Sonucu: 
    3.59 ile 3.50 arasındakiler: """+ str(üçelli) +"""
    3.55 ile 3.46 arasındakiler: """+ str(üçorta) +"""
    3 küsür olup şartı karşılamayanlar: """+ str(değil) +"""
    3'ten küçük olanlar: """+ str(uçukk) +"""
    4'ten büyük olanlar: """+ str(uçukb) +"""
    """)