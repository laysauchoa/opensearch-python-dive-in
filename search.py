"""
This file contains code samples for search queries.
Run the following to check the available methods:

.. code-block:: shell

   python search.py --help

"""
import typer
from rich.console import Console

from config import INDEX_NAME, SERVICE_URI, client
from helpers import log_titles
from typing import List

app = typer.Typer()
console = Console()


@app.command("match")
def search_match(field: str, query: str, operator: str = "or") -> None:
    """Perform search by relevance for certain field and query."""
    typer.echo(f"Searching for {query} in the field {field} \n")
    query_body = {"query": {"match": {field: {"query": query, "operator": operator}}}}
    resp = client.search(index=INDEX_NAME, body=query_body)
    console.rule("[bold red]Match Query")
    log_titles(resp)


@app.command("multi-match")
def search_multi_match(fields: List[str], query: str) -> None:
    """Perform search by relevance for certain field and query."""
    typer.echo(f"Searching for {query} in the field {fields} \n")
    query_body = {"query": {"multi_match": {"query": query, "fields": fields}}}
    resp = client.search(index=INDEX_NAME, body=query_body)
    log_titles(resp)


@app.command("match-phrase")
def search_match_phrase(field, query, slop=0):
    """Search by match phrase for specific phrases in a field."""
    typer.echo(f"Searching for {query} in the field {field}")
    query_body = {"query": {"match_phrase": {field: {"query": query, "slop": slop}}}}
    resp = client.search(index=INDEX_NAME, body=query_body)
    console.rule("[bold red]Match Phrase Query")
    log_titles(resp)


@app.command("range")
def search_range(field: str, gte, lte) -> None:
    """Search by specifying a range of values for a field"""
    typer.echo(f"Searching for values in the {field} ranging from {gte} to {lte} \n")
    query_body = {"query": {"range": {field: {"gte": gte, "lte": lte}}}}
    resp = client.search(index=INDEX_NAME, body=query_body)
    log_titles(resp)


@app.command("fuzzy")
def search_fuzzy(field, value, fuzziness) -> None:
    """Search by specifying fuzziness to account for typos and misspelling."""
    typer.echo(
        f"Search for {value} in the {field} with fuzziness set to {fuzziness} \n"
    )
    query_body = {
        "query": {
            "fuzzy": {
                field: {
                    "value": value,
                    "fuzziness": fuzziness,
                }
            }
        }
    }
    console.rule("[bold red]Fuzzy Query")
    resp = client.search(index=INDEX_NAME, body=query_body)
    log_titles(resp)


@app.command("combine")
def search_combined_queries():
    """Search by using boolean logic with multiple search queries combined"""
    typer.echo(
        f"Searching for:\n must match category: Quick & Easy;\
         \n must not match ingredients: garlic"
    )
    query_body = {
        "query": {
            "bool": {
                "must": {"match": {"categories": "Quick & Easy"}},
                "must_not": {"match": {"ingredients": "garlic"}},
            }
        }
    }
    resp = client.search(index=INDEX_NAME, body=query_body)
    log_titles(resp)


@app.command("term")
def search_term(field: str, value: int):
    """Searching for exact matches of a value in a field."""
    typer.echo(f"Searching for exact value {value} in the field {field}")
    query_body = {"query": {"term": {field: value}}}
    resp = client.search(index=INDEX_NAME, body=query_body)
    log_titles(resp)


if __name__ == "__main__":
    app()
