/* -*- c++ -*- */
/*
 * Copyright 2015 <+YOU OR YOUR COMPANY+>.
 *
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "compare_select_fb_impl.h"

namespace gr {
  namespace rad1o_id {

    compare_select_fb::sptr
    compare_select_fb::make()
    {
      return gnuradio::get_initial_sptr
        (new compare_select_fb_impl());
    }

    /*
     * The private constructor
     */
    compare_select_fb_impl::compare_select_fb_impl()
      : gr::sync_block("compare_select_fb",
              gr::io_signature::make(2, 2, sizeof(float)),
              gr::io_signature::make(1, 1, sizeof(char)))
    {}

    /*
     * Our virtual destructor.
     */
    compare_select_fb_impl::~compare_select_fb_impl()
    {
    }

    int
    compare_select_fb_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const float *in0 = (const float *) input_items[0];
        const float *in1 = (const float *) input_items[1];
        char *out = (char *) output_items[0];

        int i = 0;
        for(i = 0; i < noutput_items; ++i)
        {
          out[i] = (in1[i]-in0[i] < 0) ? 31 : 30;
        }

        return noutput_items;
    }

  } /* namespace rad1o_id */
} /* namespace gr */
