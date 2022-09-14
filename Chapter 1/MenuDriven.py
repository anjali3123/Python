choice = 0
while(choice!=5):
    print("1.Find are of Circle: ")
    print("2.Find are of Triangle: ")
    print("3.Find are of Rectangle: ")
    print("4.Find the Simple Interest : ")
    print("5.Exit : ")
    choice = input("Enter Your Choice: ")
    if choice.isnumeric():
        choice = int(choice)
        if choice==1:
            PI=3.14
            radius = int(input("Enter Radius for Circle: "))
            circle = PI*radius*radius
            print("Area of Circle is:",circle)
        elif choice==2:
            length = int(input("Enter Length: "))
            base = int(input("Enter Length: "))
            triangle = 1/2(length*base)
            print("Area of Triangle is:",triangle)
        elif choice==3:
            length = int(input("Enter Length: "))
            width = int(input("Enter Width: "))
            rectangle = length*width
            print("Area of Rectangle is:",rectangle)
        elif choice==4:
            P = int(input("Enter Principal Amount: "))
            R = int(input("Enter Interest Rate: "))
            N = int(input("Enter Years: "))
            SI = (P*R*N)/100
            print("Simple Interest is:",SI)
    else:
        print("Please Enter ")