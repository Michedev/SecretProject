from CacheServer import CacheServer
from TheParser import TheConfigParser


class Brain:

    def __init__(self, filename, outputFilename):
        self.parser = TheConfigParser(filename)
        self.parser.readConfiguration()
        self.output = open(outputFilename, mode='w')


    def run(self):
        CacheServer.capacity = self.parser.cacheServerCapacity
        sortedVideos = self.parser.videos.sort(key=lambda video: video.size)
        sortedRequests = self.parser.requests.sort(key=lambda req: req.numRequests)[-1:]
        self.output.write(self.parser.numberOfCacheServer)
        for i in range(self.parser.numberOfCacheServer):
            idVideo = sortedRequests[i].videoID
            video = self.parser.videos[i]
            self.output.write(f"{i} {idVideo}")
