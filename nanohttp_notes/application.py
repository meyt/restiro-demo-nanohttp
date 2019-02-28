from nanohttp import Application
from .controllers import RootController


class DemoApplication(Application):

    def __init__(self):
        super().__init__(root=RootController())


app = DemoApplication()
