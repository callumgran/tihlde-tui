class AppContext:
    def __init__(self):
        self.user_data = None

    def set_user_data(self, data: dict):
        """Save user data in the context."""
        self.user_data = data

    def get_user_data(self):
        """Retrieve user data from the context."""
        return self.user_data
    
    def clear(self):
        """Clear the context."""
        self.user_data = None