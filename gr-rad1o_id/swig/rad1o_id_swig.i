/* -*- c++ -*- */

#define RAD1O_ID_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "rad1o_id_swig_doc.i"

%{
#include "rad1o_id/compare_select_fb.h"
%}

%include "rad1o_id/compare_select_fb.h"
GR_SWIG_BLOCK_MAGIC2(rad1o_id, compare_select_fb);
