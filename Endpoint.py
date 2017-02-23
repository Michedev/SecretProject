from CacheServer import CacheServer

class Endpoint:

    def __init__(self, latency_to_datacenter, cacheServersList):
        self.cacheServerList = [CacheServer(id, latency) for id, latency in cacheServersList]

    def __getitem__(self, item):
        return self.cacheServerList
