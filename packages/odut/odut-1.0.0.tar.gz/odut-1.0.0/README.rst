====
odut
====

.. image:: https://pyup.io/repos/gitlab/minglyu/odut/shield.svg
     :target: https://gitlab.com/minglyupolimi/odut
     :alt: Updates

Odoo utility functions with commnd line interfaces.

1.Before runing the scripts, make sure you have activated your virtual enviroment,
and installed the dependencies:  

``pip3 install -r requirements.txt``


Features
--------
1. Safely remove dependencies of the Odoo modules...
you can either pass modules in a list from the cmd line, or you can just use a file
with the modules listed in the first line of the file.  


Install the package from the source
-----------------------------------
``pip3 install odut``


**Windows**::

  $ odut --modules "['account', 'crm']" --base_dir 'Path to your addons'

**Macos/Linux**::

  $ odut --modules "['account', 'crm']" --base_dir 'Path to your addons'


Packaging Up
-------------

Build the source::

  $ python3 setup.py sdist bdist_wheel

run commands to check the errors::

  $ twine check dist/*

Uploading to Pypi::

  $ python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*


**Caution**:dist file of same name cannot be uploaded again.

Credits
-------
minglyupolimi@gmail.com
