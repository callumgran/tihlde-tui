from textual.containers import Container
from textual.widgets import Static, Button

def create_news_view():
    """Creates the widgets for the news view."""
    return Container(
        Static("[bold blue]News is not yet implemented![/bold blue]"),
    )
