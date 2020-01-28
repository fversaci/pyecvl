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

import pyecvl._core.ecvl as ecvl


def test_size():
    assert ecvl.DataTypeSize(ecvl.DataType.int8) == 1
    assert ecvl.DataTypeSize(ecvl.DataType.int16) == 2
    assert ecvl.DataTypeSize(ecvl.DataType.int32) == 4
    assert ecvl.DataTypeSize(ecvl.DataType.int64) == 8
    assert ecvl.DataTypeSize(ecvl.DataType.float32) == 4
    assert ecvl.DataTypeSize(ecvl.DataType.float64) == 8
    assert ecvl.DataTypeSize(ecvl.DataType.uint8) == 1
    assert ecvl.DataTypeSize(ecvl.DataType.uint16) == 2


def test_size_no_args():
    assert ecvl.DataTypeSize() == 8
    assert ecvl.DataTypeSignedSize() == 6
