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


# USAGE:

def other_tasks():
    pass

def some_tasks(load_result):
    pass

async def load():
    with await TaskWrapper() as wrapper:
        some_tasks(wrapper.results)
    other_tasks() # other_tasks is executed until wrapper gets a result. Then the code inside context manager is executed
                  # If load() terminates before wrapper, the termination is halted until the context manager terminates

# EQUIVALENT TO:

# def other_tasks():
#     pass

# def some_tasks(loaded_result):
#     pass

# async def load_result():
#     pass

# async def load():
#     task = asyncio.create_task(load_result())
#     other_tasks()
#     await asyncio.gather(task)
#     some_tasks(task.result())
