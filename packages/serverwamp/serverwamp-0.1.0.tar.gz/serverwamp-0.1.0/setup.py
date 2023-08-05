from setuptools import setup, find_packages
import sys

if sys.version_info < (3, 6):
    raise RuntimeError("serverwamp requires Python 3.6+")

setup(
    name='serverwamp',
    version='0.1.0',
    description=('An adapter for aiohttp, enabling a server to service WAMP '
                 'calls and subscriptions over WebSockets.'),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=(
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Framework :: AsyncIO',
    ),
    install_requires=(
        'aiohttp>=3.0.0',
        'dataclasses~=0.6;python_version<"3.7"'
    ),
    keywords=(
        'WAMP', 'WebSockets', 'aiohttp', 'RPC', 'pubsub', 'broker', 'dealer'
    ),
    author='Justin Turner Arthur',
    author_email='justinarthur@gmail.com',
    url='https://github.com/JustinTArthur/serverwamp',
    license='MIT',
    packages=find_packages(exclude=('tests',)),
)
