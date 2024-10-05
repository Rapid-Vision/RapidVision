import bpy
import mathutils

class Camera:
    _camera: bpy.types.Camera
    _camera_obj: bpy.types.Object

    def __init__(self):
        self._camera = bpy.data.cameras.new("Camera")
        self._camera_obj = bpy.data.objects.new("Camera", self._camera)
        bpy.context.collection.objects.link(self._camera_obj)

    def set_position(self, position: mathutils.Vector):
        self._camera_obj.location = position

    def set_rotation(self, rotation: mathutils.Vector | mathutils.Euler | mathutils.Quaternion | list):
        if isinstance(rotation, mathutils.Vector) or isinstance(rotation, list):
            self._camera_obj.rotation_euler = mathutils.Vector(rotation)
        elif isinstance(rotation, mathutils.Euler):
            self._camera_obj.rotation_euler = rotation
        elif isinstance(rotation, mathutils.Quaternion):
            self._camera_obj.rotation_quaternion = rotation

    def look_at(self, target: mathutils.Vector):
        target = mathutils.Vector(target)

        direction = -(target - self._camera_obj.location)
        rot_quat = direction.to_track_quat('Z', 'Y')
        self._camera_obj.rotation_euler = rot_quat.to_euler()

    def set_lens(self, focal_length: float):
        self._camera.lens = focal_length