from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
from mkdocs.structure.nav import (Navigation, Section, Page)
from titlecase import titlecase


def traverse_navigation(tree):
    if not isinstance(tree, (Navigation, Section)):
        yield tree
    else:
        if isinstance(tree, Navigation):
            for sublist in tree:
                yield from traverse_navigation(sublist)
        elif isinstance(tree, Section):
            yield tree
            for sublist in tree.children:
                yield from traverse_navigation(sublist)


class TitleCasingPlugin(BasePlugin):
    config_scheme = (
        ("capitalization_type", config_options.Type(str, default="title")),
        ("default_page_name", config_options.Type(str, default="Home"))
    )

    def on_nav(self, nav, config, files):
        for descendant in traverse_navigation(nav):
            if isinstance(descendant, (Section, Page)):
                if not(descendant.title):
                    descendant.title = descendant.url.rstrip("/").split(
                        "/")[-1].replace("-", " ").replace("_", " ")
                    if len(descendant.title.replace(" ", "")) == 0:
                        descendant.title = self.config["default_page_name"]

                if self.config["capitalization_type"] == "first_letter":
                    descendant.title = descendant.title.title()
                else:
                    descendant.title = titlecase(descendant.title)
