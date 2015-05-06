class BasicError:
    """JSON encodable error container"""

    def __init__(self, status=None, message=None):
        """Initializes the object with the basic options"""
        self.status = status
        self.message = message