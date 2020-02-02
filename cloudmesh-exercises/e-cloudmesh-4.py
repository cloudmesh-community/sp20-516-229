# Develop a program that demonstrates the use of cloudmesh.common.Shell.

class CloudMesh4:

    def sampleShellExecute(self):
        """ function to use execute """
        from cloudmesh.common.Shell import Shell
        result = Shell.execute('pwd')
        print(result)

        result = Shell.execute('ls', ['-l', '-a'])
        print(result)

        result = Shell.execute('ls', '-l -a')
        print(result)

if __name__ == "__main__":
    cm1 = CloudMesh4()
    cm1.sampleShellExecute()
