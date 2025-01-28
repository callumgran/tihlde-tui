from textual.containers import Container
from textual.widgets import Static

def create_home_view(app=None):
    """Creates the widgets for the home view."""
    user_data = app.context.get_user_data() if app else None
    first_name = user_data["first_name"] if user_data else "Guest"
    last_name = user_data["last_name"] if user_data else ""

    return Container(
        Static(f"[bold green]Welcome, {first_name} {last_name}![/bold green]", classes="welcome-message"),
        Static("Explore events, career opportunities, news, and more!", id="description"),
        id="home-container",
    )