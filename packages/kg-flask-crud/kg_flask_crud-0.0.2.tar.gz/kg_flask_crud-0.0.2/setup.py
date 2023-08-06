import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kg_flask_crud",
    version="0.0.2",
    author="Keoni Gandall",
    author_email="koeng101@gmail.com",
    description="An opinionated library to quickly create Flask CRUD interfaces",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

