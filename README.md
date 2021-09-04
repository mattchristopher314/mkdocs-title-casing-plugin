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
  - title-casing
```

> If this is the first `plugins` entry that you are adding, you should probably also add `search` as this is enabled by default.

## Usage

When the plugin is enabled, all section and page titles will be converted to use Title Case. For example, `War and peace` becomes `War and Peace`.

### Configuration

* `capitalization_type` (string)
  * `title` - default - gives `War and Peace`.
  * `first_letter` - gives `War And Peace`.
* `default_page_name` (string). The page name to use when it cannot be determined automatically. Default is `Home`.

#### Example mkdocs.yml

```yml
plugins:
  - search
  - title-casing:
      capitalization_type: first_letter
      default_page_name: Index
```
