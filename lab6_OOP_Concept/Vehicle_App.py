from  OOP_Exercise_Chapter6 import Vehicle

# option
def display_option():
    print("Welcome to Vahicle Data Store Sytem (VDSS)")
    print("1.Add Veheicle")
    print("2.Display all Veheicle")
    print("3.exit")
    select = int(input("select(1-3)? : "))
    if select == 1:
        input_vehicle_data()
    elif select==2:
        display_vehicle()
    elif select ==3:
        print("Good Bay.")
        exit(0)
    else:
        print("Please, select number 1-3.")

# add data
def input_vehicle_data():
    brand = input("Enter vehicle brand: ")
    model = input("Enter vehicle model: ")
    color = input("Enter vehicle color: ")
    maxspeed = int(input("Enter vehicle max speed: "))
    price = float(input("Enter vehicle price: "))

    my_vehicle.append(Vehicle(brand,model,color,maxspeed,price))
    print("\n-----------------------------------")
    print("Alrready add vehicle to store.")
    print("-----------------------------------\n")


    # display data
    def display_vehicle():
        if len(my_vehicle) ==0:
            print("You had no vehicle data.")
        else:
            print(f'You had {len(my_vehicle)} following:')
            for x in my_vehicle:
                x.vehicle_datail()
            print("\n")


# run
my_vehicle = []
s = 0
while s == 0:
    display_option()
