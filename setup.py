import setuptools
with open("README.md", "r") as fh:
 long_description = fh.read()  
setuptools.setup(
 name="trello-futter-krot", version="0.0.1", author="futter", author_email="futterbeta@gmail.com",
description="Trello-client-server", long_description=long_description, long_description_content_type="text/markdown",
url="https://github.com/futter-krot/Trello.futter-krot.io", packages=setuptools.find_packages(), classifiers=[ "Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License", "Operating System :: OS Independent", ], python_requires='>=3.6',)