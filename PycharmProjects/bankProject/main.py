while True :
    print("you are welcome to meg bank")


    print("i  alredy have a  account = 1")
    print("i  have not had a account yet = 9")
    bankUser = {}

    userType = int(input("please your user type"))

    if userType == 9:
        while True :
            name = input("enter  your name")
            password = input("enter  your passwoord")
            bankUser.update(name : password)







