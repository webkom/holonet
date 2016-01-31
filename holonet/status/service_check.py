from . import manager


def service_check():
    """
    Return a list with tuples of status-checks
    """
    return [(name, check.status) for name, check in manager.items()]
