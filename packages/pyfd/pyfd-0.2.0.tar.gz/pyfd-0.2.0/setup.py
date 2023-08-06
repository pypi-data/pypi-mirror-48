import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyfd",
    version="0.2.0",
    author="Tim Sessanna",
    author_email="timothy.sessanna@dish.com",
    description="A Python wrapper for the Freshdesk API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dish-freshdesk/pyfd",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)