def Velocity():
    print("1. Velocity")
    print("2. Speed")
    print("3. Time")
    Input = input("What do you want to search : ")

    if Input == "Velocity":
        Time = input("Enter the time taken : ")
        Speed = input("Enter the speed that the object travelled : ")
        Time = int(Time)
        Speed = int(Speed)
        Velocity  = Speed / Time
        print(f"{Speed} / {Time}")
        print(Velocity)
    elif Input == "speed":
        Time = input("Enter the time taken : ")
        Velocity = input("Enetr the Velocity that the object travelled : ")
        Time = int(Time)
        Velocity = int(Velocity)
        Speed  = Velocity * Time
        print(f"{Time} * {Velocity}")
        print(Speed) 
    elif Input == "Time":
        Velocity = input("Enetr the Velocity that the object travelled : ")
        Speed = input("Enetr the speed that the object travelled : ")
        Speed = int(Speed)
        Velocity = int(Velocity)
        Time  = Velocity / Speed
        print(Velocity)

def FinalVelocity():
    print("1. Final Velocity")
    FinalVelocity = input("Enter the FinalVelocity taken : ")
    print(FinalVelocity)

def Displacement():
    print("Finding the Displacement")
    Time = input("Eneter The time taken : ")
    Acceleration = input("Enter the Acceleration ata which the object travelled :  ")
    FinalVelocity = input("Enter the FinalVelocity/IntitalVelocity taken : ")
    Time = int(Time)
    Acceleration = int(Acceleration)
    FinalVelocity = int(FinalVelocity)
    
    Displacement = FinalVelocity * Time + 0.5 * Acceleration * (Time * Time)
    print(f"{FinalVelocity} * {Time} + 0.5 * {Acceleration} * ({Time} * {Time})")
    print(Displacement)

def FinalVelocitySquare():
    IntitalVelocity = input("Enetr Initial Velcoity : ")
    Displacement = input("Enetr the displacmnet of the object : ")
    Acceleration = input("Enter the acceleration of the object : ")
    IntitalVelocity = int(IntitalVelocity)
    Displacement = int(Displacement)
    Acceleration = int(Acceleration)

    VelocitySquare = (IntitalVelocity * IntitalVelocity) + 2 * Acceleration * Displacement
    print(f"({IntitalVelocity} * {IntitalVelocity}) + 2 * {Acceleration} * {Displacement}")
    print(VelocitySquare)

def NewtonSecondLaw():
    Force = input("Enter the Force of the object ")
    Mass = input("Enter the Mass of the object : ")
    Acceleration = input("Enter the Acceleration of the object : ")
    Force = int(Force)
    Mass = int(Mass)
    Acceleration = int(Acceleration)

    print("1. Force")
    print("2. Mass")
    print("3. Acceleration")
    Input = input("What do you want to search : ")

    if Input == "Force":
        Mass = input("Enter the Mass of the object : ")
        Acceleration = input("Enter the Acceleration of the object : ")
        Mass = int(Mass)
        Acceleration = int(Acceleration)

        Force = Mass * Acceleration
        print(f"{Mass} * {Acceleration}")
        print(Force)
    elif Input == "Mass":
        Force = input("Enter the Force of the object ")
        Acceleration = input("Enter the Acceleration of the object : ")
        Force = int(Force)
        Acceleration = int(Acceleration)

        Mass = Force / Acceleration
        print(f"{Force} / {Acceleration}")
        print(Mass)
    elif Input == "Acceleration":
        Mass = input("Enter the Mass of the object : ")
        Force = input("Enter the Acceleration of the object : ")
        Mass = int(Mass)
        Force = int(Acceleration)

        Acceleration = Mass / Force
        print(f"{Mass} / {Force}")
        print(Acceleration)







