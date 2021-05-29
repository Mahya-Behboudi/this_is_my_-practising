class QueenSprite:

    def __init__(self, img, target_posn):
        self.image = img
        self.target_posn = target_posn
        (x, y) = target_posn
        self.posn = (x, 0)     # Start ball at top of its column
        self.y_velocity = 0    #    with zero initial velocity

    def update(self):
        self.y_velocity += gravity       # Gravity changes velocity
        (x, y) = self.posn
        new_y_pos = y + self.y_velocity  # Velocity moves the ball
        self.posn = (x, new_y_pos)       #   to this new position.

    def draw(self, target_surface):      # Same as before.
        target_surface.blit(self.image, self.posn)
    def contain_point(self,pt):
        """ return true if my sprite rectangule contain the point"""
        (my_x,my_y) = self.posn
        my_width = self.image.get_width()
        my_height =  self.image.get_height()
        (x,y)= pt
        return (x>= my_x and x<my_x+my_width and y>=my_y and y<my_y +my_height)