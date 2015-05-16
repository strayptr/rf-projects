#!/usr/bin/python

#==============================================================================
# Functionality
#==============================================================================

# utility funcs, classes, etc go here.

#==============================================================================
# Cmdline
#==============================================================================
import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, 
    description="""
TODO
""")
     
parser.add_argument('-v', '--verbose',
    action="store_true",
    help="verbose output" )

parser.add_argument('-f', '--frequency', type=int,
        help="frequency in hz")

parser.add_argument('-b', '--bandwidth', type=int,
        help="bandwidth of each sample")

parser.add_argument('-s', '--sample-rate', type=int,
        help="sample rate in hz")

parser.add_argument('filename',
        help="input IQ file")

#==============================================================================
# Main
#==============================================================================
import sys
import pdb
import numpy as np

import pyximport
pyximport.install(setup_args={"include_dirs":np.get_include()},
                  reload_support=True)
import support


def signal_analyze(ft, freq, sample_rate):
    freqs = np.fft.fftfreq(len(ft))
    print(freqs.min(), freqs.max())
    # (-0.5, 0.499975)
    pdb.set_trace()

    # Find the peak in the coefficients
    idx = np.argmax(np.abs(ft))
    freq = freqs[idx]
    freq_in_hertz = abs(freq * sample_rate)
    print(freq_in_hertz)


def main():
    print args
    samples = support.iq_fromfile(args.filename)
    signal = support.iq_to_signal(samples)
    pdb.set_trace()
    print 'analyzing...'
    ft = support.iq_fft(samples)
    signal_analyze(ft, args.frequency, args.sample_rate)

if __name__ == "__main__":
    args = parser.parse_args()
    main()


