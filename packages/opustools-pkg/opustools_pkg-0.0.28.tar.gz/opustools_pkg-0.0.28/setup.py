import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="opustools_pkg",
    version="0.0.28",
    author="Mikko Aulamo",
    author_email="mikko.aulamo@helsinki.fi",
    description="Tools to read OPUS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url="https://github.com/pypa/example-project",
    packages=setuptools.find_packages(),
    scripts=["bin/opus_read", "bin/opus_cat", "bin/opus_get",
        "bin/add_lang_ids"],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
