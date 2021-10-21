def gen(n):
    abc = ""
    for i in range(n):
        abc = abc + (chr(i + 97))
    print(abc)


def letra_o(n):
    contain = ""
    for i in range(n):
        contain += "*"
    print(contain)
    contain_middle = "*"
    for i in range(n - 2):
        contain_middle += " "
    contain_middle += "*"
    for i in range(n - 2):
        print(contain_middle)
    print(contain)


def letra_i(n):
    contain = ""
    for i in range(n):
        contain += "*"
    print(contain)
    contain_middle = ""
    for i in range(int(n / 2)):
        contain_middle += " "
    contain_middle += "*"
    for i in range(n - 2):
        print(contain_middle)
    print(contain)


def letra_x(n):
    for i in range(n):
        if i < int(n/2):
            contain = " "*i
            contain_middle = " "*(n-i*2-2)
            print(contain + "*" + contain_middle + "*" + contain)
        elif i > int(n / 2):
            contain = " " * (n-i-1)
            contain_middle = " " *(i*2-n)
            print(contain + "*" + contain_middle + "*" + contain)
        else:
            contain = " "* int(n/2)
            print(contain+"*")

gen(4)

gen(10)

letra_o(5)

letra_i(5)

letra_x(5)