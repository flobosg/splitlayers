# splitlayers

Python script based on [layer-to-svg](https://github.com/james-bird/layer-to-svg), but:

* Uses `lxml.etree` instead of `xml.etree.ElementTree`.
* Each output file will be named `slide-n.svg` according to layer order.

If a layer named `background` exists, it will be present in each output file.
