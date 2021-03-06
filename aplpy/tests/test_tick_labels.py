from __future__ import absolute_import, print_function, division

import os

import numpy as np
from astropy.tests.helper import pytest
from .helpers import generate_hdu

from .. import FITSFigure

ROOT = os.path.dirname(os.path.abspath(__file__))
HEADER_DIR = os.path.join(ROOT, 'data/2d_fits')
REFERENCE = os.path.join(HEADER_DIR, '1904-66_TAN.hdr')


def test_tick_labels_show_hide():
    data = np.zeros((16, 16))
    f = FITSFigure(data)
    f.tick_labels.hide()
    f.tick_labels.show()
    f.tick_labels.hide_x()
    f.tick_labels.show_x()
    f.tick_labels.hide_y()
    f.tick_labels.show_y()
    f.close()


def test_tick_labels_format_scalar():
    data = np.zeros((16, 16))
    f = FITSFigure(data)
    f.tick_labels.set_xformat('%i')
    f.tick_labels.set_yformat('%i')
    f.close()


def test_tick_labels_position():
    data = np.zeros((16, 16))
    f = FITSFigure(data)
    f.tick_labels.set_xposition('top')
    f.tick_labels.set_xposition('bottom')
    f.tick_labels.set_yposition('right')
    f.tick_labels.set_yposition('left')
    f.close()


def test_tick_labels_position_invalid():
    data = np.zeros((16, 16))
    f = FITSFigure(data)
    with pytest.raises(ValueError):
        f.tick_labels.set_xposition('right')
    with pytest.raises(ValueError):
        f.tick_labels.set_xposition('left')
    with pytest.raises(ValueError):
        f.tick_labels.set_yposition('top')
    with pytest.raises(ValueError):
        f.tick_labels.set_yposition('bottom')
    f.close()


def test_tick_labels_font():
    data = np.zeros((16, 16))
    f = FITSFigure(data)
    f.tick_labels.set_font(size='small', weight='bold', stretch='normal',
                           family='serif', style='normal', variant='normal')
    f.close()


def test_single_d_format():
    hdu = generate_hdu(REFERENCE)
    f = FITSFigure(hdu)
    f.show_grayscale()
    f.tick_labels.set_yformat('d.d')
    f.save('test_label_format.png')
