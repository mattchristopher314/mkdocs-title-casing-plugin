from setuptools import find_packages, setup

file = open("README.md", "r")
LONG_DESCRIPTION = file.read()
file.close()

setup(
    name="mkdocs-title-casing-plugin",
    description="A lightweight mkdocs plugin to add title casing to all mkdocs pages and sections",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    keywords="mkdocs title case casing plugin",
    url="https://github.com/Rusty3141/mkdocs-title-casing-plugin",
    author="Rusty3141",
    version="0.1.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "mkdocs>=1.0",
        "titlecase>=2.3"
    ],
    license="GPLv3",
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "mkdocs.plugins": [
            "title-casing = mkdocs_title_casing_plugin.plugin:TitleCasingPlugin"
        ]
    },
)
