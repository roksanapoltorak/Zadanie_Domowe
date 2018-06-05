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
        month_30 = [4, 6, 9, 11]

        if len(pesel) == 11 and checking_sum % 10 == int(pesel[10]):
            if int(pesel[2:4]) <=12 and int(pesel[2:4]) in months_31 and int(pesel[4:6]) <= 31:
                if birth == int(pesel[0:6]) and sex.lower() == 'f' and int(pesel[9]) in ("02468"):
                    return True
                elif birth == int(pesel[0:6]) and sex.lower() == 'm' and pint(pesel[9]) in ("13579"):
                    return True
            elif int(pesel[2:4]) <= 12 and int(pesel[2:4]) in month_30 and int(pesel[4:6]) <= 30:
                return True

        else:
            return False

    except ValueError:
        print("Something went wrong. Please try again.")

    except IndexError:
        print("You entered not enough or too many digits...")

def extract_personal_data(pesel):
    """
    Returns dictionary with data about user's date of birth and sex

    Args:
        PESEL, user's date of birth and sex to check if these information are compatible
    Returns:
        Dictionary with data about user's date of birth and sex
    """

    personal_data = {}

    if validate(pesel):
        try:
            personal_data['birth_date'] = pesel[:6]

            if pesel[9] in ("02468"):
                personal_data['sex'] = 'female'
            elif pesel[9] in ("13579"):
                personal_data['sex'] = 'male'
            else:
                print("Your birth and/or your sex don't fit with your pesel.")

            print("Your data has been saved in the database.")
            print(personal_data)

        except ValueError:
            print("Something went wrong. Please try again.")

        except IndexError:
            print("You entered not enough or too many digits...")

    else:
        print("You entered wrong data.")

