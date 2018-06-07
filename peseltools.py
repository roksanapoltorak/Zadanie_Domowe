""""

Module for PESEL validation

"""


def validate(pesel, birth, sex):
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
        female = [0, 2, 4, 6, 8]
        male = [1, 3, 5, 7, 9]

        if len(pesel) == 11 and checking_sum % 10 == int(pesel[10]):
            if (sex.lower() == 'f' and int(pesel[9]) in female) or (sex.lower() == 'm' and int(pesel[9]) in male):
                if 1800 <= int(birth[:4]) <= 1899:
                    if (int(pesel[2:4])-80) == int(birth[4:6]) and int(birth[4:6]) in months_31 and int(pesel[4:6]) <= 31:
                        return True
                    elif (int(pesel[2:4])-80) == int(birth[4:6]) and int(birth[4:6]) in months_30 and int(pesel[4:6]) <= 30:
                        return True
                elif 1900 <= int(birth[:4]) <= 1999:
                    if int(pesel[2:4]) <=12 and int(pesel[2:4]) in months_31 and int(pesel[4:6]) <= 31:
                        return True
                    elif int(pesel[2:4]) <= 12 and int(pesel[2:4]) in months_30 and int(pesel[4:6]) <= 30:
                        return True
                elif 2000 <= int(birth[:4]) <= 2018:
                    if (int(pesel[2:4])-20) == int(birth[4:6]) and int(birth[4:6]) in months_31 and int(pesel[4:6]) <= 31:
                        return True
                    elif (int(pesel[2:4])-20) == int(birth[4:6]) and int(birth[4:6]) in months_30 and int(pesel[4:6]) <= 30:
                        return True
        else:
            return False

    except ValueError:
        print("Something went wrong. Please try again.")

    except IndexError:
        print("You entered not enough or too many digits...")

def extract_personal_data(pesel, birth, sex):
    """
    Returns dictionary with data about user's date of birth and sex

    Args:
        PESEL, user's date of birth and sex to check if these information are compatible
    Returns:
        Dictionary with data about user's date of birth and sex
    """

    personal_data = {}
    female = [0, 2, 4, 6, 8]
    male = [1, 3, 5, 7, 9]

    if validate(pesel, birth, sex):
        try:
            personal_data['birth_date'] = (birth[6:]+'.' + birth[4:6]+'.'+birth[:4])

            if int(pesel[9]) in female:
                personal_data['sex'] = 'female'
            elif int(pesel[9]) in male:
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

