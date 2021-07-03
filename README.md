# Simualting reactions in fluid flow using COMSOL

The COMSOL model generates a concentration distribution of products from a first order reaction occuring in flow within a microfluidic device. This can be used to predict the outcome when the device is used for time-resolving cryo-EM.

The microfluidic device includes two inlets from which your reactants are inserted into the device. The two will be completely mixed and allowed to incubate before exiting the device, and used for cryo-EM and imaging.

![image](https://i.postimg.cc/q7qXwKQd/Screenshot-2021-07-03-at-16-41-47.png)

There are various COMSOL models you can use to simulate different types of reactions, including:

![image](https://i.postimg.cc/FKxzYC0r/Screenshot-2021-07-03-at-16-50-50.png)

And using the various python files attached, you can easily generate personalised parameter files to directly insert them into the COMSOL model to run your simulation. 

Download the folder from GitHub
-------------------
![image](https://i.postimg.cc/V6CCdWsD/Screenshot-2021-07-03-at-16-54-58.png)

Once the folder is downloaded, unzip it into your desired destination.

You may notice that there are varioud folders for the different types of reactions. This is required because each type consists of unique parameters and models. 

We will now go through how you can generate your personlised parameter file, using a second order reaction as an example.

Create a personalised parameter file
-------------------

Open terminal or command line and change the directory (‘cd’):

	$ cd YourFilePath/COMSOL-main/Second_Order_Reaction 
 
Run the script using python by typing the following for MacOS and Linux:

	$ python Create_Your_File_Here.py
	
Or Windows:
  
	$ python Create_Your_File_Here


Prompts will appear, as shown below. Enter the specific values for your reaction of interest.

![image](https://i.postimg.cc/qMv4MMv5/Screenshot-2021-07-03-at-17-09-06.png)

Please enter your values in the units stated, and only enter numeric values.

There are 5 main parameters you have to define for each type of reaction:

1) Volume of reactants being used
2) Initial concentration of reactants
3) Diffusivity of reactants
4) Diffusivity of products
5) Rate constant

This will generate a new text file in the same folder as the python file. It contains all the parameters required to run the COMSOL model.

Customise the COMSOL model
-------------------

Open the appropriate .mph COMSOL model, in this case the 'Second_Order_Reaction.mph' file and follow these steps below.

![image](https://i.postimg.cc/66yFDXfk/Screenshot-2021-07-03-at-18-53-04.png)
![image](https://i.postimg.cc/ZnpH4VRd/Screenshot-2021-07-03-at-18-54-40.png)

Further customisation
-------------------

The models can only simulate first, second and third order reactions, all producing one product. However, it is possible to add more reactants or products within the reaction. Follow these steps below.

![image](https://i.postimg.cc/XNzyxwsf/Screenshot-2021-07-03-at-20-05-20.png)

You add each value into the boxes or paramatise by entering them into the parameter table or text file.

![image](https://i.postimg.cc/YqNm6jsk/Screenshot-2021-07-03-at-20-13-40.png)
