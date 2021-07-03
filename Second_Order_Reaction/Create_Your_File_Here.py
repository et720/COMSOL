import math

#Blank line
print()

#Injection volume
volume = (input("\033[1m" + 'Enter the total volume of reactants you are in injecting into the device (in litres)\nThen press Enter: ' + "\033[1m"))

while volume.isnumeric() == False:
    volume = (input("\033[1m" + 'Please enter a numerical value: ' + "\033[1m"))
else:
    volume = int(volume)

#Calculate height required
height = volume/(2E-9)

#Blank line
print()

#Concentration A
A0 = (input("\033[1m" + 'Enter your initial concentration of reactant A (in molarity), \nThen press Enter: ' + "\033[1m"))

while A0.isnumeric() == False:
    A0 = (input("\033[1m" + 'Please enter a numerical value: ' + "\033[1m"))
else:
    A0 = int(A0)

#Blank line
print()

#Concentration B
B0 = (input("\033[1m" + 'Enter your initial concentration of reactant B (in molarity), \nThen press Enter: ' + "\033[1m"))

while B0.isnumeric() == False:
    B0 = (input("\033[1m" + 'Please enter a numerical value: ' + "\033[1m"))
else:
    B0 = int(B0)

#Blank line
print()

#Diffusivity A
A_diff = (input("\033[1m" + 'Enter the diffusivity of A (in m^2/s), \nThen press Enter: ' + "\033[1m"))

while A_diff.isnumeric() == False:
    A_diff = (input("\033[1m" + 'Please enter a numerical value: ' + "\033[1m"))
else:
    A_diff = int(A_diff)

#Blank line
print()

#Diffusivity B
B_diff = (input("\033[1m" + 'Enter the diffusivity of B (in m^2/s), \nThen press Enter: ' + "\033[1m"))

while B_diff.isnumeric() == False:
    B_diff = (input("\033[1m" + 'Please enter a numerical value: ' + "\033[1m"))
else:
    B_diff = int(B_diff)

#Blank line
print()

#Rate Constant
k = (input("\033[1m" + 'Enter the rate constant (in M^-1.s^1) , \nThen press Enter: ' + "\033[1m"))

while k.isnumeric() == False:
    k = (input("\033[1m" + 'Please enter a numerical value: ' + "\033[1m"))
else:
    k = int(k)

#Blank line
print()

#Filename
name = input("\033[1m" + 'Please enter the name for your personalised text file: \n ' + "\033[1m")

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
txt_file.write("A_diff  " + str(A_diff) + "[M^2/s)]  Diffusivity of A\n" )
txt_file.write("B_diff  " + str(B_diff) + "[M^2/s)]  Diffusivity of B\n" )
txt_file.write("k  " + str(k) + "[(M^-1)*(s^-1)]  Rate constant\n" )
txt_file.close()

#Blank line
print()

print( "\033[1m" + "Your personalised text file has now been created!" + "\033[1m")
print()
print("\033[1m" + "Find your file is here:" + "\033[1m")
print("YourFilePath/foldername/foldername")
print()
print("\033[1m" + "Exiting...." + "\033[1m")

    
exit()

