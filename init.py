import time
from datetime import date, timedelta


######################################################################
# bulding a simple structure to converse the time in commonly using
# take date in format day/moth/year
# calcul this x + 14 = o ; list = [x+4, .... ,y-6 , y+3 + 10] ;
#

#####################################################################


# for day
my_time = time.gmtime()
year = my_time.tm_year

######################################
# janvier : 31
# fevrier : 28 or 29
# mars ; 30
# avril :
################################
# saving the laster day of regle
def wath_is_the_last_time():
    day = 0
    moth = 0
    day = int(input('day : '))
    moth = int(input('month : '))
    yr = int(input(f'year default year is {year} :'))
    my_date = date(yr, moth, day)


    return my_date


def remember_last():
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
        day_b = date2 - date1
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

def feconded_period(date1, date_ov):
    """ in this function we can calculate the fecondation period"""
    i = date_ov - date1
    on_date = None
    ii = 0
    fecond = []
    for x in range(i, date_ov.day):
        if on_date != None:
            on_date = i + timedelta(days=ii)
            fecond.append(on_date)
            ii += 1

    return fecond



if __name__ == "__main__":

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
        print(feconded_period(date_ov))

