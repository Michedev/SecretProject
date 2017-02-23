from CacheServer import CacheServer
from TheParser import TheConfigParser
from Utilities import ThePrinter


class Brain:

    def __init__(self, filename, outputFilename):
        self.parser = TheConfigParser(filename)
        self.parser.readConfiguration()
        self.printer = ThePrinter(self.parser.numberOfCacheServer, outputFilename)
        self.cacheServerActualCapacity = [0] * self.parser.numberOfCacheServer
        self.videosInCacheServer = dict([(i, []) for i in range(self.parser.numberOfCacheServer)])


    def run(self):
        CacheServer.capacity = self.parser.cacheServerCapacity
        sortedRequests = self.parser.requests[:]
        sortedRequests.sort(key=lambda req: -req.numRequests)
        for i in range(len(sortedRequests)):
            self.putInCacheServer(sortedRequests[i])
        self.printer.print()


    def putInCacheServer(self, request):

        endpoint = self.parser.endpoints[request.endpointID]
        video = self.parser.videos[request.videoID]
        availableCacheServer = list(filter(lambda cacheServer : self.cacheServerActualCapacity[cacheServer.id] + video.size < CacheServer.capacity, endpoint.cacheServerList))
        if len(availableCacheServer) == 0:
            return None
        bestCacheServer = min(availableCacheServer, key=lambda cacheServer: cacheServer.latency)
        if request.videoID in self.videosInCacheServer[bestCacheServer.id] :
            return None
        self.printer.put(bestCacheServer.id, request.videoID)
        self.cacheServerActualCapacity[bestCacheServer.id] += video.size
        self.videosInCacheServer[bestCacheServer.id].append(request.videoID)


