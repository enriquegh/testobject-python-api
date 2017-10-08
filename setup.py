from distutils.core import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name = 'testobject',
    packages = ['testobject'],
    version = '0.1.0',
    description = 'Python API wrapper for TestObject',
    author = 'Enrique Gonzalez',
    author_email = 'egonzalezh94@gmail.com',
    license='MIT',
    url = 'https://github.com/enriquegh/testobject-python-api',
    install_requires=['requests', 'pyyaml'],
    long_description=readme,
    keywords = ['wrapper-api', 'testobject'],
    classifiers = [],
)