"""
test_disributed_unique_id.py
"""

import pytest
import distributed_unique_id as uid

def test_uid_generator():
    '''
    test that time is actually going up
    '''
    uid1 = uid.unique_key_generator()
    uid2 = uid.unique_key_generator()
    uid3 = uid.unique_key_generator()

    assert uid1 < uid2
    assert uid2 < uid3

def test_get_machine_id():
    '''
    test machine id function
    '''
    machine_id = uid.get_machine_id()
    assert isinstance(machine_id, str)
    machine_id_2 = uid.get_machine_id()
    assert machine_id == machine_id_2

def test_get_counter_increments():
    '''
    test counter, ensure it increments
    '''
    generator = uid.CounterGenerator()
    initial_count = generator.get_counter(100)
    next_count = generator.get_counter(100)
    assert next_count == initial_count + 1

def test_get_counter_restarts():
    '''
    test counter, ensure it restarts on different time
    '''
    generator = uid.CounterGenerator()
    generator.get_counter(100)
    next_count = generator.get_counter(101)
    assert next_count == 0

