def area_of_rec(l,b):
    return l*b
def perimeter_of_rec(l,b):
    return 2*(l+b)
def area_of_circle(r):
    return 22/7*(r**2)
def area_of_square(x):
    return x**2
def area_of_tri(b,h):
    return 1/2*(b*h)

if __name__=="__main__":
    while True:
        print("selct an option")
        print("1.Area of rectangle")
        print("2.perimeter of rectangle")
        print("3.area of circle")
        print("4.area od square")
        print("5.area od triangle")
        print("6.exit")

        option= int(input("enter the option"))

        if option==1:
            l=int(input("enter the length"))
            b=int(input("enter the breadth"))
            arearec=area_of_rec(l,b)
            print(arearec)
        elif option == 2:
            l = int(input("enter the length"))
            b = int(input("enter the breadth"))
            perirec = perimeter_of_rec(l, b)
            print(perirec)
        elif option == 3:
            r = int(input("enter the radius"))
            areacir = area_of_circle(r)
            print(areacir)
        elif option==4:
            x= int(input("enter the sides"))
            areasqr=area_of_square(x)
            print(areasqr)
        elif option==5:
            b = int(input("enter the base"))
            h = int(input("enter the height"))
            areatri=area_of_tri(b,h)
            print(areatri)
        elif option==6:
            break
        else:
            print("invaild option")
