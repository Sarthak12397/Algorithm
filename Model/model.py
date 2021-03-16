class user:
    def __init__(self, uid=0, uname=0, passw=0, add=0, mail=0):
        self.__userid = uid
        self.__username = uname
        self.__password = passw
        self.__address =add
        self.__email = mail

    def set_userId(self, uid):
         self.__userid = uid
    def get_userId(self):
        return self.__userid

    def set_username(self, uname):
        self.__username = uname
    def get_username(self):
        return self.__username


    def set_password(self, passw):
         self.__password = passw
    def get_password(self):
        return self.__password

    def set_address(self,add):
         self.__address = add
    def get_address(self):
        return self.__address


    def set_email(self, mail):
        self.__email = mail
    def get_email(self):
        return self.__email

