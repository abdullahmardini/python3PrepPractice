'''
logic to support distributed unique id problem
practice script for interviewing.io
https://interviewing.io/mocks/microsoft-system-design-unique-id-generation
'''
import time
import uuid

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

    def get_machine_id(self) -> str:
        '''
        input: None
        return: str
        Basically needs to be something unique to the machine.
        Really simple function, but maybe needs to be something more complicated in the future.
        '''
        return str(uuid.getnode())

    def get_epoch_time(self) -> int:
        '''
        input: None
        return: str
        Just gives you default python time
        '''
        return time.time()

    def get_uid(self) -> str:
        '''
        input: None
        return: str
        Put it all together. Keep the logic separate so that it's
        easier to refactor down the line.
        '''
        time_now = self.get_epoch_time()
        machine_id =  self.get_machine_id()
        count = self.get_counter(time_now)
        return f'{time_now}.{machine_id}.{count}'
