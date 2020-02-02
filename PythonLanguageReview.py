class PythonLanguageReview:

    def learnPrint(self):
        name = "Prateek"
        print(f"He said his name is {name}")

    def f(test):
        msg = "This is a test {test}".format(**locals())
        print("  jj   ", locals())
        from cloudmesh.common.debug import VERBOSE
        d = {'test': 'Gergor'}
        VERBOSE(d, "a", "RED", 100)
        from cloudmesh.common.console import Console

        msg = 'my message'

        Console.ok(msg)  # prins a green message
        Console.error(msg)  # prins a red message proceeded with ERROR
        Console.msg(msg)  # prins a regular black message


        from cloudmesh.common.variables import Variables

        variables = Variables()

        variables['debug'] = True
        variables['trace'] = True
        variables['verbose'] = 10
        m = {'key': 'value'}
        VERBOSE(m)
        a ={ 'p' : "ac"}
        print(a['p'])

        from cloudmesh.common.Shell import Shell

        result = Shell.execute('pwd')
        print(result)

        result = Shell.execute('ls', ['-l', '-a'])
        print(result)

        result = Shell.execute('ls', '-l -a')
        print(result)

        result = Shell.ls('-aux')
        print(result)

        result = Shell.ls('-a')
        print(result)

        result = Shell.pwd()
        print(result)

        from cloudmesh.common.StopWatch import StopWatch
        from time import sleep


        StopWatch.start('test')
        sleep(1)
        StopWatch.stop('test')

        print(StopWatch.get('test'))

if __name__ == "__main__":
    p = PythonLanguageReview()
    p.learnPrint()
    p.f()
