import asyncio


class InferTask:
    def __init__(self, id, tokens, request):
        self.id_ = id
        self.tokens = tokens
        self.request = request
        self.output_queue = asyncio.Queue()
        self._kv_cache_pool_item = None
        self.pos = 0
        self.finished_reason = None
        
    def bind_kvcache(self, kv_cache_pool_item, pos):
        self._kv_cache_pool_item = kv_cache_pool_item
        self.pos = pos
        self.tokens = self.tokens[pos:]

