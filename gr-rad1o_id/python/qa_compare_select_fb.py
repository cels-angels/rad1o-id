#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2015 <+YOU OR YOUR COMPANY+>.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

from gnuradio import gr, gr_unittest
from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import rad1o_id
import sys


class qa_compare_select_fb (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # set up fg
        samp_rate = 100
        ##################################################
        # Blocks
        ##################################################
        self.rad1o_id_compare_select_fb_0 = rad1o_id.compare_select_fb()
        self.blocks_vector_source_x_0_0 = blocks.vector_source_f((3.34, 1.67, 12.97, 2.34, 100.00), False, 1, [])
        self.blocks_vector_source_x_0 = blocks.vector_source_f((2.34, 5.67, 8.97, 7.34, 10.00), False, 1, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_vector_sink_x_0 = blocks.vector_sink_b(1)
        ##################################################
        # Connections
        ##################################################
        self.tb.connect((self.blocks_vector_source_x_0, 0), (self.rad1o_id_compare_select_fb_0, 0))
        self.tb.connect((self.blocks_vector_source_x_0_0, 0), (self.rad1o_id_compare_select_fb_0, 1))
        self.tb.connect((self.rad1o_id_compare_select_fb_0, 0), (self.blocks_throttle_0, 0))
        self.tb.connect((self.blocks_throttle_0, 0), (self.blocks_vector_sink_x_0, 0));



        self.tb.run ()

        print self.blocks_vector_sink_x_0.data()
        # check data


if __name__ == '__main__':
    gr_unittest.run(qa_compare_select_fb, "qa_compare_select_fb.xml")
