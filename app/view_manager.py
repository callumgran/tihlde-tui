from textual.containers import Container
from app.components import login_view, main_menu, data_view

def switch_view(app, view_name):
    """
    Switch between different views.
    Args:
        app (TIHLDEApp): The main application instance.
        view_name (str): The name of the view to switch to.
    """
    content = app.query_one("#content", Container)
    content.remove_children()
    if view_name == "login_view":
        content.mount(*login_view().children)
    elif view_name == "main_menu":
        content.mount(*main_menu().children)
    elif view_name == "data_view":
        content.mount(*data_view().children)
