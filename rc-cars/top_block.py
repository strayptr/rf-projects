#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Tue Apr 28 23:16:33 2015
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import window
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import wx

class top_block(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Top Block")

		##################################################
		# Variables
		##################################################
		self.variable_chooser_0 = variable_chooser_0 = 1
		self.transition_width = transition_width = 10000
		self.sym_per_sec = sym_per_sec = 2032
		self.samp_rate = samp_rate = 2000000
		self.rf_gain = rf_gain = 10
		self.cutoff_freq = cutoff_freq = 10000

		##################################################
		# Blocks
		##################################################
		_transition_width_sizer = wx.BoxSizer(wx.VERTICAL)
		self._transition_width_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_transition_width_sizer,
			value=self.transition_width,
			callback=self.set_transition_width,
			label='transition_width',
			converter=forms.float_converter(),
			proportion=0,
		)
		self._transition_width_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_transition_width_sizer,
			value=self.transition_width,
			callback=self.set_transition_width,
			minimum=100,
			maximum=100000,
			num_steps=1000,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_transition_width_sizer)
		_rf_gain_sizer = wx.BoxSizer(wx.VERTICAL)
		self._rf_gain_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_rf_gain_sizer,
			value=self.rf_gain,
			callback=self.set_rf_gain,
			label='rf_gain',
			converter=forms.int_converter(),
			proportion=0,
		)
		self._rf_gain_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_rf_gain_sizer,
			value=self.rf_gain,
			callback=self.set_rf_gain,
			minimum=0,
			maximum=47,
			num_steps=47,
			style=wx.SL_HORIZONTAL,
			cast=int,
			proportion=1,
		)
		self.Add(_rf_gain_sizer)
		_cutoff_freq_sizer = wx.BoxSizer(wx.VERTICAL)
		self._cutoff_freq_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_cutoff_freq_sizer,
			value=self.cutoff_freq,
			callback=self.set_cutoff_freq,
			label='cutoff_freq',
			converter=forms.int_converter(),
			proportion=0,
		)
		self._cutoff_freq_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_cutoff_freq_sizer,
			value=self.cutoff_freq,
			callback=self.set_cutoff_freq,
			minimum=100,
			maximum=100000,
			num_steps=1000,
			style=wx.SL_HORIZONTAL,
			cast=int,
			proportion=1,
		)
		self.Add(_cutoff_freq_sizer)
		self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
			self.GetWin(),
			title="Scope Plot",
			sample_rate=samp_rate,
			v_scale=0,
			v_offset=0,
			t_scale=0,
			ac_couple=False,
			xy_mode=False,
			num_inputs=1,
			trig_mode=gr.gr_TRIG_MODE_AUTO,
			y_axis_label="Counts",
		)
		self.Add(self.wxgui_scopesink2_0.win)
		self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
			self.GetWin(),
			baseband_freq=0,
			y_per_div=10,
			y_divs=10,
			ref_level=0,
			ref_scale=2.0,
			sample_rate=samp_rate,
			fft_size=1024,
			fft_rate=15,
			average=False,
			avg_alpha=None,
			title="FFT Plot",
			peak_hold=False,
		)
		self.Add(self.wxgui_fftsink2_0.win)
		self._variable_chooser_0_chooser = forms.drop_down(
			parent=self.GetWin(),
			value=self.variable_chooser_0,
			callback=self.set_variable_chooser_0,
			label='variable_chooser_0',
			choices=[1, 2, 3],
			labels=["a", "b", "c"],
		)
		self.Add(self._variable_chooser_0_chooser)
		self.osmosdr_sink_c_0 = osmosdr.sink_c( args="numchan=" + str(1) + " " + "" )
		self.osmosdr_sink_c_0.set_sample_rate(samp_rate)
		self.osmosdr_sink_c_0.set_center_freq(27.14e6, 0)
		self.osmosdr_sink_c_0.set_freq_corr(0, 0)
		self.osmosdr_sink_c_0.set_gain(10, 0)
		self.osmosdr_sink_c_0.set_if_gain(rf_gain, 0)
		self.osmosdr_sink_c_0.set_bb_gain(20, 0)
		self.osmosdr_sink_c_0.set_antenna("", 0)
		self.osmosdr_sink_c_0.set_bandwidth(0, 0)
		  
		self.low_pass_filter_0 = gr.interp_fir_filter_fff(1, firdes.low_pass(
			1, samp_rate, cutoff_freq, transition_width, firdes.WIN_BLACKMAN, 6.76))
		self.const_source_x_0 = gr.sig_source_f(0, gr.GR_CONST_WAVE, 0, 0, 0)
		self.blocks_vector_source_x_0 = blocks.vector_source_f([1,1,1,0,  1,1,1,0,  1,1,1,0,  1,1,1,0,  1,0, 1,0, 1,0, 1,0, 1,0, 1,0, 1,0, 1,0, 1,0, 1,0], True, 1, [])
		self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate)
		self.blocks_repeat_0 = blocks.repeat(gr.sizeof_float*1, samp_rate/sym_per_sec)
		self.blocks_float_to_complex_0 = blocks.float_to_complex(1)

		##################################################
		# Connections
		##################################################
		self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_repeat_0, 0))
		self.connect((self.blocks_repeat_0, 0), (self.blocks_throttle_0, 0))
		self.connect((self.blocks_throttle_0, 0), (self.wxgui_scopesink2_0, 0))
		self.connect((self.blocks_throttle_0, 0), (self.low_pass_filter_0, 0))
		self.connect((self.const_source_x_0, 0), (self.blocks_float_to_complex_0, 1))
		self.connect((self.low_pass_filter_0, 0), (self.blocks_float_to_complex_0, 0))
		self.connect((self.blocks_float_to_complex_0, 0), (self.osmosdr_sink_c_0, 0))
		self.connect((self.blocks_float_to_complex_0, 0), (self.wxgui_fftsink2_0, 0))


	def get_variable_chooser_0(self):
		return self.variable_chooser_0

	def set_variable_chooser_0(self, variable_chooser_0):
		self.variable_chooser_0 = variable_chooser_0
		self._variable_chooser_0_chooser.set_value(self.variable_chooser_0)

	def get_transition_width(self):
		return self.transition_width

	def set_transition_width(self, transition_width):
		self.transition_width = transition_width
		self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff_freq, self.transition_width, firdes.WIN_BLACKMAN, 6.76))
		self._transition_width_slider.set_value(self.transition_width)
		self._transition_width_text_box.set_value(self.transition_width)

	def get_sym_per_sec(self):
		return self.sym_per_sec

	def set_sym_per_sec(self, sym_per_sec):
		self.sym_per_sec = sym_per_sec

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
		self.blocks_throttle_0.set_sample_rate(self.samp_rate)
		self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff_freq, self.transition_width, firdes.WIN_BLACKMAN, 6.76))
		self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
		self.osmosdr_sink_c_0.set_sample_rate(self.samp_rate)

	def get_rf_gain(self):
		return self.rf_gain

	def set_rf_gain(self, rf_gain):
		self.rf_gain = rf_gain
		self._rf_gain_slider.set_value(self.rf_gain)
		self._rf_gain_text_box.set_value(self.rf_gain)
		self.osmosdr_sink_c_0.set_if_gain(self.rf_gain, 0)

	def get_cutoff_freq(self):
		return self.cutoff_freq

	def set_cutoff_freq(self, cutoff_freq):
		self.cutoff_freq = cutoff_freq
		self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff_freq, self.transition_width, firdes.WIN_BLACKMAN, 6.76))
		self._cutoff_freq_slider.set_value(self.cutoff_freq)
		self._cutoff_freq_text_box.set_value(self.cutoff_freq)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

