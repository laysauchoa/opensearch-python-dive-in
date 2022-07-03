OpenSearch® search queries with Python
======================================

This repository contains code examples related to `OpenSearch with Python queries <https://developer.aiven.io/docs/products/opensearch/howto/opensearch-search-and-python.html>`_.

Repository structure
--------------------

* `config.py <https://github.com/aiven/demo-opensearch-python/blob/main/config.py>`_, basic information to connect to the cluster
* `index.py <https://github.com/aiven/demo-opensearch-python/blob/main/index.py>`_, contains methods that manipulate the index
* `search.py <https://github.com/aiven/demo-opensearch-python/blob/main/search.py>`_, contains search queries methods
* `helpers.py <https://github.com/aiven/demo-opensearch-python/blob/main/helpers.py>`_, response handler of search requests

Dataset
-------
You can download the dataset `from Kaggle recipe dataset <https://www.kaggle.com/hugodarwood/epirecipes?select=full_format_recipes.json>`_, and save the ``full_format_recipes.json`` in the current folder of the `demo <https://github.com/aiven/demo-opensearch-python>`_.

Search examples
---------------
The available search options can be found by using help command::

    python search.py --help

Find the arguments to be passed to a certain function by running::

    python search.py OPTION --help


OPTION can be:

* `match <https://opensearch.org/docs/latest/opensearch/query-dsl/full-text/#match>`_
* `multi-match <https://opensearch.org/docs/latest/opensearch/query-dsl/full-text/#match>`_
* `match-phrase <https://opensearch.org/docs/latest/opensearch/query-dsl/full-text/#match-phrase>`_
* `fuzzy <https://opensearch.org/docs/latest/opensearch/query-dsl/full-text/#options>`_
* `term <https://opensearch.org/docs/latest/opensearch/query-dsl/term/#term>`_
* `slop <https://opensearch.org/docs/latest/opensearch/query-dsl/full-text/#options>`_
* `range <https://opensearch.org/docs/latest/opensearch/query-dsl/term/#range>`_
* `query-string <https://opensearch.org/docs/latest/opensearch/query-dsl/full-text/#query-string>`_
* `combine <https://opensearch.org/docs/latest/opensearch/query-dsl/bool/>`_

Quickstart
-----------

To run those examples you need:
* `Python 3.7+ <https://www.python.org/downloads/>`_.
* An OpenSearch® cluster. It can be `set it up manually <https://opensearch.org/downloads.html>`_ or you can use a fully managed service, such as `Aiven for OpenSearch® <https://aiven.io/opensearch>`_.
* OpenSearch cluster `Service URI`

Dependencies
''''''''''''

Install all dependencies::

    pip install -r requirements.txt

Service URI
'''''''''''
To connect with your cluster, you need the **Service URI** of your OpenSearch cluster. You can find the connection details in the section **Overview** on `Aiven web console <https://console.aiven.io>`_. Notice that ``service_uri`` contains credentials; therefore, should be treated with care. 

This project uses ``dotenv`` `Python library <https://pypi.org/project/python-dotenv/>`_ to manage the environment variables.

Replace your ``SERVICE_URI`` on `.env` file with yours as string::

    SERVICE_URI=<https://<user>:<password>@<host>:<port>


Do you have questions?
----------------------
Feel free to open an issue with your question on `Issues` or drop me a message at laysa.uchoa@aiven.com


License
-------

This work is licensed under the Apache License, Version 2.0. Full license text is available in the LICENSE file and at http://www.apache.org/licenses/LICENSE-2.0.txt


Trademarks
----------

OpenSearch, Python are trademarks and property of their respective owners. All product and service names used in this website are for identification purposes only and do not imply endorsement.
