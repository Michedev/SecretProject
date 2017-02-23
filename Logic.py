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
        sortedRequests.sort(key=lambda req: -req.numRequests * self.calculateLatencyGain(req))
        for i in range(len(sortedRequests)):
            self.putInCacheServer(sortedRequests[i])
        self.printer.print()

    def findBestLatencyInCacheServers(self, request):
        endpoint = self.parser.endpoints[request.endpointID]
        video = self.parser.videos[request.videoID]
        if len(endpoint.cacheServerList) == 0:
            return endpoint.latencyToDatacenter - 1
        bestCacheServer = min(endpoint.cacheServerList, key=lambda cacheServer: cacheServer.latency)
        return bestCacheServer.latency

    def calculateLatencyGain(self, request):
        return self.parser.endpoints[request.endpointID].latencyToDatacenter - self.findBestLatencyInCacheServers(request)

    def putInCacheServer(self, request):
        endpoint = self.parser.endpoints[request.endpointID]
        video = self.parser.videos[request.videoID]
        if self.checkIfVideoAlreadyCached(endpoint, request.videoID):
            return None
        availableCacheServer = list(filter(lambda cacheServer : self.cacheServerActualCapacity[cacheServer.id] + video.size < CacheServer.capacity, endpoint.cacheServerList))
        if len(availableCacheServer) == 0:
            return None
        bestCacheServer = min(availableCacheServer, key=lambda cacheServer: cacheServer.latency * 0.6 + (video.size) * 0.1 + (self.cacheServerActualCapacity[cacheServer.id] - video.size) * 0.3)

        self.printer.put(bestCacheServer.id, request.videoID)
        self.cacheServerActualCapacity[bestCacheServer.id] += video.size
        self.videosInCacheServer[bestCacheServer.id].append(request.videoID)

    def checkIfVideoAlreadyCached(self, endpoint, videoID):
        cacheServersIds = [cacheServer.id for cacheServer in endpoint.cacheServerList]
        for cacheServerID in cacheServersIds:
            if videoID in self.videosInCacheServer[cacheServerID]:
                return True
        return False


