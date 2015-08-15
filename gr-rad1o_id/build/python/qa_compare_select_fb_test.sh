#!/usr/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id/build/python:$PATH
export LD_LIBRARY_PATH=/home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id/build/swig:$PYTHONPATH
/usr/bin/python2 /home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id/python/qa_compare_select_fb.py 
