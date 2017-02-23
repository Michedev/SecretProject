from Video import Video
from Endpoint import Endpoint
from EndpointRequests import EndpointRequests


class TheConfigParser:
    def __init__(self, nameOfConfigFile):
        self.theFile = 'Config/' + nameOfConfigFile
        self.numberOfVideos = 0
        self.numberOfEndpoints = 0
        self.numberOfRequestDecription = 0
        self.numberOfCacheServer = 0
        self.cacheServerCapacity = 0
        self.videos = []
        self.endpoints = []
        self.requests = []

    def readConfiguration(self):
        theFile = open(self.theFile)

        values = theFile.readline().split(' ')
        self.numberOfVideos = int(values[0])
        self.numberOfEndpoints = int(values[1])
        self.numberOfRequestDecription = int(values[2])
        self.numberOfCacheServer = int(values[3])
        self.cacheServerCapacity = int(values[4])

        values = theFile.readline().split(' ')

        self.videos = [Video(int(el)) for el in values]

        for i in range(0, self.numberOfEndpoints):
            values = theFile.readline().split(' ')
            latency = int(values[0])
            n = int(values[1])
            theList = []
            for j in range(0, n):
                values = theFile.readline().split(' ')
                theList.append([int(values[0]), int(values[1])])
            self.endpoints.append(Endpoint(latency, theList))

        for i in range(0, self.numberOfRequestDecription):
            values = theFile.readline().split(' ')
            self.requests.append(EndpointRequests(int(values[2]), int(values[0]), int(values[1])))
