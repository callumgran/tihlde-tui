from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer, Button, Input
from app.components import (
    create_login_view,
    create_events_view,
    create_careers_view,
    create_news_view,
    create_home_view,
    create_event_details_view,
)
from app.utils import load_token
from app.actions import handle_login, handle_logout
from app.context import AppContext
from app.api import fetch_user_data

class TIHLDETUI(App):
    CSS_PATH = "app.css"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.token = load_token()
        self.current_view = None
        self.context = AppContext()

        if self.token:
            self.context.set_user_data(fetch_user_data(self.token))

        self.view_map = {
            "login_view": create_login_view,
            "home_view": create_home_view,
            "events_view": create_events_view,
            "careers_view": create_careers_view,
            "news_view": create_news_view,
        }

    def compose(self) -> ComposeResult:
        """Define the initial UI structure."""
        yield Header()
        self.header = Container(
            Button("Home", id="home", variant="primary"),
            Button("Events", id="events", variant="primary"),
            Button("Careers", id="careers", variant="primary"),
            Button("News", id="news", variant="primary"),
            Button("Logout", id="logout", variant="warning"),
            Button("Exit", id="exit", variant="error"),
            id="header",
        )
        yield self.header
        yield Container(id="content")
        yield Footer()

    def on_mount(self) -> None:
        """Initialize the view based on the token."""
        self.update_header_visibility()
        self.switch_view("home_view" if self.token else "login_view")

    def update_header_visibility(self):
        """Show or hide the header based on the token."""
        self.header.visible = bool(self.token)

    def switch_view(self, view_name: str, data: dict = None) -> None:
        """Switch between different views."""
        if self.current_view == view_name:
            self.log(f"Already on view: {view_name}")
            return

        content = self.query_one("#content", Container)
        content.remove_children()

        self.log(f"Switching to view: {view_name}")
        if view_name == "event_details_view":
            content.mount(create_event_details_view(self, data))
        else:
            view_function = self.view_map.get(view_name)
            if view_function:
                content.mount(view_function(self))
            else:
                self.log(f"Unknown view: {view_name}")
        self.current_view = view_name

    def on_button_pressed(self, event):
        """Handle button presses."""
        button_map = {
            "login": lambda: self.login(
                self.query_one("#username", Input).value,
                self.query_one("#password", Input).value,
            ),
            "home": lambda: self.switch_view("home_view"),
            "events": lambda: self.switch_view("events_view"),
            "careers": lambda: self.switch_view("careers_view"),
            "news": lambda: self.switch_view("news_view"),
            "logout": lambda: self.logout(),
            "exit": lambda: self.exit(),
            "back-to-events": lambda: self.switch_view("events_view"),
        }

        if event.button.id and event.button.id.startswith("event-"):
            event_id = event.button.id.split("-")[1]
            self.switch_view("event_details_view", data=event_id)
            return

        action = button_map.get(event.button.id)
        if action:
            action()
        else:
            self.log(f"Unknown button pressed: {event.button.id}")
    
    def login(self, username: str, password: str):
        """Handle login."""
        handle_login(self, username, password)

        if self.token:
            self.context.set_user_data(fetch_user_data(self.token))

        self.update_header_visibility()
        self.switch_view("home_view")

    def logout(self):
        """Handle logout."""
        handle_logout(self)
        self.token = None
        self.context.clear()
        self.update_header_visibility()
        self.switch_view("login_view")
