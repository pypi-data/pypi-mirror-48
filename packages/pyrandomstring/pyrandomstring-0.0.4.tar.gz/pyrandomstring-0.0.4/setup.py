import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "pyrandomstring",
    version = "0.0.4",
    author = "Lakhya Jyoti Nath (ljnath)",
    author_email = "ljnath@ljnath.com",
    description = "PyRandomString is a python library to generate N random list of string of M length. Ofcourse you can configure N and M",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/ljnath/PyRandomString",
    packages = setuptools.find_packages(),
    license='MIT',
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)