from textual.containers import Container
from textual.widgets import Static, Button
from app.api import fetch_events
from app.utils import pretty_print_date

def create_event_widget(event):
    """
    Create a single widget displaying all details of an event.
    Args:
        event (dict): The event data.
    Returns:
        Container: A container with all the event's details combined.
    """
    event_details = (
        f"[bold]{event['title']}[/bold]\n"
        f"Start Date: {pretty_print_date(event['start_date'])}\n"
        f"End Date: {pretty_print_date(event['end_date'])}\n"
        f"Organizer: {event['organizer']['name']}\n"
        f"Category: {event['category']['text']}"
    )

    return Container(
        Static(event_details, classes="event-details"),
        Button(f"More Info", id=f"event-{event['id']}", variant="primary"),
        classes="event-container",
    )

def create_events_view(app=None):
    """
    Creates a simple events view that displays events in a scrollable layout.
    Args:
        app: The main application instance (optional, for access to token).
    Returns:
        Container: The container with the events list.
    """
    events = fetch_events(app.token) if app else []
    event_widgets = [create_event_widget(event) for event in events]

    if not event_widgets:
        return Container(
            Static("[bold red]No events available at the moment.[/bold red]"),
            id="events-container",
        )

    return Container(
        *event_widgets,
        id="events-container",
    )
