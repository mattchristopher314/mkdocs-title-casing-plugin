![PyPI](https://img.shields.io/pypi/v/mkdocs-title-casing-plugin)
![PyPI - License](https://img.shields.io/pypi/l/mkdocs-title-casing-plugin)

# mkdocs-title-casing-plugin
A lightweight mkdocs plugin to add title casing to all mkdocs pages and sections.
Uses [python-titlecase](https://github.com/ppannuto/python-titlecase) for formatting.

## Setup

Install the plugin using pip:

```bash
pip install mkdocs-title-casing-plugin
```

Include the plugin in `mkdocs.yml`. For example:

```yml
plugins:
  - search
  - git-authors
```

> If this is the first `plugins` entry that you are adding, you should probably also add `search` as this is enabled by default.

## Usage

When the plugin is enabled, all section and page titles will be converted to use Title Case. For example, `War and peace` becomes `War and Peace`.
