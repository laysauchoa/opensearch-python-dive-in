 .. raw:: html

   <p align="center">
      <a href="https://aiven.io/blog/opensearch-dinner-party">
         <img src="https://github.com/laysauchoa/opensearch-python-dive-in/blob/main/images/opensearch-python.png" width="60%" alt="OpenSearch Python dive in" />
      </a>
   </p>
   <p align="center">
   </p>

OpenSearch® with Python
========================

This repository contains code examples related to `OpenSearch with Python queries <https://developer.aiven.io/docs/products/opensearch/howto/opensearch-search-and-python.html>`_.

Quickstart
-----------

To run those examples, you need:

* `Python 3.7+ <https://www.python.org/downloads/>`_

* An OpenSearch® cluster. It can be `set it up manually <https://opensearch.org/downloads.html>`_ or you can use a fully managed service, such as `Aiven for OpenSearch® <https://aiven.io/opensearch>`_

* OpenSearch® cluster `Service URI`
  
Repository structure
--------------------
This repository contains the following:

..  code-block::

    ├── CODE_OF_CONDUCT.md
    ├── CONTRIBUTING.rst
    ├── LICENSE
    ├── README.rst
    ├── __init__.py
    ├── analyzer.py
    ├── config.py
    ├── helpers.py
    ├── images
    │   └── opensearch-python.png
    ├── index.py
    ├── recipes.json
    ├── requirements.txt
    └── search.py 


* `config.py <https://github.com/laysauchoa/opensearch-python-dive-in/blob/main/config.py>`_, basic information to connect to the cluster
* `index.py <https://github.com/laysauchoa/opensearch-python-dive-in/blob/main/index.py>`_, contains methods that manipulate the index
* `search.py <https://github.com/laysauchoa/opensearch-python-dive-in/blob/main/search.py>`_, contains search queries methods
* `helpers.py <https://github.com/laysauchoa/opensearch-python-dive-in/blob/main/helpers.py>`_, response handler of search requests
* `analyzer.py <https://github.com/laysauchoa/opensearch-python-dive-in/blob/main/analyzer.py>`_, test built-in analyzers with user input

Dataset
-------
You can download the `Kaggle recipe dataset <https://www.kaggle.com/hugodarwood/epirecipes?select=full_format_recipes.json>`_, and save the file as ``recipes.json`` in this current folder.

Search queries
---------------

The available search options can be found by using the `--help` command::

    python search.py --help

Find the arguments to be passed to a certain function by running::

    python search.py OPTION --help


OPTION can be:

* `match <https://opensearch.org/docs/latest/opensearch/query-dsl/full-text/#match>`_
* `multi-match <https://opensearch.org/docs/latest/opensearch/query-dsl/full-text/#match>`_
* `match-phrase <https://opensearch.org/docs/latest/opensearch/query-dsl/full-text/#match-phrase>`_
* `fuzzy <https://opensearch.org/docs/latest/opensearch/query-dsl/full-text/#options>`_
* `term <https://opensearch.org/docs/latest/opensearch/query-dsl/term/#term>`_
* `range <https://opensearch.org/docs/latest/opensearch/query-dsl/term/#range>`_
* `combine <https://opensearch.org/docs/latest/opensearch/query-dsl/bool/>`_


Test an analyzer 
----------------

OpenSearch comes with a set of built-in analyzers:

- standard
- simple
- whitespace
- stop
- keyword
- pattern
- fingerprint
- languages

You can use ``analyzer.py`` to test how an analyzer works. As a result, you will be able to see which tokens it generates.

The available analyzer options can be found by using the `--help` command::

    python analyzer.py --help

Find the arguments to be passed to a certain function by running::

    python analyzer.py OPTION --help

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


License
-------

|License: CC BY 4.0|

I created this repository to make OpenSearch® easy to use for Python developers.
You can use this work by following the CC-BY license. Please attribute it by mentioning “OpenSearch® and Python by @laysauchoa”.

This work is licensed under a `Creative Commons Attribution 4.0
International License <https://creativecommons.org/licenses/by/4.0/>`__.

.. |License: CC BY 4.0| image:: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
   :target: https://creativecommons.org/licenses/by/4.0/deed.de

Trademarks
----------

OpenSearch® and Python are trademarks and property of their respective owners. All product and service names used in this website are for identification purposes only and do not imply endorsement.

Do you have questions?
----------------------
Feel free to open an issue with your question on `Issues` or drop me a message at ``laysa.uchoa@gmail.com``.


More OpenSearch® resources
--------------------------

- `Migrate from Elasticsearch to OpenSearch client <https://aiven.io/blog/migrate-elasticsearch-client-to-opensearch>`_.
- `Write search queries with OpenSearch and Python <https://aiven.io/blog/opensearch-dinner-party>`_.
