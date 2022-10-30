# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="ImgToolsGG",  # todo fix this name
    version="0.1.1",
    description="test how to make a package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://google.com/",
    author="MeJustAFanOfGSW",
    author_email="example@email.com", # todo fix this
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["ImgTools"],  # todo: main folder
    include_package_data=True,
    install_requires=["numpy"]
)



# 1. fix setup.py
# 2. install  wheel  twine
# 3. python setup.py sdist bdist_wheel
# 4. check build run: twine check dist/*
# 5. register on pypi and test.pypi  buxuele # LD8VjZhQFzY@cL_

# 6. upload for test
# twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# 7. upload the real package: twine upload dist/*

# 8 travis-ci, github-账户关联
# 9。  version="0.1.0", -->  version="0.1.1",
# 10。 fix .travis.yml
# token_name: Travis deployment
# token: pypi-AgEIcHlwaS5vcmcCJDJlMGEzZjhkLTVhZDAtNDdiNy1iOTk3LTZkYWQ3ZTc4ZmQ3MwACElsxLFsiaW1ndG9vbHNnZyJdXQACLFsyLFsiZWFmNTUzMzctYWFlMS00ZjExLTg2OTQtZmQ3MWY1NGFhNmRlIl1dAAAGIL8eYhQfLr1HbXamTy5LEDpy2eUqnhzEOFN_RYeRsqJl
