"""
test_unique_id_gen.py
"""

from unique_id_gen import CounterGenerator

def test_uid_generator():
    '''
    test that time is actually going up and the counter
    '''
    generator = CounterGenerator()
    uid1 = generator.get_uid()
    uid2 = generator.get_uid()
    uid3 = generator.get_uid()

    assert uid1 < uid2
    assert uid2 < uid3

def test_get_machine_id():
    '''
    test machine id function
    '''
    generator = CounterGenerator()
    machine_id = generator.get_machine_id()
    assert isinstance(machine_id, str)
    machine_id_2 = generator.get_machine_id()
    assert machine_id == machine_id_2

def test_get_counter_increments():
    '''
    test counter, ensure it increments
    '''
    generator = CounterGenerator()
    initial_count = generator.get_counter(100)
    next_count = generator.get_counter(100)
    assert initial_count == type(int)
    assert next_count == initial_count + 1

def test_get_counter_restarts():
    '''
    test counter, ensure it restarts on different time
    '''
    generator = CounterGenerator()
    generator.get_counter(100)
    next_count = generator.get_counter(101)
    assert next_count == 0
