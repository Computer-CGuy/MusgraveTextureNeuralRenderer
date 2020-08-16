import bpy
import random
from random import randint
import pickle	
bpy.context.scene.render.engine = 'CYCLES'

bpy.ops.object.delete(use_global=False)
bpy.ops.wm.open_mainfile(filepath="Renderer.blend")
l = []

random.seed(50)

for i in range(0,5,1):
    a,b,c,d,e = randint(0,3),randint(0,10),randint(1,4),randint(0,3),randint(0,3)
    bpy.data.materials["Drop"].node_tree.nodes["Musgrave Texture"].inputs[1].default_value = a
    bpy.data.materials["Drop"].node_tree.nodes["Musgrave Texture"].inputs[2].default_value = b
    bpy.data.materials["Drop"].node_tree.nodes["Musgrave Texture"].inputs[3].default_value = c
    bpy.data.materials["Drop"].node_tree.nodes["Musgrave Texture"].inputs[4].default_value = d
    bpy.data.materials["Drop"].node_tree.nodes["Musgrave Texture"].inputs[5].default_value = e
    l.append([a,b,c,d,e])
    bpy.context.scene.render.image_settings.file_format='JPEG'
    bpy.context.scene.render.filepath = "C:/Users/My PC/Desktop/Python/NeuralRenderer/MusgraveTextureNeuralRenderer/Generator/pic%0.2d.jpg"%i
    bpy.ops.render.render(use_viewport = True, write_still=True)
    with open("out.pkl","wb") as f:
        pickle.dump(l,f)
#    #bpy.data.objects.remove(ob,do_unlink=True)

