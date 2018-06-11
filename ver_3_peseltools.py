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

    months_31 = [1, 3, 5, 7, 8, 10, 12]
    months_30 = [4, 6, 9, 11]
    weights = [9, 7, 3, 1, 9, 7, 3, 1, 9, 7]
    pesel_numbers = []
    multiplication_results = []

    try:

        for number in pesel:
            pesel_numbers.append(int(number))

        for id, num in enumerate(pesel_numbers[:10]):
            result = num * weights[id]
            multiplication_results.append(result)

        checking_sum = 0
        for num in multiplication_results:
            checking_sum += num


        if len(pesel) == 11 and checking_sum % 10 == int(pesel[10]):
            a = int(pesel[2:4]) - 80  # for birthdates between 1800 and 1899
            b = int(pesel[2:4])  # for birthdates between 1900 and 1999
            c = int(pesel[2:4]) - 20  # for birthdates between 2000 and 2099

            if int(pesel[2:4]) in range(81, 93):
                if a in months_31 and int(pesel[4:6]) <= 31:
                    return True
                elif a in months_30 and int(pesel[4:6]) <= 30:
                    return True
            elif int(pesel[2:4]) in range(1, 13):
                if b in months_31 and int(pesel[4:6]) <= 31:
                    return True
                elif b in months_30 and int(pesel[4:6]) <= 30:
                    return True
            elif int(pesel[2:4]) in range(21, 33):
                if c in months_31 and int(pesel[4:6]) <= 31:
                    return True
                elif c in months_30 and int(pesel[4:6]) <= 30:
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
        if int(pesel[2:4]) in range(81, 93):
            a = (int(pesel[2:4]) - 80)  # for birthdates between 1800 and 1899
            personal_data['birth_date'] = (pesel[4:6] + '.' + str(a) + '.' + '18' + pesel[:2])
        elif int(pesel[2:4]) in range(1, 13):
            b = int(pesel[2:4]) # for birthdates between 1900 and 1999
            personal_data['birth_date'] = (pesel[4:6] + '.' + str(b) + '.' + '19' + pesel[:2])
        elif int(pesel[2:4]) in range(21, 33):
            c = (int(pesel[2:4]) - 20)  # for birthdates between 2000 and 2099
            personal_data['birth_date'] = (pesel[4:6] + '.' + str(c) + '.' + '20' + pesel[:2])

        if int(pesel[9]) % 2 == 0:
            personal_data['sex'] = 'female'
        else:
            personal_data['sex'] = 'male'

        print("Your data has been saved in the database:")
        print(personal_data)
