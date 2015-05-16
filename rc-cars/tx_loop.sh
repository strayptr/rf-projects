#!/bin/bash

source freq.sh

if [ -z "$1" ]; then
  # print help
  ./tx.sh
  exit 1
fi

INFILE=$1
shift 1

while true; do
  ./tx.sh "$INFILE"
done


