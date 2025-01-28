from textual.containers import Container
from textual.widgets import Static, Button

def create_events_view(app=None):
    """Creates the widgets for the events view."""
    return Container(
        Static("[bold blue]Events are not yet implemented![/bold blue]"),
    )
