#!/bin/bash

source freq.sh

FILENAME=$1
shift 1

if [ -z "$FILENAME" ]; then
  echo 'analyze <filename>'
  exit 1
fi

PY=pypy
PY=python

$PY analyze.py --freq $FREQ --bandwidth $BASEBAND_FILTER_BANDWIDTH --sample-rate $SAMPLE_RATE_HZ "$FILENAME" $@

