class Door:
    def open_method(self) -> None:
        print("hi")

class SecuredDoor:
    def __init__(self) -> None:
        self._klass = Door()

    def open_method(self) -> None:
        print(f"Adding security measures to method of {self._klass}.")
        self._klass.open_method()

if __name__ == "__main__":
    secured_door = SecuredDoor()
    secured_door.open_method()