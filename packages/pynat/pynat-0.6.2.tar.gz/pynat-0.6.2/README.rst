.. |pypi| image:: https://img.shields.io/pypi/v/pynat.svg
.. _pypi: https://pypi.python.org/pypi/pynat
.. |license| image:: https://img.shields.io/github/license/arantonitis/pynat.svg
.. _license: https://github.com/arantonitis/pynat/tree/master/LICENSE

PyNAT
*****
|pypi|_ |license|_

Discover external IP addresses and NAT topologies using STUN (Simple Traversal of UDP Through Network Address Translators).

PyNAT follows `RFC 3489`_, and is inspired by a similar program for 
Python 2.x called PyStun_. PyNAT supports Python 2.7 and later.

.. _RFC 3489: https://tools.ietf.org/html/rfc3489
.. _PyStun: https://github.com/jtriley/pystun

Installation
============
PyNAT requires Python 2.7 or later.

From PyPI
---------
Install PyNAT by running ``pip3 install pynat`` from the command line.

.. note::

   On some Linux systems, installation may require running pip with root permissions, or running ``pip3 install pynat --user``. The latter may require exporting `~/.local/bin` to PATH.
   
From GitHub
-----------
Clone or download the `git repo`_, navigate to the directory, and run::

    python3 setup.py sdist
    cd dist
    pip3 install pynat-<version>.tar.gz
    
.. _git repo: https://github.com/arantonitis/pynat

Usage
=====
To get information about the network topology and external IP/port used, run ``pynat``::

    Network type: UDP Firewall 
    Internal address: 127.0.0.1:54320 
    External address: 127.0.0.1:54320
    
Run ``pynat -h`` or ``pynat --help`` for more options::

    usage: pynat [-h] [--source_ip SOURCE_IP] [--source-port SOURCE_PORT]
                 [--stun-host STUN_HOST] [--stun-port STUN_PORT]

    PyNAT v0.0.0 Discover external IP addresses and NAT topologies using STUN.
    Copyright (C) 2018 Ariel Antonitis. Licensed under the MIT License.

    optional arguments:
      -h, --help            show this help message and exit
      --source_ip SOURCE_IP
                            The source IPv4 address to bind to.
      --source-port SOURCE_PORT
                            The source port to bind to.
      --stun-host STUN_HOST
                            The STUN host to use for queries.
      --stun-port STUN_PORT
                            The port of the STUN host to use for queries.
                          
To use PyNAT inside a Python shell or project::

    from pynat import get_ip_info
    topology, ext_ip, ext_port = get_ip_info()
    
To also get information about the internal IP, if unknown::

    topology, ext_ip, ext_port, int_ip = get_ip_info(include_internal=True)
    
Development
===========
PyNAT versioning functions on a ``MAJOR.MINOR.PATCH.[DEVELOP]`` model. Only stable, non development releases will be published to PyPI. Because PyNAT is still a beta project, the ``MAJOR`` increment will be 0. Minor increments represent new features. Patch increments represent problems fixed with existing features.
