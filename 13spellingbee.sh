#!/bin/bash

gunzip -c ../MCB185/data/dictionary.gz | grep "r" | grep -E "^[acinorxz]{4,}$"
