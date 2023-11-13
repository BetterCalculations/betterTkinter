class Placer:
    def __init__(self, app_width: int, app_height: int):
        self.app_width = app_width
        self.app_height = app_height
        self.not_important = None
        self.margin_center = 90
        self.margin_right = 60

    def get_width(self, positions: list):
        self.not_important = None
        return positions[0]

    def get_height(self, positions: list):
        self.not_important = None
        return positions[1]

    def top_right(self, margin: int = 30):
        # returns a array
        if margin == 30:
            margin = self.margin_right
        return [self.app_width - margin, margin]

    def top_left(self, margin: int = 30):
        # returns a array
        return [self.app_width - self.app_width + margin, margin]

    def top_center(self, margin: int = 30):
        # returns a array
        if margin == 30:
            margin = self.margin_center
        return [self.app_width / 2 - margin, margin]

    def body_left(self, margin: int = 30):
        # returns a array

        return [self.app_width - self.app_width + margin, self.app_height // 2 - margin]

    def body_center(self, margin: int = 30):
        if margin == 30:
            margin = self.margin_center
        # returns a array
        return [self.app_width // 2 - margin, self.app_height // 2 - margin]

    def body_right(self, margin: int = 30):
        # returns a array
        if margin == 30:
            margin = self.margin_right
        return [self.app_width - margin, self.app_height // 2 - margin]

    def footer_center(self, margin: int = 30):
        # returns a array
        if margin == 30:
            margin = self.margin_center
        return [self.app_width - margin // 2, self.app_height - margin]

    def footer_left(self, margin: int = 30):
        # returns a array
        return [self.app_width - self.app_width + margin, self.app_height - margin]

    def footer_right(self, margin: int = 30):
        # returns a array
        if margin == 30:
            margin = self.margin_right
        return [self.app_width - margin, self.app_height - margin]

