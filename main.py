def citirelista() -> list[int]:
    lista = []
    n = int(input("Introduceti nr de elem: "))
    for i in range(n):
        elem=int(input("l["+str(i)+"]= "))
        lista.append(elem)
    return lista
def afisare_nr_negative(lis):
    for x in lis:
        if x < 0:
            print(x)
def celmaimicnr(lis):
    n = int(input("Introduceti ultima cifra:"))
    min=99999999
    for x in lis:
        if x % 10 == n and x < min:
            min = x
    if min == 99999999:
        print("NU Exista")
    else:
        return min
def is_prime(x):
    if x < 2:
        return False
    else:
        for i in range(2,x//2+1,1):
            if x % i == 0:
                return False
        return True
def is_superprime(x):
    ok = 1
    while x != 0 and ok == 1:
        if is_prime(x):
            x = x // 10
        else:
            ok = 0
    if ok == 0:
        return False
    else:
        return True
def cmmdc(m,n):
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return m
def main():
    lst=[]
    while True:
        print("1.Citire lista")
        print("2.Afisarea numerelor negative din lista")
        print("3.Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură")
        print("4.Afișarea tuturor numerelor din listă care sunt superprime")
        print("5.Inlocuirea numerelor din lista.(Pozitive-cmmdc,negative-invers)")
        print("6.Afisare lista")
        print("7.Iesire")
        optiune = int(input("Introduceti optiunea: "))
        if optiune == 1:
            lst=citirelista()
        if optiune == 2:
            afisare_nr_negative(lst)
        if optiune == 3:
            celmaimicnr(lst)
        if optiune == 4:
            for x in lst:
                if x>0 and is_superprime(x):
                    print(x)
        if optiune == 5:
            lst2=[]
            for x in lst:
                if x > 0:
                    y = x + 1
                    while lst[y]>0:
                        y += 1
                    (cmmdc(lst[x],lst[y]))
                else:
                    inv = 0
                    w

        if optiune == 6:
            print(lst)
        if optiune == 7:
            break

main()