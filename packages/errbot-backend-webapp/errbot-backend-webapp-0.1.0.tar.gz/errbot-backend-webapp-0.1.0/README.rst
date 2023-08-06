============================
Errbot Webapp backend plugin
============================

.. image:: https://travis-ci.com/attakei/errbot-backend-webapp.svg?branch=master
    :target: https://travis-ci.com/attakei/errbot-backend-webapp

**This is alpha-level implementation. Use only local**

Web UI based backend interface for Errbot (not Webhook feature).

Overview
========

This plugin can exchange messages Errbot and any browsers by WebSocket.
It may be able to supply public chat-bot on a website with Errbot.

Demo
====

.. image:: ./demo.gif

Features
========

* Exchange messages by WebSocket
* HTML for reference implementtion

Usage
=====

Prerequirements
---------------

You must ready environment to run Errbot(>=6.0.x).


Installation
------------

As single source
^^^^^^^^^^^^^^^^

Clone this project and configure to use as extra-backend for Errbot.

.. code-block:: bash

   $ cd /path/to/your-errbot-env
   $ git clone https://github.com/attakei/errbot-backend-webapp.git
   $ pip install -r errbot-backend-webapp/requirements.txt


.. code-block:: python

   BOT_EXTRA_BACKEND_DIR = './errbot-backend-webapp'
   BACKEND = 'Webapp'


As PyPI package
^^^^^^^^^^^^^^^

.. code-block:: bash

   $ cd /path/to/your-errbot-env
   $ pip install errbot-backend-webapp

.. code-block:: python

   import errbot_backend_webapp

   BOT_EXTRA_BACKEND_DIR = errbot_backend_webapp.get_plugin_dir()
   BACKEND = 'Webapp'


Configuration
-------------

Webapp host and port can configure by your ``config.py``.
Plugin see ``BOT_IDENTITY``.

.. code-block:: python

   BOT_IDENTITY = {
       'host': '127.0.0.1',  # Listen host. default is 'localhost'
       'port': 8001,         # Listen port. default is 8080
   }


To Do
=====

- Configuration static resource dir
- Authorize by session

License
=======

GPLv3. `See it <./LICENSE>`_
