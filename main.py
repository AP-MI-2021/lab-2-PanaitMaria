import math

def get_leap_years(start,end):
    list=[]
    for year in range(start,end+1):
        if not year % 4 :
            list.append(year)
    return list

def test_get_leap_years():
    years=get_leap_years(2000,2020)
    assert(2004 in years)

def get_perfect_squares(start, end):
    # returns a list of perfect squares between given range
    # start, end: int
    # return: list
    return list(filter(lambda x: int(math.sqrt(x)) == math.sqrt(x), range(start, end + 1)))


def test_get_perfect_squares():
    # test function for get perfect squares
    assert(get_perfect_squares(1, 10) == [1, 4, 9])
    assert(get_perfect_squares(10, 100) == [i * i for i in range(4, 11)])

def get_temp(temp, frrom, to):
    temp_celsius = temp
    if frrom == 'K':
        temp_celsius = temp_celsius - 273.15
    if frrom == 'F':
        temp_celsius = (temp_celsius - 32) / 1.8
    if to == 'K':
        return temp_celsius + 273.15
    if to == 'F':
        return (temp_celsius * 1.8 + 32)
    return temp_celsius

def test_get_temp():
    assert(get_temp(-40, 'F', 'C') == -40)
    assert(get_temp(-40, 'C', 'F') == -40)
    assert(get_temp(0, 'F', 'C') + 17.78 < 0.01)
    assert(abs(get_temp(-17.78, 'C', 'F')) < 0.01)
    assert(abs(get_temp(98.6, 'F', 'C') - 37) < 0.01)
    assert(abs(get_temp(100, 'C', 'F') - 212) < 0.01)
    assert (abs(get_temp(0, 'K', 'C') + 273.15) < 0.01)
    assert (abs(get_temp(-273.15, 'C', 'K')) < 0.01)
    assert (abs(get_temp(160 , 'K', 'C') + 113.15) < 0.01)




def main():
    test_get_leap_years()
    test_get_temp()

    l = []
    while True:
        print("11. Afișează toți anii bisecți între doi ani dați")
        print("12. Afișează toate pătratele perfecte dintr-un interval închis")
        print("13.Transformă o temperatură dată într-o scară dată (K, F sau C) într-o altă scară dată. ")
        print("x. Iesire")

        optiune = input("Dati optiunea: ")

        if optiune == "11":
            print(get_leap_years(2000,2020))
        elif optiune == "12":
            start = int(input('start: '))
            end = int(input('end: '))
            print(f'list of squares in range: {get_perfect_squares(start, end)}')
        elif optiune == "13":
            temp= int(input('Dati temperatura'))
            frrom = int(input('Din  '))
            to = int(input('In '))
            print(get_temp(temp, frrom, to))
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")

main()