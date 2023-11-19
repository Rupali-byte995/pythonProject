# condition to restrict getter and setter
class Password:
    def __init__(self, password):
        self.__password = password

    def print_pwd(self):
        print("Your password is ", self.__password)

    def get_pwd(self):
        return self.__password

    def set_pwd(self, pwd):
        if len(pwd) > 6:
            self.__password = pwd
            print("length is", len(self.__password))
        else:
            print("Weak password")


p = Password("abcdllffkfk")
p.print_pwd()
s = p.get_pwd()
p.set_pwd("rt")
