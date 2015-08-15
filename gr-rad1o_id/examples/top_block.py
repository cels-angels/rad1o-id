#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sat Aug 15 14:21:34 2015
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
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
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
        self.freq_slider = freq_slider = 500e3
        self.f1_bp_taps = f1_bp_taps = [-0.0034913108684122562, 0.016121335327625275, -0.030533839017152786, 0.01881207898259163, 0.043789319694042206, -0.12244637310504913, 0.13050289452075958, -0.020888589322566986, -0.1393565535545349, 0.21573688089847565, -0.1393565535545349, -0.020888589322566986, 0.13050289452075958, -0.12244637310504913, 0.043789319694042206, 0.01881207898259163, -0.030533839017152786, 0.016121335327625275, -0.0034913108684122562]
        self.f0_bp_taps = f0_bp_taps = [0.009907027706503868, 0.01748894527554512, 0.0200509000569582, -0.00631917268037796, -0.06848347187042236, -0.12408018857240677, -0.10601181536912918, 0.006915525533258915, 0.14913780987262726, 0.21388313174247742, 0.14913780987262726, 0.006915525533258915, -0.10601181536912918, -0.12408018857240677, -0.06848347187042236, -0.00631917268037796, 0.0200509000569582, 0.01748894527554512, 0.009907027706503868]

        ##################################################
        # Blocks
        ##################################################
        self._freq_slider_range = Range(100e3, 2e6, 100, 500e3, 200)
        self._freq_slider_win = RangeWidget(self._freq_slider_range, self.set_freq_slider, "freq_slider", "counter_slider", float)
        self.top_layout.addWidget(self._freq_slider_win)
        self.rad1o_id_compare_select_fb_0 = rad1o_id.compare_select_fb()
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
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	sample_rate/down_sampling, #bw
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_1.disable_legend()
        
        if complex == type(float()):
          self.qtgui_freq_sink_x_1.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_1_win)
        self.fir_filter_xxx_0_0 = filter.fir_filter_ccc(down_sampling, (f1_bp_taps))
        self.fir_filter_xxx_0_0.declare_sample_delay(0)
        self.fir_filter_xxx_0 = filter.fir_filter_ccc(down_sampling, (f0_bp_taps))
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.blocks_complex_to_mag_squared_0_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(sample_rate, analog.GR_COS_WAVE, freq_slider, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.fir_filter_xxx_0, 0))    
        self.connect((self.analog_sig_source_x_0, 0), (self.fir_filter_xxx_0_0, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.rad1o_id_compare_select_fb_0, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0_0, 0), (self.rad1o_id_compare_select_fb_0, 1))    
        self.connect((self.fir_filter_xxx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))    
        self.connect((self.fir_filter_xxx_0, 0), (self.qtgui_freq_sink_x_1, 0))    
        self.connect((self.fir_filter_xxx_0_0, 0), (self.blocks_complex_to_mag_squared_0_0, 0))    
        self.connect((self.fir_filter_xxx_0_0, 0), (self.qtgui_freq_sink_x_1, 1))    
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
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.sample_rate/self.down_sampling)

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.sample_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.sample_rate/self.down_sampling)

    def get_freq_slider(self):
        return self.freq_slider

    def set_freq_slider(self, freq_slider):
        self.freq_slider = freq_slider
        self.analog_sig_source_x_0.set_frequency(self.freq_slider)

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
