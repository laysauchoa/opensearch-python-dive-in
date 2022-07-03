from pprint import pprint


def log_titles(result):
    try:
        hits = result["hits"]["hits"]
        pprint([res["_source"]["title"] for res in hits])
    except Exception as e:
        print("Error has occurred: %s", e)
