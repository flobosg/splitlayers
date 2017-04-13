#!/usr/bin/env python
import copy
import argparse
from lxml import etree

parser = argparse.ArgumentParser()
parser.add_argument("-k",  "--keep", metavar='LAYER', help="keep layer in output files")
parser.add_argument("-p",  "--prefix", metavar='PREFIX', help="set ordered output prefix")
parser.add_argument("SVGFILE", help="input SVG file")
args = parser.parse_args()

TREE = etree.parse(args.SVGFILE)
ROOT = TREE.getroot()
LAYER_ATTR = "{http://www.w3.org/2000/svg}g"
LABEL_ATTR = "{http://www.inkscape.org/namespaces/inkscape}label"

LAYERS = [g for g in ROOT.findall(LAYER_ATTR) if g.get(LABEL_ATTR) != args.keep]
print len(LAYERS), "layers found."

for i, layer in enumerate(LAYERS, 1):
    layer_num = str(i).zfill(len(LAYERS)/10)
    if layer.get(LABEL_ATTR):
        layer_title = layer.get(LABEL_ATTR)
    else:
        layer_title = "layer-%s" % layer_num
    layer_tree = copy.deepcopy(TREE)
    layer_root = layer_tree.getroot()
    for g in layer_root.findall(LAYER_ATTR):
        if g.get(LABEL_ATTR) not in (args.keep, layer_title):
            layer_root.remove(g)
    if args.prefix:
        out_file = "%s-%s.svg" % (args.prefix, layer_num)
    else:
        out_file = "%s.svg" % layer_title
    print out_file, "saved."
    layer_tree.write(out_file)
