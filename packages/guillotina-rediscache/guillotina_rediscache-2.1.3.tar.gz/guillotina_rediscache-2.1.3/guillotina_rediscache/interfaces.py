from guillotina.async_util import IAsyncUtility


CACHE_PREFIX = 'gcache2-'

class IRedisChannelUtility(IAsyncUtility):
    pass


class IRedisUtility(IAsyncUtility):
    pass
