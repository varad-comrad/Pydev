import asyncio

class TaskWrapper:
    def __init__(self, *args, **kwargs) -> None:
        pass

    def __aenter__(self):
        pass

    def __aexit__(self, exc_type, exc_value, trace):
        pass

    def __await__(self):
        pass


# USAGE:

def other_tasks():
    pass # processar html

def some_tasks(load_result):
    pass # processar resultado query banco de dados

async def load():
    async with await TaskWrapper() as wrapper:
        some_tasks(wrapper.results)
    other_tasks() # other_tasks is executed until wrapper gets a result. Then the code inside context manager is executed
    other_tasks() # If load() terminates before wrapper, the termination is halted until the context manager terminates
    other_tasks()
    other_tasks() # wrapper foi carregado aqui
    other_tasks() # so é chamado depois que o codigo do context manager for executado


# EQUIVALENT TO:

# def other_tasks():
#     pass

# def some_tasks(loaded_result):
#     pass

# async def load_result():
#     pass

# async def load():
#     task = asyncio.create_task(load_result())
#     other_tasks() (X4, in this case) 
#     await asyncio.gather(task)
#     some_tasks(task.result())
#     other_tasks() (X1)
