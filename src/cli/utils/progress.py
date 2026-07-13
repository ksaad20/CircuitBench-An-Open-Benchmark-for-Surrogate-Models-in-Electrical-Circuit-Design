"""
Progress bar utilities.
"""

from rich.progress import Progress


def run_with_progress(description: str, task) -> None:
    """
    Execute a callable while displaying a progress bar.
    """
    with Progress() as progress:
        task_id = progress.add_task(description, total=1)
        task()
        progress.update(task_id, advance=1)
