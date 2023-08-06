"""setup.py - install script for pandoc-tablenos."""

# Copyright 2015-2019 Thomas J. Duck.
# All rights reserved.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import re, io

import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, dist
from setuptools.command.install import install
from setuptools.command.install_scripts import install_scripts

DESCRIPTION = """\
A pandoc filter for numbering tables and their references
when converting markdown documents to other formats.
"""

# From https://stackoverflow.com/a/39671214
__version__ = re.search(
    r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
    io.open('pandoc_tablenos.py', encoding='utf_8_sig').read()
    ).group(1)


#-----------------------------------------------------------------------------
# Hack to overcome pip/setuptools problem on Win 10.  See:
#   https://github.com/tomduck/pandoc-eqnos/issues/6
#   https://github.com/pypa/pip/issues/2783
# Note that cmdclass must be be hooked into setup().

# pylint: disable=invalid-name, too-few-public-methods

# Custom install command class for setup()
class custom_install(install, object):
    """Ensures setuptools uses custom install_scripts."""
    def run(self):
        super(custom_install, self).run()

# Custom install_scripts command class for setup()
class install_scripts_quoted_shebang(install_scripts, object):
    """Ensure there are quotes around shebang paths with spaces."""
    def write_script(self, script_name, contents, mode="t", *ignored):
        shebang = str(contents.splitlines()[0])
        if shebang.startswith('#!') and ' ' in shebang[2:].strip() \
          and '"' not in shebang:
            quoted_shebang = '#!"%s"' % shebang[2:].strip()
            contents = contents.replace(shebang, quoted_shebang)
        super(install_scripts_quoted_shebang,
              self).write_script(script_name, contents, mode, *ignored)

# The custom command classes only need to be used on Windows machines
if os.name == 'nt':
    cmdclass = {'install': custom_install,
                'install_scripts': install_scripts_quoted_shebang},

    # Below is another hack to overcome a separate bug.  The
    # dist.Distribution.cmdclass dict should not be stored in a length-1 list.

    # Save the original method
    # pylint: disable=protected-access
    dist.Distribution._get_command_class = dist.Distribution.get_command_class

    # Define a new method that repairs self.cmdclass if needed
    def get_command_class(self, command):
        """Pluggable version of get_command_class()"""
        try:
            # See if the original behaviour works
            return dist.Distribution._get_command_class(self, command)
        except TypeError:
            # If self.cmdclass is the problem, fix it up
            if type(self.cmdclass) is tuple and type(self.cmdclass[0]) is dict:
                self.cmdclass = self.cmdclass[0]
                return dist.Distribution._get_command_class(self, command)
            else:
                # Something else went wrong
                raise

    # Hook in the new method
    dist.Distribution.get_command_class = get_command_class

else:
    cmdclass = {}

# pylint: enable=invalid-name, too-few-public-methods

#-----------------------------------------------------------------------------


setup(
    name='pandoc-tablenos',
    version=__version__,

    author='Thomas J. Duck',
    author_email='tomduck@tomduck.ca',
    description='Table number filter for pandoc',
    long_description=DESCRIPTION,
    license='GPL',
    keywords='pandoc table numbers filter',
    url='https://github.com/tomduck/pandoc-tablenos',
    download_url='https://github.com/tomduck/pandoc-tablenos/tarball/' + \
                 __version__,

    install_requires=['pandoc-xnos~=2.0.0b2'],

    py_modules=['pandoc_tablenos'],
    entry_points={'console_scripts':['pandoc-tablenos = pandoc_tablenos:main']},
    cmdclass=cmdclass,

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python'
        ],
)
