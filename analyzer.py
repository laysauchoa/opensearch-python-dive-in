"""
This file contains code samples for analyzers.
Run the following to check the available methods:

.. code-block:: shell

   python analyzers.py --help

"""
import typer
import collections

from rich.console import Console
from rich.table import Table
from enum import Enum

from config import INDEX_NAME, client
from helpers import log_titles
from typing import List

app = typer.Typer(rich_markup_mode="rich")
console = Console()


class BuiltInAnalyzer(str, Enum):
    standard = "standard"
    simple = "simple"
    whitespace = "whitespace"
    stop = "stop"
    keyword = "keyword"
    pattern = "pattern"
    fingerprint = "fingerprint"


@app.command("test")
def test_analyzer(
    text: str,
    analyzer: BuiltInAnalyzer = BuiltInAnalyzer.standard,
):
    """Tokenizer your input with a built-in analyzer of your choice"""
    res = client.indices.analyze(body={"analyzer": analyzer, "text": [text]})
    tokens = [sample["token"] for c, sample in enumerate(res["tokens"])]
    print(f"{analyzer} \n")
    print(f"Tokens: {tokens} \n")


@app.command("test_all")
def test_analyzers(text: str):
    """Check how your input is tokenized with all OpenSearch built-in analyzers"""
    console.rule("[bold red]OpenSearch® Built-in Analyzers")
    table = Table(title="OpenSearch® Built-in Analyzers")

    table.add_column("Analyzer", justify="right", style="cyan", no_wrap=True)
    table.add_column("Tokens", style="magenta")
    for analyzer in BuiltInAnalyzer:
        res = client.indices.analyze(body={"analyzer": analyzer, "text": [text]})
        tokens = [sample["token"] for c, sample in enumerate(res["tokens"])]

        table.add_row(f"{analyzer}", f"{tokens}")

    console.print(table)


if __name__ == "__main__":
    app()
