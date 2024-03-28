#Abbreviated words and phrases
#inv- inventory, rentCarOHB- Rent Car on hourly basis, rentCarODB- Rent Car on daily basis,rentCarOWB- Rent Car on weekly basis, 
#req- request, rT- rentalTime, rB- rentalBasis, nOC- number of cars, rP- rentalPeriod
import datetime
class carRental:
    
    def __init__(self,inv=0):
        self.inv=inv
    
    def displayinv(self):
        print("Avaiable no. cars:{}.".format(self.inv))
        return self.inv
    
    def rentCarOHB(self,n):
        if n<=0:
            print("No. of cars should be more than 0.")
            return None
        elif n>self.inv:
            print("Sorry! We only have {} cars available to rent.".format(self.inv))
            return None
        else:
            now=datetime.datetime.now()
            print("You have rented {} car(s) on hourly basis today at {} hours.".format(n,now.hour))
            print("Hourly charge for for each car is 5$.")
            print("Thank you for using our rental service we hope to serve you again.")
            self.inv-=n
            return now
    
    def rentCarODB(self,n):
        if n<=0:
            print("No. of cars should be more than 0.")
            return None
        elif n>self.inv:
            print("Sorry! We only have {} cars available to rent.".format(self.inv))
            return None
        else:
            now=datetime.datetime.now()
            print("You have rented {} car(s) on daily basis today at {} hours.".format(n,now.hour))
            print("Daily charge for for each car is 20$.")
            print("Thank you for using our rental service we hope to serve you again.")
            self.inv-=n
            return now
    
    def rentCarOWB(self,n):
        if n<=0:
            print("No. of cars should be more than 0.")
            return None
        elif n>self.inv:
            print("Sorry! We only have {} cars available to rent.".format(self.inv))
            return None
        else:
            now=datetime.datetime.now()
            print("You have rented {} car(s) on weekly basis today at {} hours.".format(n,now.hour))
            print("Daily charge for for each car is 60$.")
            print("Thank you for using our rental service we hope to serve you again.")
            self.inv-=n
            return now
        
     
    def returnCar(self,req):
        rT,rB,nOC=req
        bill=0
        
        if rT and rB and nOC:
            self.inv+=nOC
            now=datetime.datetime.now()
            rP=now-rT
            
            # For hourly bill calculation
            if rB==1:
                bill=round(rP.seconds/3600)*5*nOC
                
            # For daily bill calculation
            elif rB==2:
                bill=round(rP.days)*20*nOC
        
            # For weekly bill calculation
            elif rB==3:
                bill=round(rP.days/7)*60*nOC
        
            if(7<=nOC<=12):
                print("You are elligible for a promotional discount")
                nill=bill*0.8
            
            print("Thanks for returning the car(s). Hope you enjoyed our service")
            print("Your bill amount is ${}".format(bill))
            return bill
        else:
            print("Are you sure you rented a car from us?")
            return None
        
class Customer:
    def __init__(self):
        self.cars=0
        self.rB=0
        self.rT=0
        self.bill=0
        
    def reqCar(self):
        cars=input("How many cars do you require?")
        try:
            cars=int(cars)
        except ValueError:
            print("The number should be more than 0")
            return -1
        if cars<1:
            print("Invalid input. The no. of cars should be greater than 0!")
            return -1
        else:
            self.cars=cars
        return self.cars
    def returnCar(self):
        if self.rB and self.rT and self.cars:
            return self.rB,self.rT,self.cars
        else:
            return 0,0,0
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        