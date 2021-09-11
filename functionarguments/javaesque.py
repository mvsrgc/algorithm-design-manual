class Menu:
    def __init__(self, config: dict):
        self.title = config["title"]
        self.body = config["body"]


menu = Menu({"title": "Title", "body": "Body"})
