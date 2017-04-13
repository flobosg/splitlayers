# splitlayers

Python script based on [layer-to-svg](https://github.com/james-bird/layer-to-svg), but:

* Uses `lxml.etree` instead of `xml.etree.ElementTree`.
* Has an optional `-p PREFIX` argument. If this is set each output file will be named `PREFIX-number.svg` according to layer order. Otherwise the output filename will be the layer name.

If a layer named `background` exists, it will be present in each output file.
