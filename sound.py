import pygame


class SoundManager:
    def __init__(self):
        self.sounds = {
            'arrow' : pygame.mixer.Sound("sound/arrow_launch.ogg"),
            'birds_attack' : pygame.mixer.Sound("sound/birds_attack.mp3"),
            'bg_sound' : pygame.mixer.Sound("sound/birds_in_forest.ogg")

        }

    def play(self, name):
        self.sounds[name].play()