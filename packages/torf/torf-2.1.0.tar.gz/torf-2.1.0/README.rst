torf
====

torf provides a high-level ``Torrent`` class that represents the metainfo of a
torrent. ``Torrent`` instances can be created from scratch, from a file path or
from a `file-like object
<https://docs.python.org/3/glossary.html#term-file-object>`_. A ``Torrent``
instance can create a ``.torrent`` file or a `BTIH magnet link
<https://en.wikipedia.org/wiki/Magnet_link#BitTorrent_info_hash_(BTIH)>`_.

This project started as a fork of `dottorrent
<https://github.com/kz26/dottorrent>`_ but turned into a rewrite with more
features like full control over the torrent's metainfo, validation,
randomization of the info hash to help with cross-seeding and more.

`torf-cli <https://github.com/rndusr/torf-cli>`_ is a command line tool that
makes use of torf.

Example
-------

.. code:: python

    from torf import Torrent
    t = Torrent(path='path/to/content',
                trackers=['https://tracker1.example.org:1234/announce',
                          'https://tracker2.example.org:5678/announce'],
                comment='This is a comment')
    t.private = True
    t.generate()
    t.write('my.torrent')

Documentation
-------------

Documentation is in the docstrings. Read it locally by running ``pydoc3
torf.Torrent`` after the installation. It's also available `online
<https://torf.readthedocs.io/>`_.

Installation
------------

torf is available on `PyPI <https://pypi.org/project/torf>`_.

The latest development version is in the master branch on `GitHub
<https://github.com/rndusr/torf>`_.

Contributing
------------

I consider this project feature complete, but feel free to request new features
or improvements. Bug reports are always welcome, of course.

License
-------

`MIT <https://opensource.org/licenses/MIT>`_
