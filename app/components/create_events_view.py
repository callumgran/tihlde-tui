from textual.containers import Container
from textual.widgets import Label, Button, Static, LoadingIndicator
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
        Label(event_details),
        Container(
            Button(f"More Info", id=f"event-{event['id']}", variant="primary"),
            classes="button-container",
        ),
        classes="event-container",
    )

def create_events_view(app):
    """
    Creates an events view that displays events in a scrollable layout.
    Args:
        app: The main application instance.
    Returns:
        Container: The container with the events list.
    """
    events_container = Container(id="events-container")

    async def load_events():
        events_container.mount(LoadingIndicator())
        events = await fetch_events(app.token)
        event_widgets = [create_event_widget(event) for event in events]
        events_container.remove_children()
        if event_widgets:
            events_container.mount(*event_widgets)
        else:
            events_container.mount(
                Static("[bold red]No events available at the moment.[/bold red]")
            )

    app.call_later(load_events)
    return events_container