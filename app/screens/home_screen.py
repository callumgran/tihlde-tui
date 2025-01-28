from app.screens.base_screen import BaseScreen
from textual.containers import Container
from textual.widgets import Static
from app.api import fetch_user_data


class HomeScreen(BaseScreen):
    """Main home screen for navigation."""

    def compose(self):
        """Define the layout for the home screen."""
        yield from super().compose()
        
        if not self.app.context.get_user_data():
            self.app.context.set_user_data(fetch_user_data(self.app.token))
            
        user_data = self.app.context.get_user_data()
        first_name = user_data["first_name"] if user_data else "Guest"
        last_name = user_data["last_name"] if user_data else ""

        yield Container(
            Static(f"[bold green]Welcome, {first_name} {last_name}![/bold green]", classes="welcome-message"),
            Static("Explore events, career opportunities, news, and more!", id="description"),
            id="home-container",
        )

    def on_button_pressed(self, event):
        """Handle button presses for home-specific actions."""
        super().on_button_pressed(event)
