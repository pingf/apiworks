"""
apiwork
-------------
author: dameng
"""
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='apiworks',
    version='2018.11.01',
    url='https://github.com/pingf/apiworks.git',
    license='MIT',
    author='Jesse MENG',
    author_email='pingf0@gmail.com',
    description='api that works!',
    long_description=read('README.rst'),
    py_modules=['apiworks'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    packages=['apiworks'],
    zip_safe=False,
    include_package_data=True,
    # package_data={
    #     'apiworks': ['*'],  # All files from folder A
    # },
    platforms='any',
    install_requires=[
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
