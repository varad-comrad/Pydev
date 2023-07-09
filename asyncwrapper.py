import asyncio

class TaskWrapper:
    def __init__(self, *args, **kwargs) -> None:
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, trace):
        pass

    def __await__(self):
        pass

def other_tasks():
    pass

async def load():
    with await TaskWrapper() as wrapper:
        pass
    other_tasks()