"""SETUPTOOLS CONFIGURATION FILE """
# This file is used to configure the setuptools package for the pytextable
# project.
from setuptools import setup, find_packages

# Read the long description from README.md using a 'with' statement
with open("README.md", encoding="UTF-8") as readme_file:
    long_description = readme_file.read()

setup(
    name="pytextable",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        "pandas>=1.0.0",
    ],
    author="Vadim Tiganov",
    author_email="tiganoviv@gmail.com",
    description="A simple Python tool to generate LaTeX tables",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tiganoviv/pytextable",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
