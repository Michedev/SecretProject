from CacheServer import CacheServer
from TheParser import TheConfigParser
from Utilities import ThePrinter


class Brain:

    def __init__(self, filename, outputFilename):
        self.parser = TheConfigParser(filename)
        self.parser.readConfiguration()
        self.printer = ThePrinter(self.parser.numberOfCacheServer, outputFilename)
        self.cacheServerRemainCapacity = [0] * self.parser.numberOfCacheServer


    def run(self):
        CacheServer.capacity = self.parser.cacheServerCapacity
        sortedRequests = self.parser.requests[:]
        sortedRequests.sort(key=lambda req: -req.numRequests)
        for i in range(len(sortedRequests)):
            self.putInCacheServer(sortedRequests[i])
            idVideo = sortedRequests[i].videoID
            video = self.parser.videos[i]
            self.printer.put(i, idVideo)
        self.printer.print()


    def putInCacheServer(self, request):
        endpoint = self.parser.endpoints[request.endpointID]
        video = self.parser.videos[request.videoID]
        availableCacheServer = list(filter(lambda cacheServer : self.cacheServerRemainCapacity[cacheServer.id] + video.size < CacheServer.capacity, endpoint.cacheServerList))
        if len(availableCacheServer) == 0:
            return None
        bestCacheServer = min(availableCacheServer, key=lambda cacheServer: cacheServer.latency)
        self.printer.put(bestCacheServer.id, request.videoID)


