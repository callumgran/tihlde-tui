from textual.app import App
from app.screens.events_screen import EventsScreen
from app.screens.home_screen import HomeScreen
from app.screens.login_screen import LoginScreen
from app.screens.event_details_screen import EventDetailsScreen
from app.context import AppContext
from app.utils import load_token


class TIHLDETUI(App):
    CSS_PATH = "app.css"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.token = load_token()
        self.context = AppContext()

    def on_mount(self):
        if self.token:
            self.push_screen(HomeScreen())
        else:
            self.push_screen(LoginScreen())

    def switch_to_home(self):
        self.push_screen(HomeScreen())

    def show_events(self):
        self.push_screen(EventsScreen())

    def show_event_details(self, event_id):
        self.push_screen(EventDetailsScreen(event_id))

    def logout(self):
        self.token = None
        self.pop_screen()
        self.push_screen(LoginScreen())
