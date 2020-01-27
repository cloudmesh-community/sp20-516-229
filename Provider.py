import os as os  # os package help python code to communicate operating system.
import pprint  as pprint


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

    def print_os(self):
        """function to print os name"""
        print(os.name)
        return os.name

    def ram_sapce(self):
        """function to return RAM memory """
        mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')  # e.g. 4015976448
        mem_gib = mem_bytes / (1024 ** 3)
        return mem_gib

    def disk_space(self):
        """function to return HDD memory """
        s = os.statvfs('/')
        total = (s.f_bavail * s.f_frsize) / (1024 ** 3)
        return total


if __name__ == "__main__":  # Python will start running code from here.
    p = Provider()  # creating instance of Provider class
    # p.list()  # Calling list function.
    values = {'os_name' : p.print_os(),'os_ram': p.ram_sapce(), 'os_hdd': p.disk_space()}
    pprint.pprint(values,width=1)
