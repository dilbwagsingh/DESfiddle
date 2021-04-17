from setuptools import setup, find_packages

# Global variables
with open("README.md","r") as desc:
    long_description = desc.read()

VERSION="0.0.23"


# Setting up
setup(
    name="DESfiddle",
    version=VERSION,
    url="https://github.com/dilbwagsingh/DESfiddle",

    author="Dilbwag Singh",
    author_email="dilbwagsingh.che18@iitbhu.ac.in",

    description="A python package that offers high flexibility for implementing and experimenting with non-classical DES.",
    long_description = long_description,
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
