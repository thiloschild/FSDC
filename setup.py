import setuptools
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fsdc",
    version="0.0.1",
    author="Thilo Schild",
    author_email="work@thilo-schild.de",
    description="Finds identical files in 2 folders and all subfolders",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thiloschild/FSDC",
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
    packages=setuptools.find_packages(),
    install_requires=['argparse'],
    python_requires='>=3.6',
    entry_points={

        'console_scripts': [
            'find_identical_files = fsdc.fsdc:main'
        ],
        
    }
)