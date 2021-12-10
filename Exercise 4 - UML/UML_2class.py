class Circle:
    def __init__(self, radius : float = 1.0, color : str = "red") :
        self.__radius = radius
        self.__color = color
    
    def getRadius(self)-> float:
        return self.__radius

    def setRadius(self, radius:float)-> None:
        self.__radius = radius
    
    def getColor(self)-> str:
        return self.__color

    def setColor(self, color:str)-> None:
        self.__color = color
    
    def toString(self)-> str:
        return "The radius is : " + {self.getRadius()} + "\n" + "The color is : " + {self.getColor()}

    def getArea(self)-> float:
        area = (3.14)*(self.getRadius()**2)
        return area

class Cylinder(Circle):
    def __init__(self, radius : float = 1.0, color : str = "red", height : float = 1.0) :
        super().__init__(radius, color)
        self.__height = height
    
    def getHeight(self) -> float:
        return self.__height

    def setHeight(self, height : float) -> None:
        self.__height = height

    def toString(self) -> str:
        return "The height is : " + {self.getHeight()}
    
    def getVolume(self)-> float:
        volume = (3.14)*((self.getRadius())**2)* self.getHeight()
        return volume
