########
boostsrl
########

|License|_ |Travis|_ |Codecov|_

.. |License| image:: https://img.shields.io/github/license/starling-lab/boostsrl-python-package.svg
.. _License: LICENSE

.. |Travis| image:: https://travis-ci.org/starling-lab/boostsrl-python-package.svg?branch=master
.. _Travis: https://travis-ci.org/starling-lab/boostsrl-python-package

.. |Codecov| image:: https://codecov.io/gh/starling-lab/boostsrl-python-package/branch/master/graphs/badge.svg?branch=master
.. _Codecov: https://codecov.io/github/starling-lab/boostsrl-python-package?branch=master

**boostsrl** is a set of Python wrappers around
`BoostSRL <https://starling.utdallas.edu/software/BoostSRL>`_ with a scikit-learn interface.

Questions? Contact `Alexander L. Hayes  <https://hayesall.com>`_ (`hayesall <https://github.com/hayesall>`_)

Getting Started
---------------

**Prerequisites**:

- Java 1.8
- Python (3.6, 3.7)

**Installation**

.. code-block:: bash

   pip install boostsrl

Basic Usage
-----------

The general setup should be similar to scikit-learn. But there are a few extra requirements in terms of setting
background knowledge and formatting the data.

A minimal working example (using the Toy-Cancer data set imported with 'example_data') is:

.. code-block:: python

    >>> from boostsrl.rdn import RDN
    >>> from boostsrl import Background
    >>> from boostsrl import example_data
    >>> bk = Background(
    ...     modes=example_data.train.modes,
    ... )
    >>> clf = RDN(
    ...     background=bk,
    ...     target='cancer',
    ...     max_tree_depth=2,
    ...     node_size=1,
    ... )
    >>> clf.fit(example_data.train)
    >>> clf.predict_proba(example_data.test)
    array([0.88079619, 0.88079619, 0.88079619, 0.3075821 , 0.3075821 ])
    >>> clf.classes_
    array([1., 1., 1., 0., 0.])

``example_data.train`` and ``example_data.test`` are each ``boostsrl.Database`` objects, so this hides some of
the complexity behind the scenes.

This example abstracts away some complexity in exchange for compactness.
For more thorough examples, see the `'docs/examples/' <https://github.com/starling-lab/boostsrl-python-package/tree/master/docs/examples>`_ directory.

Contributing
------------

Please refer to `CONTRIBUTING.md <.github/CONTRIBUTING.md>`_ for information on
submitting issues and pull requests.

Versioning
----------

We use `SemVer <https://semver.org>`_ for versioning.
See `Releases <https://github.com/starling-lab/boostsrl-python-package/releases>`_
for stable versions that are available, or the
`Project Page on PyPi <https://pypi.org/project/boostsrl/>`_.
