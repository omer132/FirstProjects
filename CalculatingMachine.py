def prt():
    print("işlem türünü seciniz")
    print("toplama/çikartma/bölme/çarpma")
prt()
islem=(input("islemi giriniz"))
sayi1=float(input("sayi1 giriniz"))
sayi2=float(input("sayi2 giriniz"))
if islem == "toplama" or "cikartma" or "bölme" or "çarpma":
    if islem == "toplama":
        print("islem sonucu:    ",sayi1+sayi2)
    elif islem == "cikartma":
        print("islem sonucu:    ",sayi1-sayi2)
    elif islem == "bölme":
        print("islem sonucu:    ",sayi1/sayi2)
    else:
        print("islem sonucu:    ",sayi1*sayi2)
else:
    print("dogru islem seciniz")    