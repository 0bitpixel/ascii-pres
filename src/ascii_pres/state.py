class AppState:
    def __init__(self):
        self.run = True
        self.config = None
        self.slide_number = 0

    def stop_app(self):
        self.run = False

    def update_config(self, config):
        self.config = config

    def increment_slide_number(self):
        self.slide_number += 1

state = AppState()