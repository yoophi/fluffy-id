import os
import re
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def find_version(fname):
    '''Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    '''
    version = ''
    with open(fname, 'r') as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError('Cannot find version information')
    return version


__version__ = find_version(os.path.join("guid_server", "__init__.py"))

setup(
    name='guid_server',
    version=__version__,
    long_description=read('README.md'),
    packages=['guid_server'],
    url='http://github.com/yoophi/guid-server',
    license='',
    author='Pyunghyuk Yoo',
    author_email='yoophi@gmail.com',
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            "guid_server = guid_server.runner:main"
        ]
    },
    install_requires=[
        'Flask==0.10.1',
        'redis==2.10.3',
    ]
)
