#!/bin/bash
# author: Henry Li and Lisa Yuan

gunzip -c ../MCB185/data/dictionary.gz | grep "r" | grep -E "^[acinorxz]{4,}$"
