#!/usr/bin/env python
# encoding: utf-8

from distutils.core import setup

setup(name='drainify',
    version='0.1',
    license='GPL',
    description='Recording spotify\'s stream.',
    author='peterr',
    author_email='coderiot@zoho.com',
    url='https://github.com/coderiot/drainify/',
    #install_requires=['dbus-python >= 1.0.0',
                      #'eyed3 >= 0.7.4',
                      #'pygobject'],
    packages=['drainify', ],
    entry_points="""
        [console_scripts]
        drainify = drainify.record:main
    """
)
