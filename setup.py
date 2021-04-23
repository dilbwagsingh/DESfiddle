import io
import os
import re
from setuptools import setup, find_packages


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())

# Global variables
LONG_DESCRIPTION = read("README.md")

VERSION="0.0.25"


# Setting up
setup(
    name="DESfiddle",
    version=VERSION,
    url="https://github.com/dilbwagsingh/DESfiddle",

    author="Dilbwag Singh",
    author_email="dilbwagsingh.che18@iitbhu.ac.in",

    description="A python package that offers high flexibility for implementing and experimenting with non-classical DES.",
    long_description = LONG_DESCRIPTION,
    long_description_content_type = "text/markdown",

    packages=find_packages(exclude=["test"]),

    install_requires=[],
    python_requires=">=3.5.0",
    keywords=['python', 'DES', 'Data Encryption Standard', 'DEA', 'Data Encryption Algorithm'],
    classifiers=[
    	"Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Legal Industry",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Security",
        "Topic :: Security :: Cryptography",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    	"License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ]
)
