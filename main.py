import pygame, sys
from settings import *
from level import Level
from button import Button
from player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.playing = False
        self.in_menu = True
        self.death_menu_active = False
        self.current_player_character = 'knight'

        #font
        self.font = pygame.font.Font(UI_FONT, MENU_FONT_SIZE)

        #sound
        self.main_sound = pygame.mixer.Sound('audio/music/main.ogg')
        self.main_sound.set_volume(0.1)
        self.menu_sound = pygame.mixer.Sound('audio/music/menu.mp3')
        self.menu_sound.set_volume(0.1)
        self.dead_sound = pygame.mixer.Sound('audio/music/dead.mp3')
        self.dead_sound.set_volume(0.1)

        #menu sounds
        self.select_sound = pygame.mixer.Sound('audio/selection/select.wav')
        self.select_sound.set_volume(1)
        self.play_sound = pygame.mixer.Sound('audio/selection/accept.wav')
        self.play_sound.set_volume(0.5)

        self.skeleton_select = pygame.mixer.Sound('audio/selection/skeleton_select.mp3')
        self.skeleton_select.set_volume(2)
        self.ninja_select = pygame.mixer.Sound('audio/selection/ninja_select.mp3')
        self.ninja_select.set_volume(2)

        self.menu_sound.play(loops = -1)

        #buttons
        self.play_button = Button('PLAY', 200, 40, (530, 320), 6, None)
        self.quit_button = Button('QUIT', 200, 40, (530, 400), 6, None)
        self.retry_button = Button('RETRY', 200, 40, (530, 320), 6, None)

        #character selection
        self.knight_button = Button('KNIGHT', 90, 90, (50, 200), 6, KNIGHT_CARD)
        self.princess_button = Button('PRINCESS', 90, 90, (200, 200), 6, PRINCESS_CARD)
        self.ninja_button = Button('NINJA', 90, 90, (50, 350), 6, NINJA_CARD)
        self.samurai_button = Button('SAMURAI', 90, 90, (200, 350), 6, SAMURAI_CARD)
        self.master_button = Button('MASTER', 90, 90, (50, 500), 6, MASTER_CARD)
        self.monk_button = Button('MONK', 90, 90, (200, 500), 6, MONK_CARD)

        self.sorcerer_button = Button('SORCERER', 90, 90, (1000, 200), 6, SORCERER_CARD)
        self.mage_button = Button('MAGE', 90, 90, (1150, 200), 6, MAGE_CARD)
        self.eskimo_button = Button('ESKIMO', 90, 90, (1000, 350), 6, ESKIMO_CARD)
        self.old_man_button = Button('OLD MAN', 90, 90, (1150, 350), 6, OLD_MAN_CARD)
        self.lion_button = Button('LION', 90, 90, (1000, 500), 6, LION_CARD)
        self.skeleton_button = Button('SKELETON', 90, 90, (1150, 500), 6, SKELETON_CARD)
        
    def play_music(self, sound):
        if self.music_playing is not None:
            self.music_playing.stop()
        sound.play(loops = -1)
        self.music_playing = sound

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if self.in_menu:
                self.handle_menu_events(event)
            elif self.playing:
                self.handle_game_events(event)
            if self.level.dead:
                self.handle_death_menu_events(event)

    def handle_menu_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.knight_button.check_click():
                self.current_player_character = 'knight'
                self.select_sound.play()
            if self.princess_button.check_click():
                self.current_player_character = 'princess'
                self.select_sound.play()
            if self.ninja_button.check_click():
                self.current_player_character = 'ninja'
                self.ninja_select.play()
            if self.skeleton_button.check_click():
                self.current_player_character = 'skeleton'
                self.skeleton_select.play()
            if self.samurai_button.check_click():
                self.current_player_character = 'samurai'
                self.select_sound.play()
            if self.master_button.check_click():
                self.current_player_character = 'master'
                self.select_sound.play()
            if self.monk_button.check_click():
                self.current_player_character = 'monk'
                self.select_sound.play()
            if self.sorcerer_button.check_click():
                self.current_player_character = 'sorcerer'
                self.select_sound.play()
            if self.mage_button.check_click():
                self.current_player_character = 'mage'
                self.select_sound.play()
            if self.eskimo_button.check_click():
                self.current_player_character = 'eskimo'
                self.select_sound.play()
            if self.lion_button.check_click():
                self.current_player_character = 'lion'
                self.select_sound.play()
            if self.old_man_button.check_click():
                self.current_player_character = 'old man'
                self.select_sound.play()

            if self.play_button.check_click():
                self.level = Level()
                self.level.player.import_player_assets(self.current_player_character)
                self.in_menu = False
                self.playing = True

                self.play_sound.play()
                self.menu_sound.stop()

                self.play_music(self.main_sound)
                pygame.display.set_caption("Game")
            if self.quit_button.check_click():
                pygame.quit()
                sys.exit()

    def handle_game_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                self.level.toggle_menu()

    def handle_death_menu_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.retry_button.check_click():
                self.level.dead = False
                self.death_menu_active = False
                self.in_menu = True

                self.play_sound.play()
                self.dead_sound.stop()

                self.play_music(self.menu_sound)
                pygame.display.set_caption("Menu")
            if self.quit_button.check_click():
                pygame.quit()
                sys.exit()

    def draw_text(self, text, font, color, x, y):
        menu_text = font.render(text, True, color)
        text_rect = menu_text.get_rect(center = (x, y))
        self.screen.blit(menu_text, text_rect)

    def render_selected_character_text(self):
        text = f"Selected Character: {self.current_player_character.capitalize()}"
        text_surface = self.font.render(text, True, START_COLOR)
        text_rect = text_surface.get_rect(center = (WIDTH // 2, HEIGHT - 50))
        self.screen.blit(text_surface, text_rect)

    def run(self):
        self.music_playing = None
        while True:
            self.handle_events()
            self.screen.fill(WATER_COLOR)

            if self.in_menu:
                self.main_menu()
            elif self.playing:
                if not self.level.dead:
                    self.level.run()
            if self.level.dead:
                self.death_menu()

            pygame.display.update()
            self.clock.tick(FPS)

    def main_menu(self):
        pygame.display.set_caption("Menu")
        BG = pygame.image.load(MENU_SCREEN).convert()
       
        self.screen.blit(BG, (0, 0))
        self.draw_text(START_TEXT, self.font, START_COLOR, 620, 50)
        self.render_selected_character_text()
        
        #character buttons
        self.knight_button.draw()
        self.princess_button.draw()
        self.ninja_button.draw()
        self.samurai_button.draw()
        self.master_button.draw()
        self.monk_button.draw()
        self.sorcerer_button.draw()
        self.mage_button.draw()
        self.eskimo_button.draw()
        self.old_man_button.draw()
        self.lion_button.draw()
        self.skeleton_button.draw()

        self.play_button.draw()
        self.quit_button.draw()
        pygame.display.update()

    def death_menu(self):
        if not self.death_menu_active:
            self.playing = False
            self.play_music(self.dead_sound)

        pygame.display.set_caption("Game Over")
        BG = pygame.image.load(DEATH_SCREEN).convert()


        self.screen.blit(BG, (0, 0))
        self.draw_text(DEATH_TEXT, self.font, DEATH_COLOR, 620, 150)

        self.retry_button.draw()
        self.quit_button.draw()
        pygame.display.update()

        self.death_menu_active = True

    def play(self):
        self.level = Level()
        self.playing = True

if __name__ == '__main__':
    game = Game()
    game.run()