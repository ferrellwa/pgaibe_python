'''
Vector2D.py
Created on Jun 18, 2016
    In the book, Buckland uses a "struct" object to define a simple object that
    implements vector operations to associate a game object with spacial properties.
    We're going to make a simple class to mimic this struct.
    
    ---On __slots__
    At first, I wanted to leverage Python's "__slots__" attribute for memory savings
    on a class that doesn't need a "__dict__" that allows for dynamic variable
    additions. After going through some stackoverflowing, I concluded that the benefits
    of memory savings don't trump the option for default variable values for object
    instantiation. This could be an optimization made for production purposes to boost
    performance, but we aren't seeking high performance for our applications (demonstration, only).
    
    The following link is a great discussion of "__slots__" and their mythicals ways:
    https://stackoverflow.com/questions/472000/usage-of-slots/
    
    ---Out-of-line
    There are no equivalents to "inline" functions in Python. Apparently, Cython has
    the capacity of inline function calls:
    http://stackoverflow.com/questions/6442050/python-equivalence-to-inline-functions-or-macros
    
@author: ferrellwa
'''
import math
from math import sqrt

class Vector2D():

    #default coordinates of (0,0) 
    def __init__(self, inputX=0, inputY=0):
        self.x = inputX
        self.y = inputY
    
    #sets x and y to 0
    def Zero(self):
        self.x = 0
        self.y = 0
    
    #returns true if x and y are both 0
    def isZero(self):
        if (self.x == 0) and (self.y == 0):
            return True
        else:
            return False
    
    #returns length of the vector
    def Length(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))
    
    #returns length of vector, squared
    def LengthSq(self):
        return (math.pow(self.x, 2) + math.pow(self.y, 2))
    
    #returns copy of Vector2D with normalized x,y
    def Normalize(self):
        temp = self
        temp.x = temp.x/temp.Length()
        temp.y = temp.y/temp.Length()
        return temp
    
    #returns the dot product between self and v2
    def Dot(self, v2):
        return (self.x * v2.x) + (self.y * v2.y)
    
    #returns positive if v2 is clockwise of self
    #returns negative if counterclockwise of self
    #remember, assume Y points down, and X increasing to the right like a Window app 
    def Sign(self, v2):
        return False
    
    #return the vector that is perpendicular to self
    def Perp(self):
        return False
    
    #adjust x and y so that the length of the vector does not exceed max
    def Truncate(self):
        return False
    
    #returns the distance between self and v2
    def Distance(self, v2):
        return False
    
    #returns the distance between self and v2, squared
    def DistanceSq(self, v2):
        return False
    
    #returns the reverse of this Vector
    def GetReverse(self):
        return False
    
    #+= operator
    def __iadd__(self, v2):
        self.x = self.x + v2.x
        self.y = self.y + v2.y
        return self
    
    #-= operator
    def __isub__(self, v2):
        self.x = self.x - v2.x
        self.y = self.y - v2.y
        return self
    
    #*= operator
    def __imul__(self, v2):
        self.x = self.x * v2.x
        self.y = self.y * v2.y
        return self
    
    #/= operator
    def __idiv__(self, v2):
        self.x = self.x / v2.x
        self.y = self.y / v2.y
        return self
    
    #== logical operator
    def __eq__(self, v2):
        if self.x == v2.x and self.y == v2.y:
            return True
        else:
            return False
    
    #!= logical operator
    def __ne__(self, v2):
        if self.x != v2.x or self.y != v2.y:
            return True
        else:
            return False