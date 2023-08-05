# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup


setup(
    name='guillotina_gcloudstorage',
    version=open('VERSION').read().strip(),
    description='guillotina gcloud storage support',
    long_description=(open('README.rst').read() + '\n' +
                      open('CHANGELOG.rst').read()),
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    author='Ramon Navarro Bosch',
    author_email='ramon@plone.org',
    keywords='guillotina async cloud storage',
    url='https://pypi.python.org/pypi/guillotina_gcloudstorage',
    license='GPL version 3',
    setup_requires=[
        'pytest-runner',
    ],
    zip_safe=True,

    include_package_data=True,
    packages=find_packages(exclude=['ez_setup']),
    install_requires=[
        'setuptools',
        'guillotina>=4.0.0<5',
        'protobuf',
        'oauth2client',
        'google-cloud-storage',
        'gcloud',
        'ujson',
        'backoff'
    ],
    tests_require=[
        'pytest',
    ],
    entry_points={
        'guillotina': [
            'include = guillotina_gcloudstorage',
        ]
    }
)
