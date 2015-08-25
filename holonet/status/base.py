class StatusCheck:

    @property
    def name(self):
        """
        Needs to be valid in a url!
        """
        raise NotImplementedError('Please add the name property.')

    STATUSES = (
        (0, 'Not Responding'),
        (1, 'Ready'),
        (2, 'Unknown'),
    )

    @property
    def status(self):
        raise NotImplementedError('Please implement the status function.')
