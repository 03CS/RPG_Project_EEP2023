#game setup
WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 64
HITBOX_OFFSET = {
    'player': -26,
    'object': -40,
    'grass': -10,
    'invisible': 0
}

#menu info
START_TEXT = 'A RPG Is Amongst Us'
START_COLOR = 'white'
START_CHAR = 'Selected Character:'
DEATH_TEXT = 'GAME OVER'
DEATH_COLOR = 'red'
MENU_FONT_SIZE = 50

#ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = 'graphics/font/joystix.ttf'
UI_FONT_SIZE = 18
MENU_SCREEN = 'graphics/bg/menu_screen.png'
DEATH_SCREEN = 'graphics/bg/death_screen.png'

#character cards
KNIGHT_CARD = 'graphics/character_cards/knight.png'
PRINCESS_CARD = 'graphics/character_cards/princess.png'
NINJA_CARD = 'graphics/character_cards/ninja.png'
SKELETON_CARD = 'graphics/character_cards/skeleton.png'
SAMURAI_CARD = 'graphics/character_cards/samurai.png'
ESKIMO_CARD = 'graphics/character_cards/eskimo.png'
LION_CARD = 'graphics/character_cards/lion.png'
MAGE_CARD = 'graphics/character_cards/mage.png'
MASTER_CARD = 'graphics/character_cards/master.png'
MONK_CARD = 'graphics/character_cards/monk.png'
SORCERER_CARD = 'graphics/character_cards/sorcerer.png'
OLD_MAN_CARD = 'graphics/character_cards/old_man.png'

#general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

#ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

#upgrade menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

#weapons
weapon_data = {
    'sword': {'cooldown': 500, 'damage': 15, 'graphic': 'graphics/weapons/sword/full.png'},
    'lance': {'cooldown': 1000, 'damage': 30, 'graphic': 'graphics/weapons/lance/full.png'},
    'axe': {'cooldown': 700, 'damage': 20, 'graphic': 'graphics/weapons/axe/full.png'},
    'rapier': {'cooldown': 300, 'damage': 8, 'graphic': 'graphics/weapons/rapier/full.png'},
    'sai': {'cooldown': 400, 'damage': 10, 'graphic': 'graphics/weapons/sai/full.png'}
}

#magic
magic_data = {
    'flame': {'strength': 5, 'cost': 50, 'graphic': 'graphics/particles/flame/fire.png'},
    'heal': {'strength': 10, 'cost': 30, 'graphic': 'graphics/particles/heal/heal.png'}
}

#enemy
monster_data = {
    'axoltol_blue': {'health': 150, 'exp': 60, 'attack_damage': 12, 'attack_type': 'slash', 'attack_sound': 'audio/attack/slash.mp3', 'speed': 3.3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 250},
    'axoltol_orange': {'health': 150, 'exp': 60, 'attack_damage': 12, 'attack_type': 'slash', 'attack_sound': 'audio/attack/slash.mp3', 'speed': 3.3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 250},
    'bamboo_green': {'health': 100, 'exp': 20, 'attack_damage': 6, 'attack_type': 'plant_green', 'attack_sound': 'audio/attack/cut.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 200},
    'bamboo_yellow': {'health': 100, 'exp': 20, 'attack_damage': 6, 'attack_type': 'plant_yellow', 'attack_sound': 'audio/attack/cut.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 200},
    'cyclops_green': {'health': 250, 'exp': 80, 'attack_damage': 15, 'attack_type': 'slash_double', 'attack_sound': 'audio/attack/slash.mp3', 'speed': 2.5, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 150},
    'cyclops_red': {'health': 250, 'exp': 80, 'attack_damage': 15, 'attack_type': 'slash_double', 'attack_sound': 'audio/attack/slash.mp3', 'speed': 2.5, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 150},
    'larva_blue': {'health': 30, 'exp': 10, 'attack_damage': 5, 'attack_type': 'circle', 'attack_sound': 'audio/attack/slime.mp3', 'speed': 2, 'resistance': 3, 'attack_radius': 30, 'notice_radius': 150},
    'larva_green': {'health': 30, 'exp': 10, 'attack_damage': 5, 'attack_type': 'circle', 'attack_sound': 'audio/attack/slime.mp3', 'speed': 2, 'resistance': 3, 'attack_radius': 30, 'notice_radius': 150},
    'mushroom_blue': {'health': 60, 'exp': 15, 'attack_damage': 8, 'attack_type': 'cut', 'attack_sound': 'audio/attack/cut.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 40, 'notice_radius': 180},
    'mushroom_red': {'health': 60, 'exp': 15, 'attack_damage': 8, 'attack_type': 'cut', 'attack_sound': 'audio/attack/cut.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 40, 'notice_radius': 180},
    'reptile_blue': {'health': 250, 'exp': 100, 'attack_damage': 18, 'attack_type': 'claw', 'attack_sound': 'audio/attack/claw.wav', 'speed': 3.8, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 260},
    'reptile_green': {'health': 250, 'exp': 100, 'attack_damage': 18, 'attack_type': 'claw', 'attack_sound': 'audio/attack/claw.wav', 'speed': 3.8, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 260},
    'skull_blue': {'health': 160, 'exp': 80, 'attack_damage': 14, 'attack_type': 'spirit_double', 'attack_sound': 'audio/attack/fireball.wav', 'speed': 3.2, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 200},
    'skull_red': {'health': 160, 'exp': 80, 'attack_damage': 14, 'attack_type': 'fire_attack', 'attack_sound': 'audio/attack/fireball.wav', 'speed': 3.2, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 200},
    'slime_blue': {'health': 120, 'exp': 40, 'attack_damage': 10, 'attack_type': 'wave_blue', 'attack_sound': 'audio/attack/slime.mp3', 'speed': 2.4, 'resistance': 3, 'attack_radius': 40, 'notice_radius': 160},
    'slime_green': {'health': 120, 'exp': 40, 'attack_damage': 10, 'attack_type': 'wave_green', 'attack_sound': 'audio/attack/slime.mp3', 'speed': 2.4, 'resistance': 3, 'attack_radius': 40, 'notice_radius': 160},
    'spirit_red': {'health': 140, 'exp': 60, 'attack_damage': 12, 'attack_type': 'spirit_red', 'attack_sound': 'audio/attack/fireball.wav', 'speed': 3.6, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 220},
    'spirit_white': {'health': 140, 'exp': 60, 'attack_damage': 12, 'attack_type': 'spirit_blue', 'attack_sound': 'audio/attack/fireball.wav', 'speed': 3.6, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 220},
    'giant_flame': {'health': 350, 'exp': 200, 'attack_damage': 35, 'attack_type': 'thunder', 'attack_sound': 'audio/attack/fireball_2.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 200},
    'giant_frog': {'health': 400, 'exp': 300, 'attack_damage': 40, 'attack_type': 'slash_circle', 'attack_sound': 'audio/attack/chomp.wav', 'speed': 3.2, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 250},
    'giant_raccoon': {'health': 600, 'exp': 600, 'attack_damage': 50, 'attack_type': 'claw_double', 'attack_sound': 'audio/attack/claw.wav', 'speed': 3.4, 'resistance': 3, 'attack_radius': 100, 'notice_radius': 300},
    'giant_spirit': {'health': 300, 'exp': 150, 'attack_damage': 25, 'attack_type': 'ice', 'attack_sound': 'audio/attack/ice.mp3', 'speed': 3, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 200},
    'demon_cyclops': {'health': 400, 'exp': 400, 'attack_damage': 45, 'attack_type': 'rock', 'attack_sound': 'audio/attack/explosion.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 200}
}