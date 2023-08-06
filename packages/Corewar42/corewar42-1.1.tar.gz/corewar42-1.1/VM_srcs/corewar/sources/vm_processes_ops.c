/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   vm_processes_ops.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dwiegand <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/06/30 16:11:21 by dwiegand          #+#    #+#             */
/*   Updated: 2019/07/03 17:59:45 by dwiegand         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "virtual_machine.h"

#include "./../../libft/sources/ft_vector/ft_vector_assets.h"
#include "./../../libft/sources/ft_binary_heap/ft_binary_heap_assets.h"

int		load_process(t_area *area, int32_t player, uint32_t pc)
{
	t_process	*new;

	new = NULL;
	if (!(new = (t_process *)ft_memalloc(sizeof(t_process))))
		return 0;
	new->player = (int32_t)player;
	new->reg[0] = ~player;
	new->pc = pc;
	new->sleep = SN_CYCLES + 1;
	new->f = g_ops[0].f;
	//new->sleep = SN_CYCLES + get_process_sleep(new, MAP[new->pc]);
	new->ordinal_number = area->g_stats.next_process_index++;
	SN_PROCESS++;
	return ft_bheap_insert(area->processes, new, &heap_cmp);
}

int		new_process(t_area *area, t_process *process, uint32_t pc)
{
	t_process	*new;

	new = NULL;
	if (!(new = (t_process *)ft_memalloc(sizeof(t_process))))
		return 0;
	*new = *process;
	for (int i = 0; i < 16; i++)
	{
		new->reg[i] = process->reg[i];
	}
	new->pc = SHIFT(pc);
	new->sleep = SN_CYCLES + 1;
	new->f = g_ops[0].f;
	//new->sleep = SN_CYCLES + get_process_sleep(new, MAP[new->pc]);
	if (area->flags & STEP_DEBUG && SN_CYCLES >= g_db_from)
	{
		printf(">> new_process:\n>> op_name: %s (%.2hhx)\n>> process pc: %d\n>> run_round: %d\n",
				g_ops[((MAP[new->pc] > 0 && MAP[new->pc] < 17) ? MAP[new->pc] : 0)].name,
				MAP[new->pc],
				new->pc,
				new->sleep);
	}
	new->ordinal_number = area->g_stats.next_process_index++;
	SN_PROCESS++;
	return ft_bheap_insert(area->processes, new, &heap_cmp);

}

int32_t			delete_not_live_processes(t_area *area)
{
	size_t		index;
	size_t		length;
	t_vector	*v;

	v = area->processes;
	length = area->processes->size(area->processes);
	index = 0;
	while (index < length)
	{
		if (((t_process *)(v->v[index]))->live_in_session == false)
		{
			free(v->v[index]);
			v->v[index] = NULL;
			V_DATA(v)->end--;
			length--;
			ft_bheap_swap(v->v + index, v->v + length);
			SN_PROCESS--;
		}
		else
		{
			((t_process *)(v->v[index]))->live_in_session = false;
			index++;
		}
	}
	ft_bheap_init(v, &heap_cmp);
	return (1);
}