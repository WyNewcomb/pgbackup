from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
        name='pgbackup',
        version='0.1.0',
        author='Wyatt Newcomb'
        author_email='jwn150@gmail.com',
        description='A utility key for backing up PostgreSQL databases.'
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/WyNewcomb/pgbackup',
        packages=find_packages('src'),
)


