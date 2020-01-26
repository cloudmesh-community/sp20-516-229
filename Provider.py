import os as os  # os package help python code to communicate operating system.


# https://docs.python.org/3/library/os.html


# This class will provide multipass information.
# This class has three functions and default constructor.
# self keyword is same as this in java. This refer current instance of class.
# self should be first argument of the function defined in class.
#
class Provider:
    def list(self):
        """ list function will execute mulitpass find command """
        os.system("multipass find")

    def shell(self):
        """ list function will execute mulitpass shell command """
        os.system("multipass shell")

    def run(self, command):
        """ list function will execute mulitpass exec command """
        os.system(f"multipass exec {command}")


if __name__ == "__main__":  # Python will start running code from here.
    p = Provider()  # creating instance of Provider class
    p.list()  # Calling list function.
