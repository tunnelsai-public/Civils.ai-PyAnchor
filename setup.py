from setuptools import setup, find_packages

setup(
    name='pyanchorgeo',
    version='0.1.0',
    packages=find_packages(include=['pyanchor', 'pyanchor.*']),
    install_requires=[
        'numpy',
    ]
)