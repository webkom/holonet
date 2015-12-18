def split_email(address):
    """
    Split an email address into a user name and domain.
    """
    local_part, at, domain = address.partition('@')
    if len(at) == 0:
        return local_part, None
    return local_part, domain
