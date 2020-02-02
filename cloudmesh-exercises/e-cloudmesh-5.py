# Develop a program that demonstrates the use of cloudmesh.common.StopWatch.

class CloudMesh5:

    def sampleStopWatch(self):
        """ function to use stop watch """
        from cloudmesh.common.StopWatch import StopWatch
        from time import sleep

        StopWatch.start('test')
        sleep(1)
        StopWatch.stop('test')
        print(StopWatch.get('test'))
        StopWatch.benchmark()

if __name__ == "__main__":
    cm1 = CloudMesh5()
    cm1.sampleStopWatch()
