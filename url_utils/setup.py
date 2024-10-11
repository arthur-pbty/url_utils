from setuptools import setup, find_packages

setup(
    name='url_utils',
    version='0.1',
    packages=find_packages(),
    description='A utility library for URL parsing and manipulation',
    author='Arthur',
    author_email='arthur.puechberty@gmail.com',
    url='https://github.com/arthur-pbty',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)