#Blank line
print('\n')

#Injection Volume
while True:
    volume = input("\033[1m" + 'Enter the total of reactants you are using (in litres).' +
                       '\nThen press Enter: ' + "\033[1m")
    try:
        volume = float(volume)
        break
    except ValueError:
        print("\033[1m" + '\nPlease enter a numerical value. \n ' + "\033[1m")
        continue

#Calculate height required
height = volume/(2E-9)

#Blank line
print('\n')
print("For the following reaction:  " + "\033[1m" + "A + B --> C\n" + "\033[1m")

#Concentration A
while True:
    A0 = input("\033[1m" +
               'Enter your initial concentration of reactant A (in molarity), \nThen press Enter: ' +
               "\033[1m")
    try:
        A0 = float(A0)
        break
    except ValueError:
        print("\033[1m" + '\nPlease enter a numerical value. \n ' + "\033[1m")
        continue

#Blank line
print('\n')

#Concentration B
while True:
    B0 = input("\033[1m" +
               'Enter your initial concentration of reactant B (in molarity), \nThen press Enter: ' +
               "\033[1m")
    try:
        B0 = float(B0)
        break
    except ValueError:
        print("\033[1m" + '\nPlease enter a numerical value. \n ' + "\033[1m")
        continue

#Blank line
print('\n')

#Diffusivity A
while True:
    A_diff = input("\033[1m" + 'Enter the diffusivity of A (in m^2/s), \nThen press Enter: '+
               "\033[1m")
    try:
        A_diff = float(A_diff)
        break
    except ValueError:
        print("\033[1m" + '\nPlease enter a numerical value. \n ' + "\033[1m")
        continue

#Blank line
print('\n')

#Diffusivity B
while True:
    B_diff = input("\033[1m" + 'Enter the diffusivity of B (in m^2/s), \nThen press Enter: '+
               "\033[1m")
    try:
        B_diff = float(B_diff)
        break
    except ValueError:
        print("\033[1m" + '\nPlease enter a numerical value. \n ' + "\033[1m")
        continue

#Blank line
print('\n')

#Diffusivity C
while True:
    C_diff = input("\033[1m" + 'Enter the diffusivity of C (in m^2/s), \nThen press Enter: '+
               "\033[1m")
    try:
        C_diff = float(C_diff)
        break
    except ValueError:
        print("\033[1m" + '\nPlease enter a numerical value. \n ' + "\033[1m")
        continue

#Blank line
print('\n')

#Rate Constant
while True:
    k = input("\033[1m" + 'Enter the rate constant (in (M^-1)*(s^-1)) , \nThen press Enter: ' +
                   "\033[1m")
    try:
        k = float(k)
        break
    except ValueError:
        print("\033[1m" + '\nPlease enter a numerical value. \n ' + "\033[1m")
        continue
    
#Blank line
print('\n')

#Filename
name = str(input("\033[1m" + 'Please enter the name for your personalised text file: \n ' + "\033[1m"))

#Convert to .txt file
substring = ".xt"
if substring in name:   
    pass
else:           
    name = name + ".txt"

txt_file  = open(name, "w+")
txt_file.write("height  " + str(height) + "[um]  Height of truncated cone\n" )
txt_file.write("A0  " + str(A0) + "[M]  Initial concentration A\n" )
txt_file.write("B0  " + str(B0) + "[M]  Initial concentration B\n" )
txt_file.write("A_diff  " + str(A_diff) + "[m^2/s]  Diffusivity of A\n" )
txt_file.write("B_diff  " + str(B_diff) + "[m^2/s]  Diffusivity of B\n" )
txt_file.write("C_diff  " + str(C_diff) + "[m^2/s]  Diffusivity of C\n" )
txt_file.write("k  " + str(k) + "[(M^-1)*(s^-1)]  Rate constant\n" )
txt_file.close()

#Blank line
print('\n')

print( "\033[1m" + "Your personalised text file has now been created!" + "\033[1m")
print('\n')
print("\033[32;1m" + "Find your file is here:" + "\033[32;1m")
print("\033[32;1m" + "YourFilePath/COMSOL-main/Second_Order_Reaction/filename.txt" + "\033[32;1m")
print('\n')
print("\033[32;1m" + "Exiting...." + "\033[32;1m")

    
exit()


