from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name = 'testobject',
    packages = ['testobject'],
    version = '1.0.0',
    description = 'Python API wrapper for TestObject',
    author = 'Enrique Gonzalez',
    author_email = 'egonzalezh94@gmail.com',
    license='MIT',
     python_requires=">=3.5",
    url = 'https://github.com/enriquegh/testobject-python-api',
    install_requires=['requests', 'pyyaml'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords = ['wrapper-api', 'testobject'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
)
