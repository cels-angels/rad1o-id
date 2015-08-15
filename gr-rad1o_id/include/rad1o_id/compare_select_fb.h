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


#ifndef INCLUDED_RAD1O_ID_COMPARE_SELECT_FB_H
#define INCLUDED_RAD1O_ID_COMPARE_SELECT_FB_H

#include <rad1o_id/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace rad1o_id {

    /*!
     * \brief <+description of block+>
     * \ingroup rad1o_id
     *
     */
    class RAD1O_ID_API compare_select_fb : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<compare_select_fb> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of rad1o_id::compare_select_fb.
       *
       * To avoid accidental use of raw pointers, rad1o_id::compare_select_fb's
       * constructor is in a private implementation
       * class. rad1o_id::compare_select_fb::make is the public interface for
       * creating new instances.
       */
      static sptr make();
    };

  } // namespace rad1o_id
} // namespace gr

#endif /* INCLUDED_RAD1O_ID_COMPARE_SELECT_FB_H */
