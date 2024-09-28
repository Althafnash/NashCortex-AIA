from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

def Minecraft():
    print("--------------------------------------------------------------")
    print("YOU CAN PRACTICE MINECRAFT HERE")
    print("build using the code in github/ursina")
    print("left click to create a cube")
    print("right click to destroy a cube")
    print("CREATED BY MOHAMMED ALTHAF")
    print("IF YOU WANT TO EXIT PRESS CTRL+SHIFT+Q")
    print("----------------------------------------------------------------")

    app = Ursina()
    window.size = (1920, 1080) 
    window.fps_counter.enabled = False
    window.exit_button.visible = False
    global block_pick
    block_pick = 1 

    def update():
        global block_pick

        if held_keys['1']: 
            block_pick = 1 
            print("Block picked: Grass")
        if held_keys['2']: 
            block_pick = 2 
            print("Block picked: Stone")
        if held_keys['3']: 
            block_pick = 3 
            print("Block picked: Brick")
        if held_keys['4']: 
            block_pick = 4 
            print("Block picked: Dirt")

    grass_texture = load_texture('assets/grass_block.png')
    brick_texture = load_texture('assets/brick_block.png')
    stone_texture = load_texture('assets/stone_block.png')
    dirt_texture = load_texture('assets/dirt_block.png')

    class Voxel(Button):
        def __init__(self, position=(0, 0, 0), texture=grass_texture):
            super().__init__(
                parent=scene,
                position=position,
                model='assets/block',
                origin_y=.6,
                texture=texture,
                color=color.white,
                scale=0.5
            )

        def input(self, key):
            if self.hovered:
                if key == 'left mouse down':
                    if block_pick == 1:
                        voxel = Voxel(position=self.position + mouse.normal, texture=grass_texture)
                    elif block_pick == 2:
                        voxel = Voxel(position=self.position + mouse.normal, texture=stone_texture)
                    elif block_pick == 3:
                        voxel = Voxel(position=self.position + mouse.normal, texture=brick_texture)
                    elif block_pick == 4:
                        voxel = Voxel(position=self.position + mouse.normal, texture=dirt_texture)
                if key == 'right mouse down':
                    destroy(self)

    for z in range(20):
        for x in range(20):
            voxel = Voxel(position=(x, 0, z))

    player = FirstPersonController()
    app.run()

print("------------------------IGNORE THIS THING S***T--------------------------------------")

