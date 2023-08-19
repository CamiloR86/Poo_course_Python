#13 Aug 2023

#La ***Clase*** es la receta que tenemos que seguir para construir un objeto.
#El ***Objeto*** Es lo que resulta despues de hacer la receta. 

#snakecase separaado_por_
#camelcase separadoPorMayusculaLaPrimera
#pascalcase TodasMayusculas, ESTA SE USA PARA LAS CLASES.

#un Objeto es una intancia o el resultado de una clase. 
#para esta clase las propiedades son estáticas. 

class Telefono():
    brand = "samsung"
    model = "S23"
    camera = "200MP"

#para crear un objeto a partir de esta clase: 

#telefono1 = Telefono() #para crear un objeto a partir de esta clase:
#print(telefono1.model)

#ATRIBUTOS, Crear una clase donde los atributos no sean fijos y los pueda variar en cada objeto. 

#class phone: #se pone sin el parentesis, cuando quiero crear un objeto a partir de esta clase...
    #def __init__(self, brand, model, camera): #Automaticamente se activa este METODO. 
        #self.brand = brand
        #self.model = model
        #self.camera = camera


#print(phone1.brand)

#Ahora, para aplicarlo, voy a crear una fábrica de libros. 

#CAMILO'S LIBRARY:

class book:
    def __init__(self, tittle, author, year, pages): #This **function** make activate the **class** when I call it to create the object. **Self**, to assign to itself. 
        self.tittle = tittle 
        self.author = author
        self.year = year
        self.pages = pages

book1 = book("One for the money", "Janet Evanovich", "2004", "450") #Mandatory, put all the arguments. 
print(book1.tittle + " " + "Written By " + book1.author + " in " + book1.year + " and content only " + book1.pages + " Pages!") #There must be some way to call book1, one time. 

#Methods,Equal actions. From one object. 
#All the **functions** that I create on one class calls **Method**. Reserved word **def** def+name+()

#I can include function inside the class. 

class phone: 
    def __init__(self, brand, model, camera): 
        self.brand = brand
        self.model = model
        self.camera = camera

    def call(self):
        print(f'You are calling from: {self.model}')

    def endcall(self):
        print(f'You finish calling from: {self.brand}')

phone1 = phone("Nokia", "5625", "2MP")
print(phone1.call()) #To call the method at the print I have to put().


