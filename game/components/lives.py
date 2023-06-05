from game.utils.constants import LIFE


class Life:
    def __init__(self):
        self.life_image = LIFE
        self.life_position = (0, 0)  # Posición inicial de la primera vida
        self.life_spacing = 60  # Separación entre cada vida

    def draw(self, screen, life_counter):
        for i in range(life_counter):
            life_rect = self.life_image.get_rect()
            life_rect.x = self.life_position[0] + i * self.life_spacing
            life_rect.y = self.life_position[1]

            # Controlar la visibilidad de las vidas
            if i < life_counter:
                screen.blit(self.life_image, life_rect)