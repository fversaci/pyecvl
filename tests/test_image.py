from pyecvl._core.ecvl import (
    Image, DataType, ColorType, View_int8, View_int16, Neg, RearrangeChannels
)


def test_empty():
    img = Image()
    assert len(img.dims_) == 0
    assert img.IsEmpty()


def test_five_dims():
    dims = [1, 2, 3, 4, 5]
    img = Image(dims, DataType.uint8, "xyzoo", ColorType.none)
    assert img.dims_ == dims
    assert len(img.strides_) == len(dims)


def test_view():
    x = Image([5, 4, 3], DataType.int8, "xyc", ColorType.RGB)
    y = View_int8(x)
    y[1, 2, 0] = 36
    y[3, 3, 2] = 48
    y[4, 2, 1] = -127
    y[3, 2, 0] = -128
    Neg(x)
    assert y[1, 2, 0] == -36
    assert y[3, 3, 2] == -48
    assert y[4, 2, 1] == 127
    assert y[3, 2, 0] == -128


def test_rearrange_channels():
    S = [3, 4, 3, 2]
    img = Image(S, DataType.int16, "cxyz", ColorType.RGB)
    view = View_int16(img)
    for i in range(S[0]):
        for j in range(S[1]):
            for k in range(S[2]):
                for l in range(S[3]):
                    view[i, j, k, l] = (l + k * S[3] + j * S[2] * S[3] +
                                        i * S[1] * S[2] * S[3])
    img2 = Image()
    RearrangeChannels(img, img2, "xyzc")
    view2 = View_int16(img2)
    assert view2[2, 0, 1, 0] == view[0, 2, 0, 1]
    assert view2[3, 1, 1, 2] == view[2, 3, 1, 1]
    assert view2[0, 2, 0, 1] == view[1, 0, 2, 0]
    assert view2[1, 2, 0, 1] == view[1, 1, 2, 0]
