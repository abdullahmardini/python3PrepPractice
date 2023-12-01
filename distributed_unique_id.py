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
from bottle import route, run

class CounterGenerator:
    '''
    Class to keep track of and return the counter. Overall, the UID needs to be unique
    overall, but given that it's composed of time + machineid + counster, the counter
    just needs to be unique per a given epoch time. Unless a user can manipulate the
    flow of time, but that's a different problem.
    '''
    def __init__(self):
        self.time_counter = 0
        self.counter_value= 0

    def get_counter(self, time_now: int) -> int:
        '''
        input: int
        return: int
        Returns some kind of counter.
        '''
        if self.time_counter == time_now:
            self.counter_value += 1
        else: # new epoch time
            self.time_counter = time_now
            self.counter_value = 0

        return self.counter_value


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
    generator = CounterGenerator()
    time_now = time.time()
    machine_id = get_machine_id()
    counter = generator.get_counter(time_now)
    return f'{time_now}.{machine_id}.{counter}'

if __name__ == '__main__':
    run(host='localhost', port=9001, debug=True)
