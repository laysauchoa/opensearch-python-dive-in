"""
Contains index operations. Check the available methods:

.. code-block:: shell

   python index.py --help

"""
import json
from pprint import pprint

import typer
from opensearchpy import helpers, OpenSearch

from config import INDEX_NAME, client


app = typer.Typer()


@app.command("load-data")
def load_data():
    """Send multiple data to an OpenSearch client.

    .. code-block:: shell

        python index.py load-data "recipes.json"

    """

    def load_data():
        """Yields data from json file."""
        with open("recipes.json", "r") as f:
            data = json.load(f)
            for recipe in data:
                yield {"_index": INDEX_NAME, "_source": recipe}
                output = (
                    recipe["title"][:50] + "..."
                    if len(recipe["title"]) > 50
                    else recipe["title"] + "status: ok"
                )
                print(output)

    data = load_data()
    print(f"Ingesting {INDEX_NAME} data")
    response = helpers.bulk(client, data)
    print(f"Data sent to your OpenSearch.")


@app.command("delete-index")
def delete_index(index_name=INDEX_NAME):
    """Delete all the documents of certain index name,
    and raise no exception.

    .. code-block:: shell

        python index.py delete-index INDEX_NAME
    """
    client.indices.delete(index=index_name, ignore=[400, 404])


@app.command("get-cluster-info")
def get_cluster_info():
    """Get information about your OpenSearch cluster

    .. code-block:: shell

        python index.py get-cluster-info

    """
    return pprint(OpenSearch.info(client), width=100, indent=1)


@app.command("get-mapping")
def get_mapping():
    """Retrieve mapping for the index.
    The mapping lists all the fields and their data types.


    .. code-block:: shell

        python index.py get-mapping

    """

    # list of all the cluster's indices
    indices = client.indices.get_alias("*").keys()

    # Example:
    # dict_keys(['.kibana_1', 'epicurious-recipes'])

    mapping_data = client.indices.get_mapping(INDEX_NAME)

    # Find index doc_type
    doc_type = list(mapping_data[INDEX_NAME]["mappings"].keys())[0]

    schema = mapping_data[INDEX_NAME]["mappings"][doc_type]
    pprint(list(schema.keys()))
    print("\n")
    pprint(schema, width=80, indent=0)


if __name__ == "__main__":
    app()
