from textual.screen import Screen
from textual.containers import Container
from textual.widgets import Header, Footer, Button


class BaseScreen(Screen):
    """Base screen that includes a header and footer."""

    def compose(self):
        """Define the base layout with header, footer, and a content container."""
        yield Header()
        yield Container(
            Button("Home", id="home", variant="primary"),
            Button("Events", id="events", variant="primary"),
            Button("Careers", id="careers", variant="primary"),
            Button("News", id="news", variant="primary"),
            Button("Logout", id="logout", variant="warning"),
            Button("Exit", id="exit", variant="error"),
            id="header",
        )

    def on_button_pressed(self, event):
        """Handle button presses in the menu."""
        button_map = {
            "home": lambda: self.app.switch_to_home(),
            "events": lambda: self.app.show_events(),
            "careers": lambda: self.app.show_careers(),
            "news": lambda: self.app.show_news(),
            "logout": lambda: self.app.logout(),
            "exit": lambda: self.app.exit(),
        }

        action = button_map.get(event.button.id)
        if action:
            action()
        else:
            self.app.log(f"Unknown button pressed: {event.button.id}")
