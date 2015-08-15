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

#ifndef INCLUDED_RAD1O_ID_COMPARE_SELECT_FB_IMPL_H
#define INCLUDED_RAD1O_ID_COMPARE_SELECT_FB_IMPL_H

#include <rad1o_id/compare_select_fb.h>

namespace gr {
  namespace rad1o_id {

    class compare_select_fb_impl : public compare_select_fb
    {
     private:
      // Nothing to declare in this block.

     public:
      compare_select_fb_impl();
      ~compare_select_fb_impl();

      // Where all the action really happens
      int work(int noutput_items,
	       gr_vector_const_void_star &input_items,
	       gr_vector_void_star &output_items);
    };

  } // namespace rad1o_id
} // namespace gr

#endif /* INCLUDED_RAD1O_ID_COMPARE_SELECT_FB_IMPL_H */
