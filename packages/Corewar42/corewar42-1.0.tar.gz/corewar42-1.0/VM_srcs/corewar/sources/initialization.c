/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   initialization.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dwiegand <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/05/27 16:55:36 by dwiegand          #+#    #+#             */
/*   Updated: 2019/07/02 22:37:35 by dwiegand         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "virtual_machine.h"

t_area		*initialization_area(void)
{
	t_area		*area;

	area = NULL;
	if (!(area = ft_memalloc(sizeof(t_area))))
		return NULL;
	area->map = NULL;
	if (!(area->map = ft_memalloc(sizeof(char) * MEM_SIZE)))
	{
		free(area);
		return (NULL);
	}
	area->processes = ft_vector_create(200, &delete_process);
	SDIE_CYCLE_DELTA = CYCLE_TO_DIE;
	SDIE_CYCLE = SDIE_CYCLE_DELTA;
	SNOT_CHANGED = 0;
	SN_CYCLES = 0;
	SDUMP_CYCLE = -1;
	area->win = -1;
	area->g_stats.next_process_index = 0;
	return (area);
}
