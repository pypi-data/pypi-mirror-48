
Installation Instructions
=========================

This section covers the basics of how to install, upgrade, and uninstall ``cmd2``.

Installing
----------
First you need to make sure you have Python 3.5+, pip_, and setuptools_.  Then you can just use pip to
install from PyPI_.

.. _pip: https://pypi.python.org/pypi/pip
.. _setuptools: https://pypi.python.org/pypi/setuptools
.. _PyPI: https://pypi.python.org/pypi

.. note::

  Depending on how and where you have installed Python on your system and on what OS you are using, you may need to
  have administrator or root privileges to install Python packages.  If this is the case, take the necessary steps
  required to run the commands in this section as root/admin, e.g.: on most Linux or Mac systems, you can precede them
  with ``sudo``::

    sudo pip install <package_name>


Requirements for Installing
~~~~~~~~~~~~~~~~~~~~~~~~~~~
* If you have Python 3 >=3.5 installed from `python.org
  <https://www.python.org>`_, you will already have pip_ and
  setuptools_, but may need to upgrade to the latest versions:

  On Linux or OS X:

  ::

    pip install -U pip setuptools


  On Windows:

  ::

    python -m pip install -U pip setuptools


.. _`pip_install`:

Use pip for Installing
~~~~~~~~~~~~~~~~~~~~~~

pip_ is the recommended installer. Installing packages from PyPI_ with pip is easy::

    pip install cmd2

This should also install the required 3rd-party dependencies, if necessary.


.. _github:

Install from GitHub using pip
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The latest version of ``cmd2`` can be installed directly from the master branch on GitHub using pip_::

  pip install -U git+git://github.com/python-cmd2/cmd2.git

This should also install the required 3rd-party dependencies, if necessary.


Install from Debian or Ubuntu repos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
We recommend installing from pip_, but if you wish to install from Debian or Ubuntu repos this can be done with
apt-get.

For Python 3::

    sudo apt-get install python3-cmd2

This will also install the required 3rd-party dependencies.

.. warning::

  Versions of ``cmd2`` before 0.7.0 should be considered to be of unstable "beta" quality and should not be relied upon
  for production use.  If you cannot get a version >= 0.7 from your OS repository, then we recommend
  installing from either pip or GitHub - see :ref:`pip_install` or :ref:`github`.


Deploy cmd2.py with your project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``cmd2`` is contained in a small number of Python files, which can be easily copied into your project.  *The
copyright and license notice must be retained*.

This is an option suitable for advanced Python users.  You can simply include the files within your project's hierarchy.
If you want to modify ``cmd2``, this may be a reasonable option.  Though, we encourage you to use stock ``cmd2`` and
either composition or inheritance to achieve the same goal.

This approach will obviously NOT automatically install the required 3rd-party dependencies, so you need to make sure
the following Python packages are installed:

  * attrs
  * colorama
  * pyperclip
  * wcwidth

On Windows, there is an additional dependency:

  * pyreadline


Upgrading cmd2
--------------

Upgrade an already installed ``cmd2`` to the latest version from PyPI_::

    pip install -U cmd2

This will upgrade to the newest stable version of ``cmd2`` and will also upgrade any dependencies if necessary.


Uninstalling cmd2
-----------------
If you wish to permanently uninstall ``cmd2``, this can also easily be done with pip_::

    pip uninstall cmd2


Extra requirement for macOS
===========================
macOS comes with the `libedit <http://thrysoee.dk/editline/>`_ library which is similar, but not identical, to GNU Readline.
Tab-completion for ``cmd2`` applications is only tested against GNU Readline.

There are several ways GNU Readline can be installed within a Python environment on a Mac, detailed in the following subsections.

gnureadline Python module
-------------------------
Install the `gnureadline <https://pypi.python.org/pypi/gnureadline>`_ Python module which is statically linked against a specific compatible version of GNU Readline::

  pip install -U gnureadline

readline via conda
------------------
Install the **readline** package using the ``conda`` package manager included with the Anaconda Python distribution::

  conda install readline

readline via brew
-----------------
Install the **readline** package using the Homebrew package manager (compiles from source)::

  brew install openssl
  brew install pyenv
  brew install readline

Then use pyenv to compile Python and link against the installed readline
