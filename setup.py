import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="em-driver",  # Replace with your own username
    version="0.0.4",
    author="Elvis Moraa",
    author_email="elvismoraa2@gmail.com",
    description="A simple library to help you read, write and update SQLite3 databases",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elvisAR-git/em-driver",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
