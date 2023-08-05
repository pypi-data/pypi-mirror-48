from io import open
from setuptools import setup

setup(
    name='async-Eel',
    version='1.0-b2',
    author='namuyang',
    packages=['async_eel'],
    package_data={
        'async_eel': ['eel.js'],
    },
    install_requires=['aiohttp', 'future', 'whichcraft'],
    python_requires='>=3.6',
    description='For little HTML GUI applications, with easy Python/JS interop',
    long_description=open('README.md', encoding='utf-8').readlines()[2],
    keywords=['gui', 'html', 'javascript', 'electron'],
    homepage='https://github.com/namuyan/async-Eel',
)
