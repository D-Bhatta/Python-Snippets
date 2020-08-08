from setuptools import find_packages, setup

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="programs",
    version="0.0.1",
    author="D-Bhatta",
    author_email="email",
    description="A collection of short python programs",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/D-Bhatta/Python-Snippets.git",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
