#decorators eg
from functools import wraps
import logging
import time

def logger(org_function):                                                            #decorator func passing org func
    logging.basicConfig(filename=f'{org_function.__name__}.log', level=logging.INFO) #loggong
    @wraps(org_function)                                                            #wraps org func it helps to nest diff decorators
    def wrapper_function(*args, **kwargs):                                             #adds functionality to org func
        logging.info(f'ran with {org_function.__name__} {args} and {kwargs}')
        return org_function(*args, *kwargs)                                              #calls org func for execution
    return wrapper_function                                             #returns object of wrapper func, this helps the org func assigned with this object

def timer(org_function):
    @wraps(org_function)
    def wrapper_function(*args, **kwargs):
        t1=time.time()
        result = org_function(*args,**kwargs)
        t2=time.time()-t1
        print(f'{org_function.__name__} completed in {t2}')
        return result
    return wrapper_function

@logger
@timer
def display(greeting, name):
    time.sleep(2)
    print(f'{greeting}, {name}!')

display('Hi', 'Lokesh')
display('Hi', 'Sai')
