"""
This file contains code samples for analyzers.
Run the following to check the available methods:

.. code-block:: shell

   python analyzers.py --help

"""
import typer
from rich.console import Console

from config import INDEX_NAME, client
from helpers import log_titles
from typing import List

app = typer.Typer(rich_markup_mode="rich")
console = Console()
resp = client.search(index=INDEX_NAME, body=query_body)


analyzers = [
    "standard",
    "simple",
    "whitespace",
    "stop",
    "keyword",
    "pattern",
    "fingerprint",
]


def generate_tokens(analyzer, text):
    res = os.indices.analyze(body={"analyzer": analyzer, "text": [text]})
    tokens = [sample["token"] for c, sample in enumerate(res["tokens"])]
    print(f"{analyzer} \n")
    print(f"Tokens: {tokens} \n")


if __name__ == "__main__":
    text = "Hello my Name is Laysa.12345"
    for analyzer in analyzers:
        generate_tokens(analyzer, text)
