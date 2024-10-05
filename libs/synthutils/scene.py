import bpy
import mathutils

from .camera import *
from .utils import *
from .environement import *

class Scene:
    def __init__(self, resolution=(640, 640), time_limit = 1):
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete()

        bpy.context.scene.render.engine = 'CYCLES'
        bpy.context.scene.cycles.device = 'GPU'
        bpy.context.scene.render.resolution_x = resolution[0]
        bpy.context.scene.render.resolution_y = resolution[1]

        bpy.context.scene.cycles.time_limit = time_limit

        update_view_layer()

    def set_camera(self, camera: Camera):
        bpy.context.scene.camera = camera._camera_obj

        return camera
    
    def set_environement(self, env: Environement):
        bpy.context.scene.world = env.world

    def render(self, dir: str, filename: str):
        """
        Renders an image using Blender's rendering engine and saves it to the specified directory.
        Args:
            dir (str): The directory where the rendered image will be saved.
            filename (str): The name of the file (without extension) to save the rendered image as.
        Returns:
            None
        """
        print(f'Rendering {filename}')
        update_view_layer()
        
        fp = f'{dir}/{filename}.png'
        bpy.ops.render.render(write_still=True)
        bpy.data.images['Render Result'].save_render(filepath = fp)