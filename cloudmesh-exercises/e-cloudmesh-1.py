class CloudMesh1:

    def sampleBanner(self):
        """ function to use banner """
        from cloudmesh.common.util import banner
        banner('banner function called')

    def sampleHeading(self):
        """function to use heading"""
        from cloudmesh.common.util import HEADING
        HEADING()

    def sampleVerbose(self):
        """function to use verbose"""
        from cloudmesh.common.debug import VERBOSE
        m = {'key': 'value'}
        VERBOSE(m)


if __name__ == "__main__":
    cm1 = CloudMesh1()
    cm1.sampleBanner()
    cm1.sampleHeading()
