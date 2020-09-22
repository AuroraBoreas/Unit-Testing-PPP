"""
## step #1. make your code publish-ready

some rules of thumbs:
- remove all print statement from your code. if you wanna inform or log something, use logging.
- remove all code that stays outside of class or function. such code (if really necessary), put it under __main__ functions

### create a python package
(known rules / approach)

### add files needed for PyPi
(known rules / approach)

PyPi needs following files in order to work:
- setup.py (detail below)
- LINCENSE.txt (the license file, if u choose MIT, get content from here)
- README.md (optional but highly recommmended)
- HISTORY.md (optional but highly recommended)

### include data files

add the following line to setup() function,
include_package_data=True

## step #2. create PyPi account

if u alrdy have a PyPi account (and still remember your username/password, ofc),
u can skip this step.

otherwise, please goto PyPi homepage and register new account instantly(for free, ofc)

## step #3. generate distribution archives and upload to PyPi

### generating distribution archives

these are archives that are uploaded to the package index and can be installed by pip.

make sure you have the latest version of setuptools and wheel installed.
`pip install --user --upgrade setuptools wheel`

now run this command from the same directory where setup.py is located:
`python3 setup.py sdist bdist_wheel`

### uploading the distribution archives

to do this, u can use twine. first, install it using pip:
`pip install --user --upgrade twince`

then upload all the archives to PyPi:
```
twine upload dist/*
... enter your PyPi username and password
```

## step #4. install your own package using pip

now everyone can install your package with familiar pip install command:
`pip install {your_package_name}`

and update it later
`pip install {your_package_name} --upgrade`

"""

from setuptools import setup, find_packages
with open('README.md') as readme_file:
    README = readme_file.read()
with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='xxx',
    version='0.0.0',
    description='useful balabala',
    long_description_content_type='text/markdown',
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='xx',
    author_email='xxxx@gmail.com',
    keywords=['Elastic', 'ElasticSearch', 'ElasticStack'],
    url='https://github.com/ncthuc/elastictools',
    download_url='https://pypi.org/project/elastictools/',
)

install_requires = [
    'elasticsearch>=6.0.0,<7.0.0',
    'jinja2',
]

if __name__ == "__main__":
    setup(
        **setup_args,
        install_requires=install_requires,
        include_package_data=True, # add this line if includes data(env, config, templates... to package)
    )