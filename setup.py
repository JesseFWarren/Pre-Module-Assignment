from setuptools import setup

setup(
    name='csv_filter',
    version='0.1',
    py_modules=['csv_filter'],
    install_requires=[],
    entry_points='''
        [console_scripts]
        csv-filter=csv_filter:main
    ''',
)