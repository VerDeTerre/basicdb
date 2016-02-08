from setuptools import setup

setup(
    name='basicdb',
    version='0.0.0',
    author='John Tye Bennett',
    author_email='john.tye.bennett@gmail.com',
    description='A small wrapper around a SQLAlchemy database connection',
    packages=['basicdb'],
    install_requires=[
        'sqlalchemy',
    ],
)
