import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="radarreader-omarimran2000",
    version="0.0.7",
    author="Omar Imran",
    author_email="omarimran@cmail.carleton.ca",
    description="Convert .dat file into a CSV file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/omarimran2000/radarreader",
    packages=['radarreader'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={'': ['radarreader/xethru_datafloat_20190614_141837.dat']},
    include_package_data=True,
    install_requires=[],
)
