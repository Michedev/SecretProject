class ThePrinter:
    def __init__(self, num, outputFile):
        self.outputs = [str(i) for i in range(0, num)]
        self.numCacheServer = num
        self.outputFile = outputFile

    def put(self, i, idVideo):
        self.outputs[i] += ' ' + str(idVideo)

    def remove(self, i, idVideo):
        modifiedLine = self.outputs[i].split(' ')
        modifiedLine[1:].remove(str(idVideo))
        self.outputs[i] = str(i) + ' ' + ' '.join(modifiedLine)

    def print(self):
        theOutputFile = open(self.outputFile, mode='w')
        theOutputFile.write(str(self.numCacheServer) + '\n')
        for line in self.outputs:
            theOutputFile.write(line + '\n')
        theOutputFile.close()