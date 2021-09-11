from typing import Text


class MenuConfig:
    title: Text
    body: Text
    button_text: Text
    cancellable: bool = False


def create_menu(config: MenuConfig) -> None:
    title = config.title
    body = config.body
    button_text = config.button_text
    cancellable = config.cancellable


config = MenuConfig()

config.title = "My delicious menu"
config.body = "A description of the various items on the menu"
config.button_text = "Order now!"
# The instance attribute overrides the default class attribute.
config.cancellable = True

create_menu(config)
