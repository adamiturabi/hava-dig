#!/bin/sh
cp src/searchroot.js docs/searchroot.js
cd src
python3 build_pages.py
