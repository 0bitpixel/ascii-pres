class AppState:
    def __init__(self):
        # fixed once initialized
        self.working_directory = None
        self.config = None
        self.total_slides = 0

        # mutable at runtime
        self.run = True
        self.current_slide = 0

    def current_slide_exists(self):
        return self.current_slide <= self.total_slides

state = AppState()