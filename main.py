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

def get_temp(temp, from, to):
    

  

def main():
    test_get_leap_years()
    l = []
    while True:
        print("11. Afișează toți anii bisecți între doi ani dați")
        print("12. Afișează toate pătratele perfecte dintr-un interval închis")
        print("x. Iesire")

        optiune = input("Dati optiunea: ")

        if optiune == "11":
            print(get_leap_years(2000,2020))
        elif optiune == "12":
            start = int(input('start: '))
            end = int(input('end: '))
            print(f'list of squares in range: {get_perfect_squares(start, end)}')
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")

main()