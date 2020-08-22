#!/bin/bash
echo ""
echo "Quick SpiceScript Setup!"
echo ""
echo "Installing Requirements..."
pip3 install -r requirements.txt
echo ""
echo "Installed Requirements, Running SpiceScript"
python3 spicescript.py
