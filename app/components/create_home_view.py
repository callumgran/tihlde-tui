from textual.containers import Container
from textual.widgets import Static

def create_home_view():
    """Creates the widgets for the home view."""
    return Container(
        Static("[bold green]Welcome to the TIHLDE Terminal Application[/bold green]", classes="welcome-message"),
        Static("Explore events, career opportunities, news, and more!", id="description"),
        id="home-container",
    )