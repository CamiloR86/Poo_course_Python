#19 August 2023.

class Car:
    def __init__(self, brand, model): #this is a special method of Python to reconize one instance.  
        self.brand = brand
        self.model = model
        self.on = False
    
    def start(self): #definicion de un nuevo metodo. 
        #Acciones que hace este metodo
        self.start = True #Start the car
        print("The", self.brand, self.model, "has started") #Print something. 

    def stop(self): #definicion de un nuevo metodo. 
        self.stop = False #Stop the car
        print("The ", self.brand, self.model, "has to stoped") #Print something.

#Para crear un objeto, le doy el nombre y lo igualo al nombre de la clase. 

corolla = Car("Toyota", "Corolla")
tesla = Car("Tesla", "Model 3")

print(type(corolla)) #Esto imprime el tipo que es Corolla, en este caso <class '__main__.Car'>
print(corolla.model)

corolla.start
corolla.stop
tesla.start
tesla.stop

print(corolla.start())  
print(corolla.stop())

print(tesla.start())  
print(tesla.stop())

