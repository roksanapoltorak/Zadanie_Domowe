print("Hello. Today we'll verify your PESEL.\n")
print("Let`s remind what it is. PESEL number has the form of YYMMDDZZZXQ, where YYMMDD is the date of birth \n with century encoded in month field, ZZZX is the personal identification number,\n where X codes sex (even number for females, odd number for males) and Q is a check digit, \n which is used to verify whether a given PESEL is correct or not. \n")

import ver_3_peseltools

pesel_of_user = input("Please enter it to check if these conditions are fulfilled: ")

ver_3_peseltools.validate(pesel_of_user)

ver_3_peseltools.extract_personal_data(pesel_of_user)
