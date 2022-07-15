"""
Helper file to format the results output
when search queries are performed.
"""

from rich import print as rprint, box
from rich.console import Console
from rich.table import Table


def log_titles(result) -> None:
    """
    Helper function to log the titles.
    """
    try:
        hits = result["hits"]["hits"]
        table = Table(title="Results: ", box=box.ROUNDED)
        table.add_column("Title", justify="center", style="cyan", no_wrap=True)
        for res in hits:
            table.add_row(res["_source"]["title"].strip())
        console = Console()
        console.print(table)
    except Exception as e:
        rprint("Error has occurred: %s", e)
