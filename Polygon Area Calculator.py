# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 21:06:49 2024

@author: jlove
"""

class Rectangle:
    def __init__(self,width,height):
        self.width=int(width)
        self.height=int(height)
    def __str__(self):
        output = f"Rectangle(width={self.width}, height={self.height})"
        return output
    def set_width(self,value):
        self.width = value
    def set_height(self,value):
        self.height = value
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return (2* self.width + 2* self.height)
    def get_diagonal(self):
        return ((self.width ** 2 +self.height**2)**.5)
    def get_picture(self):
        pic=''
        if self.width<=50 and self.height<=50:
            for y in range(self.height):
                for x in range(self.width):
                    pic+='*'
                pic+='\n'
            return pic
        else:
            pic="Too big for picture."
            return pic
        
        
    def get_amount_inside(self,Square):
        return(self.width//Square.width)*(self.height//Square.height)
    
class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)
        self.width = side
        self.height = side
    def __str__(self):
        output = f'Square(side={self.width})'
        return output
    def set_height(self, value):
        super().set_height(value)
        self.width = value
        
    def set_width(self, value):
        super().set_width(value)
        
        self.height = value
    def set_side(self,value):
        self.width = value
        self.height = value

rect = Rectangle(4,8)
print(rect.get_area())
# rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())


sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

sq.set_height(5)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

sq.set_width(6)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(4)
print(rect.get_amount_inside(Rectangle(3,6)))
