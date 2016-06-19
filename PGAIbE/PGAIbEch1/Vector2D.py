'''
Created on Jun 18, 2016
    In the book, Buckland uses a "struct" object to define a simple object that
    implements vector operations to associate a game object with spacial properties.
    We're going to make a simple class to mimic this struct.
    
    At first, I wanted to leverage Python's "__slots__" attribute for memory savings
    on a class that doesn't need a "__dict__" that allows for dynamic variable
    additions. After going through some stackoverflowing, I concluded that the benefits
    of memory savings don't trump the option for default variable values for object
    instantiation. This could be an optimization made for production purposes to boost
    performance, but we aren't seeking high performance for our applications (demonstration, only).
    
    The following link is a great discussion of "__slots__" and their mythicals ways:
    https://stackoverflow.com/questions/472000/usage-of-slots/
    
@author: ferrellwa
'''

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
            