.. start-include

===========
autorecipes
===========

Generic Conan_ recipes for C/C++ and Python projects.

.. _Conan: https://docs.conan.io/

.. image:: https://api.bintray.com/packages/jfreeman/jfreeman/autorecipes%3Ajfreeman/images/download.svg
   :target: https://bintray.com/jfreeman/jfreeman/autorecipes%3Ajfreeman/_latestVersion
   :alt: Latest Bintray version

.. .. image:: https://readthedocs.org/projects/autorecipes/badge/?version=latest
   :target: https://autorecipes.readthedocs.io/
   :alt: Documentation status

.. image:: https://travis-ci.org/thejohnfreeman/autorecipes.svg?branch=master
   :target: https://travis-ci.org/thejohnfreeman/autorecipes
   :alt: Build status: Linux and OSX

.. image:: https://ci.appveyor.com/api/projects/status/github/thejohnfreeman/autorecipes?branch=master&svg=true
   :target: https://ci.appveyor.com/project/thejohnfreeman/autorecipes
   :alt: Build status: Windows


C/C++
=====

If your project

- uses CMake_,
- and installs a `package configuration file`__
- that defines the variable ``<PACKAGE_NAME>_COMPONENTS``
- with a list of components,
- and for each of them defines a target ``<package_name>::<component>``,

then you should be able to copy this recipe to package it for Conan:

.. _CMake: https://cmake.org/cmake/help/latest/
.. __: https://cmake.org/cmake/help/latest/manual/cmake-packages.7.html#package-configuration-file

.. code-block:: python

   from conans import python_requires

   CMakeConanFile = python_requires('autorecipes/[*]@jfreeman/testing').cmake()

   class Recipe(CMakeConanFile):
       name = CMakeConanFile.__dict__['name']
       version = CMakeConanFile.__dict__['version']


Python
======

If your project

- uses Poetry_,
- with a ``pyproject.toml`` package metadata file as defined in `PEP 518`_,

.. _Poetry: https://poetry.eustace.io/docs/
.. _PEP 518: https://www.python.org/dev/peps/pep-0518/

then you should be able to copy this recipe to package it for Conan:

.. code-block:: python

   from conans import python_requires

   PythonConanFile = python_requires('autorecipes/[*]@jfreeman/testing').python()

   class Recipe(PythonConanFile):
       name = PythonConanFile.__dict__['name']
       version = PythonConanFile.__dict__['version']


FAQ
===

.. Look at this fucking joke of a syntax. Just let me nest!

- **Why do I need to copy the** ``name`` **and** ``version`` **attributes from
  the base class?**

  Conan parses the recipe looking for the ``name`` and ``version`` attributes,
  instead of just executing it. Thus, we must copy the attributes to move past
  that check.

  Further, these attributes are descriptors_. Accessing them with dot
  notation, like ``CMakeConanFile.name``, evaluates them against the class
  ``CMakeConanFile`` instead of your recipe, but they need the most derived
  type to work correctly.

  .. _descriptors: https://docs.python.org/3/howto/descriptor.html

- **Can I override some attributes?**

  Yes. These base classes just provide default values.

.. end-include
