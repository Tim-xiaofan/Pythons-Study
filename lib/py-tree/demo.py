# coding=utf-8
from Tree.core import Tree
from math import radians as rad
from PIL import Image
 
branches = (
    (.5, rad(-30)),
    (.6, rad(30)),
    (.4, rad(60))
)#元组的个数是每个节点的分支数，这里为3
 
def main():
    tree = Tree(pos=(0, 0, 0, -500), branches=branches)
    tree.grow(3)
    tree.move_in_rectangle() #用于移动树的位置，使树的位置自适应画布(自动将图片移动到画布中心)
    im = Image.new("RGB", tree.get_size(), (239, 239, 239))
    tree.draw_on(im, (85, 25, 0, 128, 53, 21), (0, 62, 21), 10)
    im.show()
 
 
if __name__ == '__main__':
    main()
