from typing import Text
from dataclasses import astuple, dataclass


@dataclass
class MenuConfig:
    title: Text
    body: Text
    button_text: Text
    cancellable: bool = False


def create_menu(config: MenuConfig):
    title, body, button_text, cancellable = astuple(config)


create_menu(
    MenuConfig(
        title="Delicious Menu",
        body="A description.",
        button_text="Order now!",
    )
)
