import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='guid_server',
    version='1.1.1',
    long_description=read('README.md'),
    packages=['guid_server'],
    url='http://github.com/yoophi/guid-server',
    license='',
    author='Pyunghyuk Yoo',
    author_email='yoophi@gmail.com',
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask==0.10.1',
        'redis==2.10.3',
    ]
)
