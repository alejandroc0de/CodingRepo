from View import View
from Base import Base


class Control:
    def __init__(self):
        self.view = View()
        self.base = Base()


    def start(self):
        self.view.welcome()
        flag1=True
        while flag1:
            option = self.view.options()
            if option == 1:
                code = self.view.login()
                if code == self.base.password:
                    self.view.loginGood()
                    flag2 = True
                    while flag2:
                        option2 = self.view.options2()
                        match option2:
                            case 1:
                                self.addPassword()
                            case 2:
                                self.findPassword()
                            case 3:
                                self.listServices()
                            case 4:
                                flag2=False
            else:
                flag1=False
                self.view.loginBad()



    def findPassword(self):
        service = self.view.askService()
        if service in self.base.passwords:
            password = self.base.passwords.get(service)
            self.view.showPassword(password)
        else:
            self.view.serviceNot(service)

    
    def addPassword(self):
        data = self.view.addService()
        name= data[0]
        password = data[1]
        self.base.passwords[name]=password
        self.view.confirmAdd()

    def listServices(self):
        services = []
        for service in self.base.passwords:
            services.append(service)
        self.view.listServices(services)
