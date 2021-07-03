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

Creating your personalised parameter file
-------------------

Open terminal or command line and change the directory (‘cd’):

	$ cd YourFilePath/COMSOL-main/Second_Order_Reaction 
 
Run the script using python by typing the following for MacOS:

	$ python Create_Your_File_Here.py
	
Or Windows:
  
	$ python YeastTransformationProtocol_API2


To personalise the COMSOL model for your reaction of interest, you must create a parameters file using the python file attached. There are 7 parameters you must identify:

1) Volume of reactants being used
2) Initial concentration of reactant A
3) Initial concentration of reactant B
4) Diffusivity of reactant A
5) Diffusivity of reactant B
6) Diffusivity of reactant C
7) Rate constant of reaction
