import pygame
from support import import_folder
from random import choice

class AnimationPlayer():
    def __init__(self):
        self.frames = {
            #magic
            'flame': import_folder('graphics/particles/flame/frames'),
            'aura': import_folder('graphics/particles/aura_green'),
            'heal': import_folder('graphics/particles/heal/frames'),
            
            #attacks 
            'cut': import_folder('graphics/particles/cut'),
            'circle': import_folder('graphics/particles/circle'),
            'slash': import_folder('graphics/particles/slash'),
            'slash_circle': import_folder('graphics/particles/slash_circle'),
            'slash_double': import_folder('graphics/particles/slash_double'),
            'plant_green': import_folder('graphics/particles/plant_green'),
            'plant_yellow': import_folder('graphics/particles/plant_yellow'),
            'spirit_blue': import_folder('graphics/particles/spirit_blue'),
            'spirit_red': import_folder('graphics/particles/spirit_red'),
            'spirit_double': import_folder('graphics/particles/spirit_double'),
            'wave_blue': import_folder('graphics/particles/wave_blue'),
            'wave_green': import_folder('graphics/particles/wave_green'),
            'claw': import_folder('graphics/particles/claw'),
            'claw_double': import_folder('graphics/particles/claw_double'),
            'fire_attack': import_folder('graphics/particles/fire_attack'),
            'ice': import_folder('graphics/particles/ice'),
            'rock': import_folder('graphics/particles/rock'),
            'thunder': import_folder('graphics/particles/thunder'),
            
            #'sparkle': import_folder('graphics/particles/sparkle'),
            #'leaf_attack': import_folder('graphics/particles/leaf_attack'),

            #monster deaths
            'axoltol_orange': import_folder('graphics/particles/smoke_orange'),
            'axoltol_blue': import_folder('graphics/particles/smoke_blue'),
            'bamboo_green': import_folder('graphics/particles/bamboo_green'),
            'bamboo_yellow': import_folder('graphics/particles/bamboo_yellow'),
            'cyclops_green': import_folder('graphics/particles/smoke_green'),
            'cyclops_red': import_folder('graphics/particles/smoke_red'),
            'larva_blue': import_folder('graphics/particles/aura_blue'),
            'larva_green': import_folder('graphics/particles/aura_green'),
            'mushroom_blue': import_folder('graphics/particles/smoke_blue'),
            'mushroom_red': import_folder('graphics/particles/smoke_red'),
            'reptile_blue': import_folder('graphics/particles/smoke_blue'),
            'reptile_green': import_folder('graphics/particles/smoke_green'),
            'skull_blue': import_folder('graphics/particles/sparkle'),
            'skull_red': import_folder('graphics/particles/sparkle'),
            'slime_blue': import_folder('graphics/particles/aura_blue'),
            'slime_green': import_folder('graphics/particles/aura_green'),
            'spirit_red': import_folder('graphics/particles/sparkle'),
            'spirit_white': import_folder('graphics/particles/sparkle'),
            'giant_flame': import_folder('graphics/particles/nova'),
            'giant_frog': import_folder('graphics/particles/aura_green'),
            'giant_raccoon': import_folder('graphics/particles/raccoon'),
            'giant_spirit': import_folder('graphics/particles/nova'),
            'demon_cyclops': import_folder('graphics/particles/smoke_red'),

            #leaves 
            'leaf': (
                import_folder('graphics/particles/leaf1'),
                import_folder('graphics/particles/leaf2'),
                import_folder('graphics/particles/leaf3'),
                import_folder('graphics/particles/leaf4'),
                import_folder('graphics/particles/leaf5'),
                import_folder('graphics/particles/leaf6'),
                self.reflect_images(import_folder('graphics/particles/leaf1')),
                self.reflect_images(import_folder('graphics/particles/leaf2')),
                self.reflect_images(import_folder('graphics/particles/leaf3')),
                self.reflect_images(import_folder('graphics/particles/leaf4')),
                self.reflect_images(import_folder('graphics/particles/leaf5')),
                self.reflect_images(import_folder('graphics/particles/leaf6'))
            )
        }

    def reflect_images(self, frames):
        new_frames = []
        for frame in frames:
            flipped_frame = pygame.transform.flip(frame, True, False)
            new_frames.append(flipped_frame)
        return new_frames

    def create_grass_particles(self, pos, groups):
        animation_frames = choice(self.frames['leaf'])
        ParticleEffect(pos, animation_frames, groups)

    def create_particles(self, animation_type, pos, groups):
        animation_frames = self.frames[animation_type]
        ParticleEffect(pos, animation_frames, groups)

class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, pos, animation_frames, groups):
        super().__init__(groups)
        self.sprite_type = 'magic'
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()
