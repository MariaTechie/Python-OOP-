import math
class Shapes:
    def __init__(self,color):
        self.__color=color
    def getColor(self):
        return self.__color
    def setColor(self,x):
        self.__color=x
    
    def calculateArea(self):
        pass
    def calcualtePerimeter(self):
        pass
class Rectangle(Shapes):
    shape='rectangle'
    def __init__(self,color,lenght,width):
        super().__init__(color)
        self.__lenght=lenght
        self.__width=width
        
    def rectangleArea(self):
        area = super().calculateArea()
        area=self.__width*self.__lenght
        return area
    def rectanglePerimeter(self):
        perimeter = super().calculatePerimeter()
        perimeter=2*(self.__width+self.__lenght)
        return perimeter
    def display(self):
        return f'the shape is {Rectangle.shape} the perimeter is {self.rectanglePerimeter()} the area is {self.rectangleArea()} the color is {self.__color}'
    
class Circle(Shapes):
    shape ='circle'
    def __init__(self,color,radius):
        super().__init__(color)
        self.__radius = radius
        
    def circleArea(self):
        area = super().calculateArea()
        area= 3.1414 * (self.__radius)**2
        return area
    
    def circlePerimeter(self):
        perimeter=super().calcualtePerimeter()
        perimeter=2*3.14*self.__radius
        return perimeter
    def display(self):
        return f'the shape is {Circle.shape} the perimeter is {self.circlePerimeter()} the area is {self.circleArea()} the color is {self.__color}'
class Triangle(Shapes):
    shape ='triangle'
    def __init__(self,color,c1,c2,c3):
        super().__init__(color)
        self.__c1=c1
        self.__c2= c2
        self.__c3=c3
        
    def trianglePerimeter(self):
        perimeter=super().calcualtePerimeter()
        perimeter=self.__c1+self.__c2+self.__c3
        return perimeter
    
    def triangleArea(self):
        s= super().trianglePerimeter()
        s=(s/2)
        area= math.sqrt(s*(s-self.__c1)*(s-self.__c2)*(s-self.__c3))
        return area
    def display(self):
        return f'the shape is {Triangle.shape} the perimeter is {self.trianglePerimeter()} the area is {self.triangleArea()} the color is {self.__color}'
        
        
        
        
    object1= Rectangle('red',2,4)
    print(object1.display())