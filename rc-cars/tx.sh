#!/bin/bash

source freq.sh

if [ -z "$1" ]; then
  echo "tx.sh <infile>"
  exit 1
fi

INFILE=$1
shift 1

set -x
hackrf_transfer -f $FREQ -s $SAMPLE_RATE_HZ -t "$INFILE" -a 1 -x $TX_GAIN $*

