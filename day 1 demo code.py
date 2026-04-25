from math import sin, cos, tan, radians, sqrt




def dsin(angle):
    """
    Returns the sin of an angle in degrees.
   
    Args:
        angle, int representing an angle in degrees
    """
    return sin(radians(angle))


def dcos(angle):
    """
    Returns cos of an angle in degrees
   
    Args:
        angle, int representing an angle in degrees
    """
    return cos(radians(angle))


def dtan(angle):
    """
    Returns tan of an angle in degrees
   
    Args:
        angle, int representing an angle in degrees
    """
    return tan(radians(angle))




lens_list=[] # keep it sorted
lens_dict={}


class lens:
    def __init__(self,x, y, width=1, height=1, focal_length=1):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.focal_length=focal_length
        lens_list.append(self)
        lens_dict[x]=self
    def hit(self,y,angle):
        # add formula for getting the new angle here
        return((self.x, y, angle-10))






class laser:
    def __init__(self, angle, *pos):
        self.x=pos[0]
        self.y=pos[1]
        self.angle=angle
        self.pos_list=[(self.y, self.y)]
   
    def hit_test(self):
        for element in lens_list:
            hit_y=self.y+dtan(self.angle)*(element.x-self.x)
            if element.x>self.x:
                if hit_y<=element.y+element.height and hit_y>=element.y-element.height:
                    new_info=element.hit(hit_y,self.angle)
                    self.x, self.y, self.angle=new_info
                    self.pos_list.append((self.x, self.y))
                    break
   
    def __repr__(self):
        return(str(self.pos_list))


a=laser(30,0,0)
b=lens(1,0,1,1,1)
c=lens(4,0,1,5,1)


a.hit_test()
a.hit_test()
print(a)
print(a.angle)

print('test')
print(3^6)