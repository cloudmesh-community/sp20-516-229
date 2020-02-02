# Develop a program that demonstrates the use of FlatDict

class CloudMesh3:

    def sampleFlatdict(self):
        """ function to use FlatDict """
        from cloudmesh.common.FlatDict import FlatDict
        data = {
            'name': 'Prateek',
                    'address': {'city': 'Naples','state': 'FL'  }
        }

        flat = FlatDict(data, sep=':')
        print(flat)

if __name__ == "__main__":
    cm1 = CloudMesh3()
    cm1.sampleFlatdict()
