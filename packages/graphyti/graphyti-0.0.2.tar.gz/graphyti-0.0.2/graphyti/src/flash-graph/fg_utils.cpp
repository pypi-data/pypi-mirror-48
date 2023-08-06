/*
 * Copyright 2014 Open Connectome Project (http://openconnecto.me)
 * Written by Da Zheng (zhengda1936@gmail.com)
 *
 * This file is part of FlashMatrix.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "fg_utils.h"
#include "in_mem_storage.h"
#include "fg_utils.h"

namespace fg
{

size_t get_out_size(fg::vertex_index::ptr vindex)
{
	if (vindex->is_compressed()) {
		fg::vsize_t num_vertices = vindex->get_num_vertices();
		if (vindex->get_graph_header().is_directed_graph()) {
			fg::in_mem_cdirected_vertex_index::ptr dindex
				= fg::in_mem_cdirected_vertex_index::create(*vindex);
			fg::directed_vertex_entry dentry = dindex->get_vertex(num_vertices - 1);
			return dentry.get_out_off() + dindex->get_out_size(
					num_vertices - 1) - vindex->get_out_part_loc();
		}
		else {
			fg::in_mem_cundirected_vertex_index::ptr uindex
				= fg::in_mem_cundirected_vertex_index::create(*vindex);
			fg::vertex_offset off = uindex->get_vertex(num_vertices - 1);
			return off.get_off() + uindex->get_size(
					num_vertices - 1) - vindex->get_header_size();
		}
	}
	else {
		if (vindex->get_graph_header().is_directed_graph()) {
			fg::directed_vertex_index::ptr dindex
				= fg::directed_vertex_index::cast(vindex);
			return dindex->get_graph_size() - vindex->get_out_part_loc();
		}
		else {
			fg::undirected_vertex_index::ptr uindex
				= fg::undirected_vertex_index::cast(vindex);
			return uindex->get_graph_size() - vindex->get_header_size();
		}
	}
}

void init_out_offs(fg::vertex_index::ptr vindex, std::vector<off_t> &out_offs)
{
	size_t num_vertices = vindex->get_num_vertices();
	assert(num_vertices + 1 == out_offs.size());
	if (vindex->is_compressed()) {
		out_offs[0] = get_out_off(vindex);
		if (vindex->get_graph_header().is_directed_graph()) {
			fg::in_mem_cdirected_vertex_index::ptr dindex
				= fg::in_mem_cdirected_vertex_index::create(*vindex);
			for (size_t i = 1; i <= num_vertices; i++)
				out_offs[i] = out_offs[i - 1] + dindex->get_out_size(i - 1);
		}
		else {
			fg::in_mem_cundirected_vertex_index::ptr uindex
				= fg::in_mem_cundirected_vertex_index::create(*vindex);
			for (size_t i = 1; i <= num_vertices; i++)
				out_offs[i] = out_offs[i - 1] + uindex->get_size(i - 1);
		}
		assert((size_t) out_offs[num_vertices]
				== get_out_size(vindex) + out_offs[0]);
	}
	else {
		if (vindex->get_graph_header().is_directed_graph()) {
			off_t out_part_loc = vindex->get_out_part_loc();
			fg::directed_vertex_index::ptr dindex
				= fg::directed_vertex_index::cast(vindex);
			for (size_t i = 0; i < num_vertices; i++)
				out_offs[i] = dindex->get_vertex(i).get_out_off();
			out_offs[num_vertices] = get_out_size(vindex) + out_part_loc;
		}
		else {
			fg::undirected_vertex_index::ptr uindex
				= fg::undirected_vertex_index::cast(vindex);
			for (size_t i = 0; i < num_vertices; i++)
				out_offs[i] = uindex->get_vertex(i).get_off();
			out_offs[num_vertices]
				= get_out_size(vindex) + vindex->get_header_size();
		}
	}
	for (size_t i = 1; i <= num_vertices; i++)
		assert(out_offs[i] > out_offs[i - 1]);
}

void init_in_offs(fg::vertex_index::ptr vindex, std::vector<off_t> &in_offs)
{
	size_t num_vertices = vindex->get_num_vertices();
	assert(num_vertices + 1 == in_offs.size());
	assert(vindex->get_graph_header().is_directed_graph());
	if (vindex->is_compressed()) {
		fg::in_mem_cdirected_vertex_index::ptr dindex
			= fg::in_mem_cdirected_vertex_index::create(*vindex);
		in_offs[0] = get_in_off(vindex);
		for (size_t i = 1; i <= num_vertices; i++)
			in_offs[i] = in_offs[i - 1] + dindex->get_in_size(i - 1);
		assert((size_t) in_offs[num_vertices]
				== get_in_size(vindex) + in_offs[0]);
	}
	else {
		fg::directed_vertex_index::ptr dindex
			= fg::directed_vertex_index::cast(vindex);
		for (size_t i = 0; i < num_vertices; i++)
			in_offs[i] = dindex->get_vertex(i).get_in_off();
		in_offs[num_vertices] = get_in_size(vindex) + vindex->get_header_size();
	}
	for (size_t i = 1; i <= num_vertices; i++)
		assert(in_offs[i] > in_offs[i - 1]);
}

static bool deduplicate = false;
// remove self edges. It's enabled by default.
static bool remove_selfe = true;

void set_deduplicate(bool v)
{
	deduplicate = v;
}

void set_remove_self_edge(bool v)
{
	remove_selfe = v;
}

namespace
{

struct unit4
{
	char data[4];
};

struct unit8
{
	char data[8];
};

}


namespace
{

typedef std::unordered_map<fg::vertex_id_t, fg::vertex_id_t> vertex_map_t;

}

namespace
{

struct block_info
{
	// The number of non-zero entries.
	uint32_t nnz;
	// The number of rows with non-zero entries.
	uint16_t nrow;
	// The number of rows with a single non-zero entry.
	uint16_t num_coos;

	block_info() {
		nnz = 0;
		nrow = 0;
		num_coos = 0;
	}
};

}
}
