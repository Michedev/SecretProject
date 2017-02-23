from CacheServer import CacheServer

class Endpoint:

    def __init__(self, latency_to_datacenter, cacheServersList):
        self.latencyToDatacenter = latency_to_datacenter
        self.cacheServerList = [CacheServer(id, latency) for id, latency in cacheServersList]

    def __getitem__(self, idCacheServer):
        for cacheServer in self.cacheServerList:
            if idCacheServer == cacheServer.id:
                return cacheServer
        raise Exception("ID Server Not found")
