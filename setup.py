from setuptools import setup, find_packages

setup(
    name="pylatextable",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        "pandas>=1.0.0",
    ],
    author="Vadim Tiganov",
    author_email="tiganoviv@gmail.com",
    description="A simple Python tool to generate LaTeX tables",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tiganoviv/pylatextable",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
