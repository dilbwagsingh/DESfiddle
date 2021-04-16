from setuptools import setup

with open("README.md","r") as desc:
    long_description = desc.read()

# Setting up
setup(
    name="DESfiddle",
    version="0.0.4",
    author="Dilbwag Singh",
    author_email="dilbwagsingh.che18@iitbhu.ac.in",
    description="For experimenting with the Data Encryption Standard",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    py_modules=["utils"],
    package_dir={'':'DESfiddle'},
    install_requires=[],
    keywords=['python', 'DES', 'Data Encryption Standard', 'DEA', 'Data Encryption Algorithm'],
    classifiers=[
    	"Development Status :: 1 - Planning",
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
