=================
 Syncurity Utils
=================

The ``syncurity-utils`` package enables Automation and Orchestration efforts with the IR-Flow platform, in conjunction
with our library of Stackstorm Packs.

Usage
~~~~~

Available on PyPI

.. code-block:: bash

    $ pip install syncurity-utils

Use in your Stackstorm pack like so:

.. code-block:: python

    from syncurity_utils import typecheck, find_domain
    from syncurity_utils.exceptions import TypecheckException

