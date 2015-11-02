from django.utils.module_loading import import_string


buffer_interface = None


def load_buffer(module):
    global buffer_interface
    buffer_interface = import_string(module)()
    buffer_interface.set_up()
