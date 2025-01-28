class AppContext:
    def __init__(self):
        self.user_data = None

    def set_user_data(self, data: dict):
        self.user_data = data

    def get_user_data(self):
        return self.user_data
    
    def clear(self):
        self.user_data = None