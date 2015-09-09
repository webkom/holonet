import os


def read_message_fixture(name):
    cwd = os.path.dirname(__file__)
    fixture_path = '{}/fixtures/messages/'.format(cwd)
    with open('{}{}'.format(fixture_path, name), 'r') as file:
        content = file.read()
        return content
