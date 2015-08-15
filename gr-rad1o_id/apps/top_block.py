#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sat Aug 15 14:49:23 2015
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from math import pi
from optparse import OptionParser
import pmt
import rad1o_id
import sip
import sys


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.down_sampling = down_sampling = 16
        self.sample_rate = sample_rate = 250e3*down_sampling
        self.preamble_len_tag = preamble_len_tag = gr.tag_utils.python_to_tag((0, pmt.intern("packet_len"), pmt.from_long(8), pmt.intern("src")))
        self.f1_bp_taps = f1_bp_taps = [-0.008489873260259628, 0.017516516149044037, -0.02309376560151577, 3.1378305752533504e-17, 0.06292477995157242, -0.12457011640071869, 0.1126808300614357, -3.387264241990756e-17, -0.14707811176776886, 0.21481703221797943, -0.14707811176776886, -3.387264241990756e-17, 0.1126808300614357, -0.12457011640071869, 0.06292477995157242, 3.1378305752533504e-17, -0.02309376560151577, 0.017516516149044037, -0.008489873260259628]
        self.f0_bp_taps = f0_bp_taps =  [0.008489873260259628, 0.017516516149044037, 0.02309376560151577, -1.1766864243609758e-17, -0.06292477995157242, -0.12457011640071869, -0.1126808300614357, 3.387264241990756e-17, 0.14707811176776886, 0.21481703221797943, 0.14707811176776886, 3.387264241990756e-17, -0.1126808300614357, -0.12457011640071869, -0.06292477995157242, -1.1766864243609758e-17, 0.02309376560151577, 0.017516516149044037, 0.008489873260259628]

        ##################################################
        # Blocks
        ##################################################
        self.rad1o_id_compare_select_fb_0 = rad1o_id.compare_select_fb()
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	1024, #size
        	sample_rate/down_sampling, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2*2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_number_sink_0 = qtgui.number_sink(
                gr.sizeof_char,
                0,
                qtgui.NUM_GRAPH_HORIZ,
        	1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("")
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        units = ["", "", "", "", "",
                  "", "", "", "", ""]
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, -1)
            self.qtgui_number_sink_0.set_max(i, 1)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	sample_rate/down_sampling, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if complex == type(float()):
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.fir_filter_xxx_1_0 = filter.fir_filter_fff(down_sampling/2, (1, ))
        self.fir_filter_xxx_1_0.declare_sample_delay(0)
        self.fir_filter_xxx_1 = filter.fir_filter_fff(down_sampling/2, (1, ))
        self.fir_filter_xxx_1.declare_sample_delay(0)
        self.fir_filter_xxx_0_0 = filter.fir_filter_ccc(down_sampling/2, (f1_bp_taps))
        self.fir_filter_xxx_0_0.declare_sample_delay(0)
        self.fir_filter_xxx_0 = filter.fir_filter_ccc(down_sampling/2, (f0_bp_taps))
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bf(([0.5, 1.5]), 1)
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=100e-2,
        	frequency_offset=1e-4,
        	epsilon=1.0,
        	taps=(1.0 + 1.0j, ),
        	noise_seed=0,
        	block_tags=True
        )
        self.blocks_vector_source_x_1 = blocks.vector_source_b((0,0), True, 1, [])
        self.blocks_vector_source_x_0 = blocks.vector_source_b([0,0], True, 1, [preamble_len_tag])
        self.blocks_tagged_stream_mux_0 = blocks.tagged_stream_mux(gr.sizeof_char*1, "packet_len", 0)
        self.blocks_tagged_stream_align_1 = blocks.tagged_stream_align(gr.sizeof_char*1, "packet_len")
        self.blocks_tag_debug_0 = blocks.tag_debug(gr.sizeof_char*1, "packet_length", ""); self.blocks_tag_debug_0.set_display(False)
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 64, "packet_len")
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_char*1, 16)
        self.blocks_packed_to_unpacked_xx_0 = blocks.packed_to_unpacked_bb(1, gr.GR_MSB_FIRST)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((0.7, ))
        self.blocks_complex_to_mag_squared_0_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.analog_frequency_modulator_fc_0 = analog.frequency_modulator_fc(2*pi/4)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_frequency_modulator_fc_0, 0), (self.channels_channel_model_0, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.fir_filter_xxx_1, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0_0, 0), (self.fir_filter_xxx_1_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.fir_filter_xxx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.fir_filter_xxx_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.blocks_packed_to_unpacked_xx_0, 0), (self.blocks_repeat_0, 0))    
        self.connect((self.blocks_repeat_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))    
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.blocks_tagged_stream_mux_0, 1))    
        self.connect((self.blocks_tagged_stream_align_1, 0), (self.blocks_tagged_stream_mux_0, 0))    
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.blocks_packed_to_unpacked_xx_0, 0))    
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.blocks_tag_debug_0, 0))    
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_tagged_stream_align_1, 0))    
        self.connect((self.blocks_vector_source_x_1, 0), (self.blocks_stream_to_tagged_stream_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.analog_frequency_modulator_fc_0, 0))    
        self.connect((self.fir_filter_xxx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))    
        self.connect((self.fir_filter_xxx_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.fir_filter_xxx_0_0, 0), (self.blocks_complex_to_mag_squared_0_0, 0))    
        self.connect((self.fir_filter_xxx_0_0, 0), (self.qtgui_time_sink_x_0, 1))    
        self.connect((self.fir_filter_xxx_1, 0), (self.rad1o_id_compare_select_fb_0, 0))    
        self.connect((self.fir_filter_xxx_1_0, 0), (self.rad1o_id_compare_select_fb_0, 1))    
        self.connect((self.rad1o_id_compare_select_fb_0, 0), (self.qtgui_number_sink_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_down_sampling(self):
        return self.down_sampling

    def set_down_sampling(self, down_sampling):
        self.down_sampling = down_sampling
        self.set_sample_rate(250e3*self.down_sampling)
        self.blocks_throttle_0.set_sample_rate(self.sample_rate/self.down_sampling)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.sample_rate/self.down_sampling)
        self.qtgui_time_sink_x_0.set_samp_rate(self.sample_rate/self.down_sampling)

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate
        self.blocks_throttle_0.set_sample_rate(self.sample_rate/self.down_sampling)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.sample_rate/self.down_sampling)
        self.qtgui_time_sink_x_0.set_samp_rate(self.sample_rate/self.down_sampling)

    def get_preamble_len_tag(self):
        return self.preamble_len_tag

    def set_preamble_len_tag(self, preamble_len_tag):
        self.preamble_len_tag = preamble_len_tag

    def get_f1_bp_taps(self):
        return self.f1_bp_taps

    def set_f1_bp_taps(self, f1_bp_taps):
        self.f1_bp_taps = f1_bp_taps
        self.fir_filter_xxx_0_0.set_taps((self.f1_bp_taps))

    def get_f0_bp_taps(self):
        return self.f0_bp_taps

    def set_f0_bp_taps(self, f0_bp_taps):
        self.f0_bp_taps = f0_bp_taps
        self.fir_filter_xxx_0.set_taps((self.f0_bp_taps))


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = top_block()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None  # to clean up Qt widgets
