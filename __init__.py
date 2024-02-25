bl_info = {
    "name": "Blender2Bevy Scene Editor Plugin",
    "description": "A plugin that extends Blender to allow usage as a scene editor for the Bevy ECS engine.",
    "author": "TGRCDev",
    "version": (0, 1),
    "blender": (4, 0, 0),
    "category": "Game Engine",
}

def register():
    print("Hello World")
def unregister():
    print("Goodbye World")