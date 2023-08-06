Overview
========

Recipe_Caching is an MIT licensed caching extension for the recipe querying
library, written in Python. It caches SQL query results keyed by the SQL query.
By providing a custom oven and a recipe extension. Using it requires defining
a ``dogpile.cache`` cache region, using the caching oven, and telling the recipe
to use the caching extension.

Installation
============

``pip install recipe_caching``

Documentation
=============

https://recipe_caching.readthedocs.io/

Development
===========

To run the tests run::

    py.test
