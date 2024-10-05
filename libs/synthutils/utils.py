import bpy
import mathutils

def update_view_layer():
    bpy.context.view_layer.update()

def append_object_from_blend(filepath: str, object_name: str):
    """
    Appends an object from an external .blend file into the current scene.
    
    :param filepath: The full path to the .blend file.
    :param object_name: The name of the object to append from the .blend file.
    """
    with bpy.data.libraries.load(filepath, link=False) as (data_from, data_to):
        if object_name in data_from.objects:
            data_to.objects.append(object_name)
        else:
            print(f"Object {object_name} not found in {filepath}")
            return

    # Link the object to the current scene
    for obj in data_to.objects:
        if obj is not None:
            bpy.context.collection.objects.link(obj)
            print(f"Appended {object_name} and linked it to the scene")
            return obj
        else:
            print(f"Failed to append object {object_name} from {filepath}")

def world_to_screen(world_coordinates: mathutils.Vector, camera: bpy.types.Object) -> mathutils.Vector:
    """
    Converts world coordinates to screen coordinates in respect to the specified camera.
    Args:
        world_coordinates (mathutils.Vector): The coordinates in the world space.
        camera (bpy.types.Object): The camera object used for the projection.
    Returns:
        mathutils.Vector: The screen coordinates corresponding to the input world coordinates.
    """
    update_view_layer()
    scene = bpy.context.scene
    
    # Calculate the projection matrix of the camera
    cam_matrix = camera.matrix_world.normalized().inverted()
    persp_matrix = camera.calc_matrix_camera(
        bpy.context.evaluated_depsgraph_get(), x=scene.render.resolution_x, y=scene.render.resolution_y)
    
    # World to camera space
    vec_cam = cam_matrix @ world_coordinates
    
    # Camera space to normalized device coordinates (NDC)
    vec_ndc = persp_matrix @ vec_cam
    
    # Homogeneous divide to get normalized device coordinates
    vec_ndc /= vec_ndc.z
    
    # Convert NDC to screen space
    screen_x = (vec_ndc.x + 1) * 0.5
    screen_y = (1 - vec_ndc.y) * 0.5
    
    return mathutils.Vector([screen_x, screen_y])
