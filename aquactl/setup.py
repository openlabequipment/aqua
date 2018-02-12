from setuptools import setup

setup(
    name='aquactl',
    version='0.1',
    py_modules=[],
    install_requires=[
        'Click',
        'IPython'
    ],
    entry_points='''
        [console_scripts]
        aquactl=aquactl:cli
    ''',
)
