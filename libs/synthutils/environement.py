import bpy
import mathutils

class Environement:

    world: bpy.types.World
    background_node: bpy.types.ShaderNodeBackground
    texture_node: bpy.types.ShaderNodeTexEnvironment
    mapping_node: bpy.types.ShaderNodeMapping

    def __init__(self, filename: str = None):
        self.world = bpy.data.worlds.new("World")
        self.world.use_nodes = True

        self.background_node = self.world.node_tree.nodes['Background']

        self.texture_node = self.world.node_tree.nodes.new('ShaderNodeTexEnvironment')
        self.world.node_tree.links.new(self.background_node.inputs['Color'], self.texture_node.outputs['Color'])

        self.mapping_node = self.world.node_tree.nodes.new('ShaderNodeMapping')
        self.mapping_node.vector_type = 'VECTOR'
        self.world.node_tree.links.new(self.texture_node.inputs['Vector'], self.mapping_node.outputs['Vector'])       

        tex_coord_node = self.world.node_tree.nodes.new('ShaderNodeTexCoord')
        self.world.node_tree.links.new(self.mapping_node.inputs['Vector'], tex_coord_node.outputs['Generated'])

        if filename is not None:
            self.set_image(filename)

    def set_image(self, filename: str):
        self.texture_node.image = bpy.data.images.load(filename)

    def set_rotation(self, rotation: mathutils.Vector):
        self.mapping_node.inputs['Rotation'].default_value = rotation

    def set_strength(self, strength: float):
        self.background_node.inputs['Strength'].default_value = strength
