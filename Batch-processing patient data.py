import numpy as np
myinput = np.genfromtxt('input_file.txt', dtype=None, encoding=None)

x = open('output.txt','w+') #opening the output file to write to it
y = open('errors.txt','w+') #opening the error file to write to it
print('Loading HealthStats...') #writing to the console
print("\n") #new line

#Defining a Class
class PrimaryClass:
    def __init__(self,mytup): #function to start the tupples
        self.name = mytup[0] #creating a variable with a tupple from the input file
        self.height = mytup[1] #creating a variable with a tupple from the input file
        self.weight = mytup[2] #creating a variable with a tupple from the input file
        self.sex = mytup[3] #creating a variable with a tupple from the input file
        self.age = mytup[4] #creating a variable with a tupple from the input file
        self.activitylevel = mytup[5] #creating a variable with a tupple from the input file
        self.SBP = mytup[6] #creating a variable with a tupple from the input file
        self.DBP = mytup[7] #creating a variable with a tupple from the input file
    
        # Possible Errors
        if self.DBP < 55:
                y.write(f"Invalid DBP: {self.DBP}") #writing to the error file.
                y.write("\n")
        elif self.SBP > 130:
                y.write(f"Invalid SBP: {self.SBP}") #writing to the error file.
                y.write("\n")
        elif self.sex < 1:
                y.write(f"Invalid Gender {self.sex}") #writing to the error file.
                y.write("\n")
        elif self.sex > 2:
                y.write(f"Invalid Gender {self.sex}") #writing to the error file.
                y.write("\n")
        elif self.activitylevel > 5:
                y.write(f"Invalid Activity Level {self.activitylevel}") #writing to the error file.
                y.write("\n")
        elif self.activitylevel < 1:
                y.write(f"Invalid Activity Level {self.activitylevel}") #writing to the error file.
                y.write("\n")
                
        # Funcion for Pulsepressure
    def pulsepressure(self):
        print(f"Name: {self.name}") #to displace in the console 
        print("Calculated Pulse Pressure") #to displace in the console
        self.pulsepress = self.SBP-self.DBP #pulse pressure equation
        x.write(f"Name: {self.name}") #writing results to the output file
        x.write("\n") #new line
        if self.pulsepress > 60: # Possible Error
                y.write(f"Invalid pulsepress {self.pulsepress}") #write to error file
                y.write("\n") #new line
     
    #function for BMI    
    def bmi(self):
        self.bmi=703*(self.weight/(self.height**2)) #BMI equation
        print("Calculated BMI") #to displace in the console
        #flow control
        if self.bmi <18.5:
                x.write(f"BMI:Underweight {self.bmi}") #writing the results to the output file
                x.write("\n") #new line
        #flow control
        elif self.bmi >= 18.5 and self.bmi <=25:
                x.write(f"BMI:Normal {self.bmi}") #writing the results to the output file
                x.write("\n") #new line
        #flow control
        elif self.bmi > 25 and self.bmi<=30:
                x.write(f"BMI:Overweight {self.bmi}") #writing the results to the output file
                x.write("\n") #new line
        #flow control
        elif self.bmi>30:
                x.write(f"BMI:Obese {self.bmi}") #writing the results to the output file
                x.write("\n") #new line
        #Possible Errors
        elif self.bmi < 10:
                y.write(f"Invalid BMI {self.bmi}") #writing the results to the error file
                y.write("\n") #new line
        elif self.bmi > 45:
                y.write(f"Invalid BMI {self.bmi}") #writing the results to the error file
                y.write("\n") #new line
                
    #function for MHR    
    def MHR(self):
            self.MHR = (220-self.age) #MHR equation
            print("Calculated MHR") #displaces on the console
            x.write(f"Max Heart Rate: {self.MHR}") #writing the results to the output file
            x.write("\n") #new line
    #function for BMR        
    def BMR(self):
            self.BMR=0 #place holder to intialize, this can be overridden
            print("Calculated BMR") #writing to the console
            if self.sex == 1: #male
                self.BMR = 66 + (6.23*self.weight)+(12.7*self.height)-(6.8*self.age) #function of BMR if male
                x.write(f"BMR is: {self.BMR}") #writing the results to the output file
                x.write("\n") #new line
            if self.sex == 2: #female
                self.BMR = 655 + (4.35*self.weight)+(4.7*self.height)-(4.7*self.age)#function of BMR if female
                x.write(f"BMR is: {self.BMR}") #writing the results to the output file
                x.write("\n") #new line
            #Possible Error
            if self.BMR < 500:
                y.write(f"Invalid BMR: {self.BMR}") #writing the results to error file
                y.write("\n") #new line
            if self.BMR > 5000:
                y.write(f"Invalid BMR: {self.BMR}") #writing the results to the error file
                y.write("\n") #new line
                
    #Function for CRA        
    def CRA(self):
            self.CRA=0 #place holder to intialize, this can be overridden
            print("Calculated CRA") #print to the console
            print("\n") #new line
            if self.activitylevel==1: #activity level from the input file
                self.CRA = self.BMR*1.2 #equation for CRA given the correct activity level
                x.write(f"Activity Level: {self.activitylevel} Sedentary") #writing to the output file
                x.write("\n") #new line
                x.write(f"CRA: {self.CRA}") #writing to the output file
                x.write("\n") #new line
                x.write("\n") #new line
            elif self.activitylevel==2: #activity level from the input file
                self.CRA = self.BMR*1.375 #equation for CRA given the correct activity level
                x.write(f"Activity Level: {self.activitylevel} Lightly Active") #writing to the output file
                x.write("\n") #new line
                x.write(f"CRA: {self.CRA}") #writing to the output file
                x.write("\n") #new line
                x.write("\n") #new line
            elif self.activitylevel==3: #activity level from input file
                self.CRA = self.BMR*1.55 #equation for CRA given the correct activity level
                x.write(f"Activity Level: {self.activitylevel} Moderately Active") #writing to the output file
                x.write("\n") #new line
                x.write(f"CRA: {self.CRA}") #writing to the output file
                x.write("\n") #new line
                x.write("\n") #new line
            elif self.activitylevel==4: #activity level from input file
                self.CRA = self.BMR*1.725 #equation for CRA given the correct activity level
                x.write(f"Activity Level: {self.activitylevel} Very Active") #writing to the output file
                x.write("\n") #new line
                x.write(f"CRA: {self.CRA}") #writing to the output file
                x.write("\n") #new line
                x.write("\n") #new line
            elif self.activitylevel==5: #activity level from input file
                self.CRA = self.BMR*1.9 #equation for CRA given the correct activity level
                x.write(f"Activity Level: {self.activitylevel} Extra Active") #writing to the output file
                x.write("\n") #new line
                x.write(f"CRA: {self.CRA}") #writing to the output file
                x.write("\n") #new line
                x.write("\n") #new line
            #Possible Errors
            elif self.CRA < 600 or self.CRA > 11400: #bounds for errors
                y.write(f"Invalid CRA {self.CRA} \n") #writing to the error files
                

#Creating an empty list to append so it continously adds to it                
HealthList=[]
for forest in myinput:
    HealthList.append(PrimaryClass(forest))
for Healthstats in HealthList:
    Healthstats.pulsepressure() #pulspressure added to the list
    Healthstats.bmi() #BMI added to the list
    Healthstats.MHR() #MHR added to the list
    Healthstats.BMR() #BMR added to the list
    Healthstats.CRA() #CRA added to the list
    
print("saving data")
x.close() #closing the output file
y.close() #close the error file

