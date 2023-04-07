import asyncio
import threading

class ThreadPlus(threading.Thread):
    def __init__(self, target=None, args=(), kwargs={}):
        super().__init__()
        self._stop_event = threading.Event()
        self._target = target
        self._args = args
        self._kwargs = kwargs
        self._coroutine_task = None

    def stop(self):
        self._stop_event.set()
        if self._coroutine_task:
            self._coroutine_task.cancel()
        # get a list of all currently active threads
        threads = threading.enumerate()

        # loop through the threads and stop each one
        for thread in threads:
            thread.stop()
            thread.join()

    def cancel(self):
        if self._coroutine_task:
            self._coroutine_task.cancel()

    def run(self):
        if self._target:
            self._target(*self._args, **self._kwargs)
        elif asyncio.iscoroutinefunction(self._args[0]):
            self._coroutine_task = asyncio.create_task(self._args[0](*self._args[1:], **self._kwargs))
            try:
                asyncio.run(self._coroutine_task)
            except asyncio.CancelledError:
                pass
        else:
            while not self._stop_event.is_set():
                pass
