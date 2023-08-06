/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   vm_game.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dwiegand <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/06/30 17:23:31 by dwiegand          #+#    #+#             */
/*   Updated: 2019/07/04 21:54:46 by dwiegand         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "virtual_machine.h"

static int			func_index(int (*f)(t_area *, t_process *))
{
	for (int i = 0; i < 17; i++)
	{
		if (f == g_ops[i].f)
			return (i);
	}
	return (0);
}

static int			run_next_process(t_area *area)
{
	t_process *process;

	process = ft_bheap_get(area->processes);
	SN_CYCLES = process->sleep;
	if (process->f != g_ops[0].f)
	{
		if ((process->f(area, process)) == 0)
			return 0;
		process->f = g_ops[0].f;
		process->sleep = SN_CYCLES + 1;
	}
	else
		process->f(area, process);
	move_first_process(area->processes);
	return 1;
}

static void			change_area_stats(t_area *area)
{
	if (SLIVES_IN_ROUND >= NBR_LIVE)
	{
		SDIE_CYCLE_DELTA -= CYCLE_DELTA;
		SNOT_CHANGED = 0;
	}
	else
		SNOT_CHANGED++;
	if (SNOT_CHANGED >= MAX_CHECKS)
	{
		SDIE_CYCLE_DELTA -= CYCLE_DELTA;
		SNOT_CHANGED = 0;
	}
	if (SDIE_CYCLE_DELTA < 0)
		SDIE_CYCLE_DELTA = 0;
	SDIE_CYCLE += SDIE_CYCLE_DELTA;
	SCYCLE_INROUND = 0;
	SLIVES_IN_ROUND = 0;
}

int32_t				play_game(t_area *area)
{
	area->win = area->g_stats.n_players - 1;
	while (SN_PROCESS > 0)
	{
		if ((area->flags & DUMP) != 0
			&& ((get_next_op_round(area->processes)) > SDUMP_CYCLE
			&& SDIE_CYCLE > SDUMP_CYCLE))
			print_dump(area);
		if ((get_next_op_round(area->processes)) > SDIE_CYCLE)
		{
			delete_not_live_processes(area);
			change_area_stats(area);
		}
		else
			if ((run_next_process(area)) == 0)
				return 0;
	}
	return (area->players[area->win].ordinal_number);
}
