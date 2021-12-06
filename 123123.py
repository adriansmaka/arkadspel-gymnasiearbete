class Enemy:
    def __init__(self):
        self.x = random.randint(0, 476)
        self.y = 20
        self.moveX = 0.2
        self.moveY = 40
        
    def move(self):
        self.x += self.moveX 

        if self.y >= 476:
            self.y = 476
            self.moveY = 0
            self.moveX = 0

        if self.x <= 0:
            self.moveX = 0.2
            self.y += self.moveY
        elif self.x >= 465:
            self.moveX = -0.2
            self.y += self.moveY

    def draw(self):
        screen.blit(nme_img, (self.x, self.y))