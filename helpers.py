"""
Helper file to format the results output
when search queries are performed.
"""

from rich import print as rprint
from rich.console import Console

console = Console(highlight=False)


def log_titles(result) -> None:
    """
    Helper function to log the titles.
    """
    try:
        hits = result["hits"]["hits"]
        console.print(
            [res["_source"]["title"].strip() for res in hits],
            justify="left",
        )
    except Exception as e:
        rprint("Error has occurred: %s", e)
