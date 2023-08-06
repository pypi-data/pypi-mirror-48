import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requires = [
    'requests',
    'lxml',
    'python-dateutil',
    'cryptease'
]

test_requirements = [
    'pytest',
    'vcrpy'
]

about = dict()
with open(os.path.join(here, 'mano', '__version__.py'), 'r') as f:
    exec(f.read(), about)

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=find_packages(),
    package_data={
        '': ['*.json']
    },
    install_requires=requires,
    tests_require=test_requirements
)
