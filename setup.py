from setuptools import setup, find_packages

setup(
    name="PyForShort",
    version="1.0",
    description="A package for creating shortcuts",
    author="Roshan D Roy",
    author_email="roshandeepuroy@gmail.com",
    url="https://github.com/R-D-R248/PyForShort",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        # Add any specific dependencies for creating shortcuts if needed
    ],
    python_requires=">=3.6",
)
