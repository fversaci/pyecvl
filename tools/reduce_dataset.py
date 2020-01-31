# Copyright (c) 2020 CRS4
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""\
Generate a smaller version of a DeepHealth dataset.
"""

import argparse
import io
import os
import yaml

Loader = getattr(yaml, "CLoader", "Loader")
Dumper = getattr(yaml, "CDumper", "Dumper")


def dump(doc, f):
    yaml.dump(doc, f, Dumper, default_flow_style=False)


def main(args):
    with io.open(args.dataset_file, "rt") as f:
        doc = yaml.load(f, Loader)
    images = doc["images"]
    try:
        split = doc["split"]
    except KeyError:
        n_out = round(args.fraction * len(images))
        doc["images"] = images[:n_out]
    else:
        n_tr = round(args.fraction * len(split["training"]))
        n_val = round(args.fraction * len(split["validation"]))
        n_test = round(args.fraction * len(split["test"]))
        out_tr = [images[_] for _ in split["training"][:n_tr]]
        out_val = [images[_] for _ in split["validation"][:n_val]]
        out_test = [images[_] for _ in split["test"][:n_test]]
        doc["images"] = out_tr + out_val + out_test
        doc["split"]["training"] = list(range(n_tr))
        doc["split"]["validation"] = list(range(n_tr, n_tr + n_val))
        doc["split"]["test"] = list(range(n_tr + n_val, n_tr + n_val + n_test))
    if not args.output_file:
        head, tail = os.path.splitext(args.dataset_file)
        args.output_file = "%s_small%s" % (head, tail)
    with io.open(args.output_file, "wt") as f:
        dump(doc, f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dataset_file", metavar="DATASET_FILE",
                        help="YAML dataset file")
    parser.add_argument("-f", "--fraction", metavar="FLOAT", type=float,
                        default=.1, help="fraction of the dataset to extract")
    parser.add_argument("-o", "--output-file", metavar="STRING",
                        help="output YAML dataset file")
    main(parser.parse_args())