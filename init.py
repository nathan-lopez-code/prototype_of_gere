import time
from datetime import date, timedelta


######################################################################
# bulding a simple structure to converse the time in commonly using
# take date in format day/moth/year
# calcul this x + 14 = o ; list = [x+4, .... ,y-6 , y+3 + 10] ;
#

#####################################################################
my_time = time.gmtime()
year = my_time.tm_year

# saving the laster day of regle
def wath_is_the_last_time():
    """take the day, month and year of the last cycle"""
    day = int(input('day : '))
    moth = int(input('month : '))
    yr = int(input(f'year default year is {year} :'))
    my_date = date(yr, moth, day)
    return my_date


def remember_last():
    """this function take the last month before the last cicle"""
    my_date = None
    print("vous souvenez vous encore de vos avant derniere regle ")
    choise = input(" soit o pour oui soit n pour non :")
    print(type(choise))
    while choise != "o" and choise != "n":
       choise = input("erreur | soit o pour oui soit n pour non :")

    if choise == 'o':
        my_date = wath_is_the_last_time()
        return my_date

    return my_date


def nomberOfday(date1, date2=None):
    day_b = None
    if date2 != None:
        day_b = date1 - date2
        day_b = day_b.days
    return day_b


def testing(day_b):
    on_error = False
    error_dico = {}
    if day_b < 0:
        on_error = True
        error_dico["moth"] = 'the second month is greater than the first'
    elif day_b == 0:
        on_error = True
        error_dico['day'] = 'the day have the coincide'

    return on_error, error_dico


def ovi_date(date1, date2=None):
    """ in this function we can calculate the day of ovilation"""
    if date2 != None:
        ovilation_date = date1 + timedelta(days=(nomberOfday(date1, date2) / 2))
    else:
        ovilation_date = date1 + timedelta(days=14)

    return ovilation_date


def feconded_period(date_ov):
    """ in this function we can calculate the fecondation period"""
    on_date = None
    ip = date_ov - timedelta(days=8)         # date - 8 jour = date initiale sur lequel on va iterer
    ii = date_ov + timedelta(days=2)
    days_init = ip.day
    days_fin = ii.day
    if days_init > days_fin:
        i = days_init - days_fin
    else:
        i = days_fin - days_init

    fecond = []
    for x in range(1, i):
        on_date = ip + timedelta(days=x)
        fecond.append(on_date)
    return fecond


def free_period(date1, date_ov):
    """this function return the free periode that we can do the party"""
    free, on_date = [], None
    init_date, init_date2 = date1 + timedelta(days=3), date_ov + timedelta(days=2)
    end_date = date_ov - timedelta(days=7)
    i = init_date.day
    ii = end_date.day
    if i > ii:
        o = i - ii
    else:
        o = ii - i
    for x in range(0, o+1):
        on_date = init_date + timedelta(days=x)
        if end_date.day == on_date.day and end_date.month == on_date.month and end_date.year == on_date.year:
            break
        free.append(on_date)

    return free, init_date2


if __name__ == "__main__":

    date_ov = None

    print("entrez le jour et mois de vos dernier regle :\n")
    first_date = wath_is_the_last_time()
    second_date = remember_last()
    day_betwen = nomberOfday(first_date, second_date)
    on_error, error_list = None, None


    print(day_betwen)
    if day_betwen != None:
        on_error, error_list = testing(day_betwen)

    if on_error:
        print(f"we have this error : {error_list}")
    else:
        # excute the commande
        date_ov = ovi_date(first_date, second_date)
        print(date_ov)
        print("***********************************")
        print(feconded_period(date_ov))
        print("***********************************")
        print(free_period(first_date, date_ov))

