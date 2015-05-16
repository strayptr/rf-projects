#!/bin/bash

source freq.sh

if [ -z "$1" ] || [ -z "$2" ]; then
  echo "record.sh <outfile> <time>"
  exit 1
fi

OUTFILE="${FREQ}_${SAMPLE_RATE_HZ}_${BASEBAND_FILTER_BANDWIDTH}_$1"
TIME=$2
shift 1
shift 1

#hackrf_transfer -f $FREQ -s $SAMPLE_RATE_HZ -b $BASEBAND_FILTER_BANDWIDTH -r $OUTFILE $*
hackrf_transfer -f $FREQ -s $SAMPLE_RATE_HZ -b $BASEBAND_FILTER_BANDWIDTH -w $OUTFILE $*
