import random
def klm():
    print("kelime seciniz")
    print("elma,agaç,kiraz,ali,metin")
klm()
can=3
dic=["elma","agaç","kiraz","ali","metin"]
dogruklm=[]
while can > 0:
    tahmin=input("kelime giriniz")
    dogruklm.append(random.choice(dic))
    if tahmin==dogruklm:
        print("dogru tahmin")
        pass
    else:
        can=can-1
        print("yanlis cevap")
print("hakkiniz bitti")