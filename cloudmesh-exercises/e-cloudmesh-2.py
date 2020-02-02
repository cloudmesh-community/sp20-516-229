# Develop a program that demonstrates the use of dotdict

class CloudMesh2:

    def sampleDotdict(self):
        """ function to use dotdict """
        from cloudmesh.common.dotdict import dotdict
        data = {
            'fname': 'Prateek',
            'mname': 'Kumar',
            'lname': 'Shaw'
        }
        data = dotdict(data)
        print(data.fname)
        print(data.mname)
        print(data.lname)

if __name__ == "__main__":
    cm1 = CloudMesh2()
    cm1.sampleDotdict()
