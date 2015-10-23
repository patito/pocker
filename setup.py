#/usr/bin/env python

"""The setup and build script for the Pocker project."""


from setuptools import setup, find_packages


__name__         = "pocker"
__description__  = "Messing around with LXC and Python."
__author__       = "Paulo Leonardo Benatto"
__version__      = "0.1"
__author_email__ = "benatto@gmail.com"
__author_site__  = "http://patito.github.io"


setup(name                 = __name__,
      description          = __description__,
      version              = __version__,
      author               = __author__,
      author_email         = __author_email__,
      url                  = __author_site__,

      include_package_data = True,

      packages = find_packages("pocker"),  # include all packages under src
      package_dir = {"": "pocker"},        # tell distutils packages are under src
)
