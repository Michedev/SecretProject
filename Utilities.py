class ThePrinter:
    def __init__(self, num, outputFile):
        self.outputs = [str(i) for i in range(0, num)]
        self.numCacheServer = num
        self.outputFile = outputFile

    def put(self, i, idVideo):
        self.outputs[i] += ' ' + str(idVideo)

    def print(self):
        theOutputFile = open(self.outputFile, mode='w')
        for line in self.outputs:
            theOutputFile.write(line + '\n')
        theOutputFile.close()