#!/usr/bin/env python
import copy
import sys
from lxml import etree

TREE = etree.parse(sys.argv[1])
ROOT = TREE.getroot()
LAYER_ATTR = "{http://www.w3.org/2000/svg}g"
LABEL_ATTR = "{http://www.inkscape.org/namespaces/inkscape}label"

LAYERS = [g for g in ROOT.findall(LAYER_ATTR) if g.get(LABEL_ATTR) != "background"]
print len(LAYERS), "layers found."

for i, layer in enumerate(LAYERS, 1):
    slide_num = str(i).zfill(len(LAYERS)/10)
    slide_title = layer.get(LABEL_ATTR)
    slide_tree = copy.deepcopy(TREE)
    slide_root = slide_tree.getroot()
    for g in slide_root.findall(LAYER_ATTR):
        if g.get(LABEL_ATTR) not in (slide_title, "background"):
            slide_root.remove(g)
    out_file = "slide-%s.svg" % slide_num
    print out_file, "saved."
    slide_tree.write(out_file)
