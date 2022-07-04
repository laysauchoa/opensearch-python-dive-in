"""
Helper file to format the results output
when search queries are performed.
"""

from pprint import pprint


def log_titles(result) -> None:
    """
    Helper function to log the titles.
    """
    try:
        hits = result["hits"]["hits"]
        pprint([res["_source"]["title"].strip() for res in hits])
    except Exception as e:
        print("Error has occurred: %s", e)
