import asyncio

class TaskEngine:
    def __init__(self, workers=4):
        self.queue = asyncio.Queue()
        self.workers = workers
        self.running = False

    async def worker(self):
        while self.running:
            task = await self.queue.get()
            try:
                await task()
            finally:
                self.queue.task_done()

    async def start(self):
        self.running = True
        self.worker_tasks = [
            asyncio.create_task(self.worker())
            for _ in range(self.workers)
        ]

    async def stop(self):
        self.running = False
        await self.queue.join()
        for w in self.worker_tasks:
            w.cancel()

    async def submit(self, coro):
        await self.queue.put(coro)
