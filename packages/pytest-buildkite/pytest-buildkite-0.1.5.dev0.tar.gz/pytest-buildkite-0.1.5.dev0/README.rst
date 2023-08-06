=====================
pytest-buildkite
=====================

.. image:: https://dev.azure.com/timgates/timgates/_apis/build/status/pytest-buildkite.pytest-buildkite?branchName=master
   :target: https://dev.azure.com/timgates/timgates/_apis/build/status/pytest-buildkite.pytest-buildkite?branchName=master)](https://dev.azure.com/timgates/timgates/_build/latest?definitionId=11&branchName=master
   :alt: Build status

.. image:: https://img.shields.io/pypi/v/pytest-buildkite.svg
    :target: https://pypi.org/project/pytest-buildkite
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pytest-buildkite.svg
    :target: https://pypi.org/project/pytest-buildkite
    :alt: Python versions

.. image:: https://img.shields.io/pypi/dm/pytest-buildkite.svg
     :target: https://pypi.python.org/pypi/pytest-buildkite/
     :alt: PyPI download month

Note: This library was repurposed from tonybaloney's pytest-azurepipelines,
the repurposing process is not yet complete.

Plugin for `pytest`_ that automatically publishes coverage and pytest report
annotations to BuildKite.

Just run pytest with this plugin and see your test results in the BuildKite UI!

----

Features:

* Formats the PyTest output to show test docstrings and module names instead of just test case names in the Buildkite UI.
* Overloads the `--junit-xml` flag on execution with a default value
* Uploads test results automatically, no need for a seperate test results upload command
* Displays the number of failed tests if there were failures as an error message in the UI
* Automatically formats code coverage and uploads coverage data if pytest-cov is installed


Installation
------------

You can install "pytest-buildkite" via `pip`_ from `PyPI`_::

    $ pip install pytest-buildkite

Running in Docker
-----------------

In order to access the Buildkite agent the docker will need access to the
buildkite-agent binary (either by extending from the official Buildkite docker
image or by installing it in the docker or mounting from the host). Also make
sure that the docker image CA certificates are installed so that it can
publish annotations back to Buildkite via HTTPS. Additionally make sure you
pass down the numerous `Buildkite Environment Variables`_. If you do mount the
agent to provide access you may find you need to mount a few additional
programs called from the agent e.g.:

.. code-block::

    volumes:
      - type: bind
        source: /usr/bin/buildkite-agent
        target: /usr/bin/buildkite-agent
      - type: bind
        source: /usr/bin/buildkite-agent-original
        target: /usr/bin/buildkite-agent-original

Contributing
------------

Contributions are very welcome. 

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-buildkite" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`MIT`: http://opensource.org/licenses/MIT
.. _`file an issue`: https://github.com/pytest-buildkite/pytest-buildkite/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project
.. _`Buildkite Environment Variables`: [https://buildkite.com/docs/pipelines/environment-variables]
