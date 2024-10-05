import bpy
import mathutils

from .utils import *

class Object:
    _object: bpy.types.Object

    def __init__(self, filename: str, name: str):
        self._object = append_object_from_blend(filename, name)

    def set_position(self, position: list):
        self._object.location = mathutils.Vector(position)

    def rotate_x(self, angle: float):
        self._object.rotation_euler.x = angle
    
    def rotate_y(self, angle: float):
        self._object.rotation_euler.y = angle

    def rotate_z(self, angle: float):
        self._object.rotation_euler.z = angle

    def set_property(self, property_name: str, value):
        self._object[property_name] = value
