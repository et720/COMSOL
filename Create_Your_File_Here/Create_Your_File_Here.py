class font:
    bold = "\033[1m"
    red = "\033[31;1m"
    green = "\033[32;1m"
    normal = "\033[0m"


#### FUNCTIONS ####

def A_conc():
    while True:
        try:
            A0 = float(input(font.bold +
               '\nEnter your initial concentration of reactant A (in molarity), \nThen press Enter: ' + font.normal))
            txt_file.write("A0  " + str(A0) + "[M]  Initial concentration A\n" )
        except ValueError:
            print(font.red + '\nPlease enter a numerical value. \n ' + font.normal)
        else:
            break

def B_conc():
    while True:
        try:
            B0 = float(input(font.bold +
               '\nEnter your initial concentration of reactant B (in molarity), \nThen press Enter: ' +
               font.normal))
            txt_file.write("B0  " + str(B0) + "[M]  Initial concentration B\n" )
        except ValueError:
            print(font.red + '\nPlease enter a numerical value. \n ' + font.normal)
        else:
            break

def C_conc():
    while True:
        try:
            C0 = float(input(font.bold +
               '\nEnter your initial concentration of reactant C (in molarity), \nThen press Enter: ' +
               font.normal))
            txt_file.write("C0  " + str(C0) + "[M]  Initial concentration C\n" )
        except ValueError:
            print(font.red + '\nPlease enter a numerical value. \n ' + font.normal)
        else:
            break

def A_diff():
    while True:
        try:
            A_diff = float(input(font.bold + '\nEnter the diffusivity of A (in m^2/s), \nThen press Enter: ' +
                  font.normal))
            txt_file.write("A_diff  " + str(A_diff) + "[m^2/s]  Diffusivity of A\n" )
        except ValueError:
            print(font.red + '\nPlease enter a numerical value. \n ' + font.normal)
        else:
            break

def B_diff():
    while True:
        try:
            B_diff = float(input(font.bold + '\nEnter the diffusivity of B (in m^2/s), \nThen press Enter: ' +
                  font.normal))
            txt_file.write("B_diff  " + str(B_diff) + "[m^2/s]  Diffusivity of B\n" )
        except ValueError:
            print(font.red + '\nPlease enter a numerical value. \n ' + font.normal)
        else:
            break

def C_diff():
    while True:
        try:
            C_diff = float(input(font.bold + '\nEnter the diffusivity of C (in m^2/s), \nThen press Enter: ' +
                  font.normal))
            txt_file.write("C_diff  " + str(C_diff) + "[m^2/s]  Diffusivity of C\n" )
        except ValueError:
            print(font.red + '\nPlease enter a numerical value. \n ' + font.normal)
        else:
            break

def one_diff():
    while True:
        try:
            one_diff = float(input(font.bold + '\nEnter the diffusivity of first product (in m^2/s), \nThen press Enter: ' +
                  font.normal))
            txt_file.write("one_diff  " + str(one_diff) + "[m^2/s]  Diffusivity of first product\n" )
        except ValueError:
            print(font.red + '\nPlease enter a numerical value. \n ' + font.normal)
        else:
            break

def two_diff():
    while True:
        try:
            two_diff = float(input(font.bold + '\nEnter the diffusivity of second product (in m^2/s), \nThen press Enter: ' +
                  font.normal))
            txt_file.write("two_diff  " + str(two_diff) + "[m^2/s]  Diffusivity of second product\n" )
        except ValueError:
            print(font.red + '\nPlease enter a numerical value. \n ' + font.normal)
        else:
            break

def three_diff():
    while True:
        try:
            three_diff = float(input(font.bold + '\nEnter the diffusivity of third product (in m^2/s), \nThen press Enter: ' +
                  font.normal))
            txt_file.write("three_diff  " + str(three_diff) + "[m^2/s]  Diffusivity of thrid product\n" )
        except ValueError:
            print(font.red + '\nPlease enter a numerical value. \n ' + font.normal)
        else:
            break

def four_diff():
    while True:
        try:
            four_diff = float(input(font.bold + '\nEnter the diffusivity of fourth product (in m^2/s), \nThen press Enter: ' +
                  font.normal))
            txt_file.write("four_diff  " + str(four_diff) + "[m^2/s]  Diffusivity of fourth product\n" )
        except ValueError:
            print(font.red + '\nPlease enter a numerical value. \n ' + font.normal)
        else:
            break

def five_diff():
    while True:
        try:
            five_diff = float(input(font.bold + '\nEnter the diffusivity of fifth product (in m^2/s), \nThen press Enter: ' +
                  font.normal))
            txt_file.write("five_diff  " + str(five_diff) + "[m^2/s]  Diffusivity of fifth product\n" )
        except ValueError:
            print(font.red + '\nPlease enter a numerical value. \n ' + font.normal)
        else:
            break

def products():
    if pro_num == 1:
        one_diff()

    elif pro_num == 2:
        one_diff()
        two_diff()
    
    elif pro_num == 3:
        one_diff()
        two_diff()
        three_diff()

    elif pro_num == 4:
        one_diff()
        two_diff()
        three_diff()
        four_diff()

    elif pro_num == 5:
        one_diff()
        two_diff()
        three_diff()
        four_diff()
        five_diff()

    else:
        print(font.red + "The maximum number of products is 5. " +
              "If more is required, following the Further Customisation section in the manual" + font.normal)



####################
#       CODE       #
####################

#Filename
name = str(input(font.bold + '\nPlease enter the name for your personalised text file:\n' + font.normal))

#Convert to .txt file
substring = ".xt"
if substring in name:   
    pass
else:           
    name = name + ".txt"

print(font.bold + "\nFor the following reactions:\n" + "1) A --> X" +
       "2) A + B --> X\n" + "3) A + B + C --> X\n" + "4) Other\n" + font.normal )
while True:
    try:
        react_num = int(input(font.bold + '\nWhich type of reaction do you want to model? \nThen press Enter: '+
               font.normal))
        if react_num <= 0 or react_num > 4:
            print(font.red + "\nPlease enter an appropriate value." + font.normal)
            exit()
        elif react_num == 4:
            print(font.red + "\nPlease refer to the manual" + font.normal)
            exit()
        else:
            pass
    except ValueError :
        print(font.red + '\nPlease enter a numerical value. ' +  font.normal)
    else:
        break

while True:
    try:
        pro_num = int(input(font.bold + '\nEnter the number of products, \nThen press Enter: '+
                font.normal))
        if pro_num <= 0:
            print(font.red + "\nPlease enter an appropriate value." +  font.normal)
            exit()
        elif pro_num <= 5:
            pass
        else:
            print(font.red + "\nPlease enter an appropriate value." +  font.normal)
            exit()
    except ValueError:
        print(font.red + '\nPlease enter a numerical value.' +  font.normal)
    else:
        break

txt_file  = open(name, "w+")

if react_num == 1:
    A_conc()
    A_diff()
    products()

elif react_num == 2:
    A_conc()
    B_conc()
    A_diff()
    B_diff()
    products()    

elif react_num == 3:
    A_conc()
    B_conc()
    C_conc()
    A_diff()
    B_diff()
    C_diff()
    products()    

elif react_num == 4:
    print(font.red + "\nPlease refer to the manual" +  font.normal)
    
else:
    print(font.red + "\nError" + font.normal)

#Rate Constant
while True:
    try:
        k = float(input(font.bold + '\nEnter the rate constant (in (M^-1)*(s^-1)) , \nThen press Enter: ' +
                   font.normal))
        txt_file.write("k  " + str(k) + "[(M^-2)*(s^-1)]  Rate constant\n" )
    except ValueError:
        print(font.red + '\nPlease enter a numerical value. \n ' +  font.normal)
    else:
        break

#Injection Volume
while True:
    try:
        volume = float(input(font.bold + '\nEnter the total of reactants you are using (in litres).' +
                       '\nThen press Enter: ' +  font.normal))
    except ValueError:
        print(font.red + '\nPlease enter a numerical value. \n ' +  font.normal)
        continue
    else:
        break
    
#Calculate height required
height = volume/(2E-9)
txt_file.write("height  " + str(height) + "[um]  Height of truncated cone\n" )

    
txt_file.close()

#Blank line
print('\n')

print( font.bold + "Your personalised text file has now been created!" + font.bold)
print('\n')
print("\033[32;1m" + "Exiting...." + "\033[32;1m")

    
exit()


