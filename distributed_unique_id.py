"""
Contained practice script for interviewing.io
https://interviewing.io/mocks/microsoft-system-design-unique-id-generation

Interview question
Design a distributed system to provide a unique ID with each request
Wait does this even make sense as a python script?
We'll see what I can fidangle
"""
#!/usr/bin/python3
from bottle import route, run
from unique_id_gen import CounterGenerator

@route('/ukg')
def unique_key_generator():
    '''
    input: None
    return: None
    returns a unique key consisting of
    time + machine id + counter
    '''
    generator = CounterGenerator()
    return generator.get_uid()

if __name__ == '__main__':
    run(host='localhost', port=9001, debug=True)
