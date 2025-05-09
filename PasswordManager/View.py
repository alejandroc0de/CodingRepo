
class View:
    def __init__(self):
        pass

    def welcome(self):
        print("\nWelcome to the password manager! 🔑\n")


    def login(self):
        code = int(input("\nEnter your passcode: 🔐\n"))
        return code
    
    def options(self):
        option = int(input("\nChoose on of these options:\n1.Login\n2.Exit ❌\n"))
        return option

    def options2(self):
        option = int(input("\nChoose on of these options:\n1.Add Password\n2.Find Password\n3.List all services\n4.Exit 🚪\n"))
        return option
    
    def loginGood(self):
        print("\nLogin info correct! 🙂\n")
    
    def loginBad(self):
        print("\nPasscode incorrect! 😥\n")

    def askService(self):
        service = input("\nWhat app are you looking for? 👨🏼‍💻\n").capitalize()
        return service
    
    def showPassword(self,password):
        print(f"\nThe password is {password}\n")
    
    def addService(self):
        nameService=input("\nWhat app are you trying to add to the Manager 📲\n").capitalize()
        passService = input("\nWhat is the password? 🔐\n")
        return nameService,passService
    
    def confirmAdd(self):
        print("\n🗝️ Password added properly! ✅\n")

    def serviceNot(self,app):
        print(f"\nThe app {app} is not in the Manager 🫤")
    
    def listServices(self,list):
        print("\n")
        for i,item in enumerate(list,start=1):
            print(f"{i}. {item}")


# now i will just add a nicer look to it 