"""
Contained practice script for interviewing.io
https://interviewing.io/mocks/microsoft-system-design-unique-id-generation

Interview question
Design a distributed system to provide a unique ID with each request
Wait does this even make sense as a python script?
We'll see what I can fidangle
"""
#!/usr/bin/python3
import uuid
import time
import os
from bottle import route, run

def get_counter() -> int:
    '''
    input: None
    return: int
    Returns some kind of counter. This needs to be unique per, and has to always increment.
    This is actually a bad idea right here because it creates an unnessary write bottle neck.
    Should use like redis or something, but the idea is to play with theories,
    not implementations.
    '''
    counter_file = 'counter.txt'
    if not os.path.exists(counter_file):
        with open(counter_file, 'w', encoding='utf-8') as f:
            f.write('0')
    with open(counter_file, 'r+', encoding='utf-8') as f:
        counter_value = int(f.read())
        f.seek(0)
        f.write(str(counter_value + 1))
        f.truncate()
    return counter_value


def get_machine_id() -> str:
    '''
    input: None
    return: str
    Basically needs to be something unique to the machine.
    Really simple function, but maybe needs to be something more complicated in the future.
    '''
    return str(uuid.getnode())

@route('/ukg')
def unique_key_generator():
    '''
    input: None
    return: None
    returns a unique key consisting of
    time + machine id + counter
    '''
    machine_id = get_machine_id()
    counter = get_counter()
    return f'{time.time()}.{machine_id}.{counter}'

run(host='localhost', port=9001, debug=True)
