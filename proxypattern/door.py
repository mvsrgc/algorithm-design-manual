class Door:
    def open_method(self) -> None:
        pass

class SecuredDoor:
    def __init__(self) -> None:
        self._klass = Door

    def open_method(self) -> None:
        print(f"Adding security measures to method of {self._klass}.")