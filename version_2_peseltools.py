""""

Module for PESEL validation

"""

def validate(pesel):
    """
    Returns validation of PESEL

    Args:
        PESEL to validate
    Returns:
        Validation of PESEL
    """

    try:
        checking_sum = 9 * int(pesel[0]) + 7 * int(pesel[1]) + 3 * int(pesel[2]) + 1 * int(pesel[3]) + 9 * int(
            pesel[4]) + 7 * int(pesel[5]) + 3 * int(pesel[6]) + 1 * int(pesel[7]) + 9 * int(pesel[8]) + 7 * int(
            pesel[9])
        months_31 = [1, 3, 5, 7, 8, 10, 12]
        months_30 = [4, 6, 9, 11]

        if len(pesel) == 11 and checking_sum % 10 == int(pesel[10]):
            a = int(pesel[2:4]) - 80  # for birthdates between 1800 and 1899
            b = int(pesel[2:4])  # for birthdates between 1900 and 1999
            c = int(pesel[2:4]) - 20  # for birthdates between 2000 and 2099

            if int(pesel[2]) == 8 or int(pesel[2]) == 9:
                if a <= 12 and a in months_31 and int(pesel[4:6]) <= 31:
                    return True
                elif a <= 12 and a in months_30 and int(pesel[4:6]) <= 30:
                    return True
            elif int(pesel[2]) == 0 or int(pesel[2]) == 1:
                if b <= 12 and b in months_31 and int(pesel[4:6]) <= 31:
                    return True
                elif b <= 12 and b in months_30 and int(pesel[4:6]) <= 30:
                    return True
            elif int(pesel[2]) == 2 or int(pesel[2]) == 3:
                if c <= 12 and c in months_31 and int(pesel[4:6]) <= 31:
                    return True
                elif c <= 12 and c in months_30 and int(pesel[4:6]) <= 30:
                    return True

    except ValueError as err_1:
        print("Something went wrong. The error is: ", err_1)

    except IndexError as err_2:
        print("You entered not enough or too many digits. The error is: ", err_2)

def extract_personal_data(pesel):
    """
    Returns dictionary with data about user's date of birth and sex

    Args:
        PESEL
    Returns:
        Dictionary with data about user's date of birth and sex
    """

    personal_data = {}

    if validate(pesel):
        if int(pesel[2]) == 8 or int(pesel[2]) == 9:
            a = (int(pesel[2:4]) - 80)  # for birthdates between 1800 and 1899
            personal_data['birth_date'] = (pesel[4:6] + '.' + str(a) + '.' + '18' + pesel[:2])
        elif int(pesel[2]) == 0 or int(pesel[2]) == 1:
            b = int(pesel[2:4]) # for birthdates between 1900 and 1999
            personal_data['birth_date'] = (pesel[4:6] + '.' + str(b) + '.' + '19' + pesel[:2])
        elif int(pesel[2]) == 2 or int(pesel[2])== 3:
            c = (int(pesel[2:4]) - 20)  # for birthdates between 2000 and 2099
            personal_data['birth_date'] = (pesel[4:6] + '.' + str(c) + '.' + '20' + pesel[:2])

        if int(pesel[9]) % 2 == 0:
            personal_data['sex'] = 'female'
        elif int(pesel[9]) % 2 != 0:
            personal_data['sex'] = 'male'

        print("Your data has been saved in the database:")
        print(personal_data)
