# -*- coding: utf-8 -*-
import sys
import pyaudio
import numpy as np
from Queue import Queue
import time
import threading

from enthought.traits.api import *
from enthought.traits.ui.api import *
from enthought.enable.api import Window, Component, ComponentEditor
from enthought.pyface.timer.api import Timer
from enthought.chaco.api import Plot, ArrayPlotData, VPlotContainer
import enthought.chaco.default_colormaps as cm

NUM_SAMPLES = 1024
SAMPLING_RATE = 8000
SPECTROGRAM_LENGTH = 100
NUM_LINES = 5

class DemoHandler(Handler):
    def closed(self, info, is_ok):
        info.object.timer.Stop()
        info.object.finish_event.set()
        info.object.thread.join()        
        return

class Demo(HasTraits):
    plot = Instance(Component)
    timer = Instance(Timer)
    spectrum_list = List
    buffer_size = Int

    traits_view = View(
        VGroup(
            HGroup(
                Item('buffer_size', style="readonly"),
            ),
            Item('plot', editor=ComponentEditor(), show_label=False),
            orientation = "vertical"),
        resizable=True, title="Audio Spectrum",
        width=900, height=500,
        handler=DemoHandler
    )

    def __init__(self, **traits):
        super(Demo, self).__init__(**traits)
        self.plot = self._create_plot_component()
        self.queue = Queue()
        self.finish_event = threading.Event()        
        self.thread = threading.Thread(target=self.get_audio_data)
        self.thread.start()
        self.timer = Timer(10, self.on_timer)
        
    def _create_plot_component(self):
        self.data = ArrayPlotData()
        self.data["frequency"] = np.linspace(0., SAMPLING_RATE/2.0, num=NUM_SAMPLES/2)
        for i in xrange(NUM_LINES):
            self.data['amplitude%d' % i] = np.zeros(NUM_SAMPLES/2)
        self.data["time"] = np.linspace(0., float(NUM_SAMPLES)/SAMPLING_RATE, num=NUM_SAMPLES)
        self.data['time_amplitude'] = np.zeros(NUM_SAMPLES)        
        self.data['imagedata'] = np.zeros(( NUM_SAMPLES/2, SPECTROGRAM_LENGTH))
        
        spectrum_plot = Plot(self.data)
        for i in xrange(NUM_LINES):
            if i==NUM_LINES-1:
                linewidth = 2
                color = (1,0,0)
            else:
                linewidth = 1
                c = (NUM_LINES-i-1)/float(NUM_LINES)
                color = (1, 0.5+c/2, c)
            spectrum_plot.plot(("frequency", "amplitude%d" % i), name="Spectrum%d" % i, 
                color=color, line_width=linewidth)
        spectrum_plot.padding_bottom = 20
        spectrum_plot.padding_top = 20
        spec_range = spectrum_plot.plots.values()[0][0].value_mapper.range
        spec_range.low = -90
        spec_range.high = 0.0
        spectrum_plot.index_axis.title = 'Frequency(Hz)'
        spectrum_plot.value_axis.title = 'Amplitude(dB)'

        time_plot = Plot(self.data)
        time_plot.plot(("time", "time_amplitude"), name="Time", color="blue")
        time_plot.padding_top = 20
        time_plot.padding_bottom = 20
        time_plot.index_axis.title = 'Time (seconds)'
        time_plot.value_axis.title = 'Amplitude'
        time_range = time_plot.plots.values()[0][0].value_mapper.range
        time_range.low = -1.5
        time_range.high = 1.5

        spectrogram_plot = Plot(self.data)
        spectrogram_time = (0.0, SPECTROGRAM_LENGTH*NUM_SAMPLES/float(SAMPLING_RATE))
        spectrogram_freq = (0.0, SAMPLING_RATE/2.0)
        spectrogram_plot.img_plot('imagedata',
            name='Spectrogram',
            xbounds=spectrogram_time,
            ybounds=spectrogram_freq,
            colormap=cm.reverse(cm.Blues),
        )
        range_obj = spectrogram_plot.plots['Spectrogram'][0].value_mapper.range
        range_obj.high = -20
        range_obj.low = -60
        spectrogram_plot.padding_bottom = 20
        spectrogram_plot.padding_top = 20

        container = VPlotContainer()
        container.add(time_plot)    
        container.add(spectrum_plot)
        container.add(spectrogram_plot)

        return container        
        
    def on_timer(self, *args):
        self.buffer_size = self.queue.qsize()
        if self.buffer_size > 1:
            spectrum, time = self.queue.get(False)
            self.spectrum_list.append(spectrum)
            if len(self.spectrum_list) > NUM_LINES: del self.spectrum_list[0]
            for i, data in enumerate(self.spectrum_list):
                self.data['amplitude%d' % i] = data
            
            self.data['time_amplitude'] = time
            
            imagedata = self.data['imagedata']           
            imagedata[:,:-1] = imagedata[:,1:]
            imagedata[:,-1] = spectrum
            self.data['imagedata'] = imagedata

    def get_audio_data(self):
        pa = pyaudio.PyAudio()
        stream = pa.open(format=pyaudio.paInt16, channels=1,
                          rate=SAMPLING_RATE,
                          input=True, frames_per_buffer=NUM_SAMPLES)
        
        while not self.finish_event.is_set():
            audio_data  = np.fromstring(stream.read(NUM_SAMPLES), dtype=np.short)
            normalized_data = audio_data / 32768.0
            fft_data = np.abs(np.fft.rfft(normalized_data))[:NUM_SAMPLES/2]
            fft_data /= NUM_SAMPLES
            np.log10(fft_data, fft_data)
            fft_data *= 20
            self.queue.put( (fft_data, normalized_data) )
            
        stream.close()
        print "finished"            

if __name__ == "__main__":
    demo = Demo()
    demo.configure_traits()