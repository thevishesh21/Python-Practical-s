#Menu Driven Program To Calulate Area (Using Elif)
while True:
    print("Menu:")
    print("1. Area Of Circle ")
    print("2. Area Of Rectangle ")
    print("3. Area Of Square ")
    choice=int(input("Enter Your Choice :  "))
    if choice == 1:
        radius = float(input("Enter The Radius Of Circle: "))
        area = 3.14159 * radius * radius
        print("Area Of Circle : ",area)
    elif choice == 2:
        length = float(input("Enter The Length Of Rectangle : "))
        breadth = float(input("Enter The breadth Of Rectangle : "))
        area = length*breadth
        print("Area Of Rectangle : ", area)
    elif choice == 3:
        side = float(input("Enter The Side Of Square : "))
        area = side**2
        print("Area Of Square : ",area)
    else:
        print("invalid Choice")
    again = input("Do You Want To Calulate More? (y/n):  ")
    if again.lower() != "y":
        print("Exiting The Program")
        break
