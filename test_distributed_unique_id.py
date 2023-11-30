"""
test_disributed_unique_id.py
"""

import pytest
import distributed_unique_id as uid

def test_get_machine_id():
    '''
    test machine id function
    '''
    machine_id = uid.get_machine_id()
    assert isinstance(machine_id, str)
    machine_id_2 = uid.get_machine_id()
    assert machine_id == machine_id_2
    # Additional assertions can be added to validate the format of the machine ID

def test_get_counter_increments():
    '''
    test counter, ensure it increments
    '''
    initial_count = uid.get_counter()
    next_count = uid.get_counter()
    assert next_count == initial_count + 1

@pytest.mark.parametrize("execution_number", range(5))
def test_get_counter_uniqueness(execution_number):
    '''
    test counter, ensure uniqueness
    '''
    # This will run the test 5 times to ensure the counter increments uniquely each time
    count = uid.get_counter()
    assert count == execution_number + 1
