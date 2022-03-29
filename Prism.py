from math import sqrt
def surface_area(l,w,h):
    return 2*(w*l+h*l+h*w)
def volume(l,w,h):
    return w*h*l
def space_diagonal(l,w,h):
    return sqrt(w**2+h**2+l**2)
if __name__=="__main__":
    l=int(input("enter the length"))
    h=int(input("enter the height"))
    w=int(input("enter the width"))

    surface=surface_area(l,h,w)
    print(surface)
    vol=volume(l,h,w)
    print(vol)
    space=space_diagonal(l,h,w)
    print(space)