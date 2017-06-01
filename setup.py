import sys
import os
try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

setup (
        name = 'guidebox',
        version = '1.0.2',
        author = 'Brian Seitel',
        author_email = 'brian@guidebox.com',
        packages = ['guidebox'],
        description = 'Guidebox Python Bindings',
        url = 'https://api.guidebox.com',
        license = 'MIT',
        install_requires = [
            'requests'
            ],
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: Implementation :: CPython",
            "Programming Language :: Python :: Implementation :: PyPy"
        ]
      )
