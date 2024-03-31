class AppState:
    def __init__(self) -> None:
        self.is_authenticated = False

    def authenticate(self):
        self.is_authenticated = True

    def deauthenticate(self):
        self.is_authenticated = False