/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   read_arguments.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dwiegand <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/05/27 16:55:36 by dwiegand          #+#    #+#             */
/*   Updated: 2019/07/04 20:58:26 by dwiegand         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "virtual_machine.h"

int32_t			set_code_to_map(const t_area* const restrict area,
								const u_char* const restrict ptr,
								const size_t length,
								const size_t start_pos )
{
	register size_t i = 0;
	while (i < length)
	{
		area->map[start_pos + i] = ptr[i];
		i++;
	}
	return 1;
}



int32_t			initialization_players(	t_area* const restrict area,
										const u_char* const restrict p1,
										const u_char* const restrict p2,
										const size_t length1,
										const size_t length2 )
{
	if (!(area->players = malloc(sizeof(t_player) * SN_PLAYERS)))
		return 0;
	area->players[0].ordinal_number = 1;
	area->players[0].start_pos = 0;
	area->players[0].last_live = 0;
	set_code_to_map(area, p1, length1, 0);
	load_process(area, 0, 0);

	area->players[1].ordinal_number = 2;
	area->players[1].start_pos = MEM_SIZE / 2;
	area->players[1].last_live = 0;
	set_code_to_map(area, p2, length2, MEM_SIZE / 2);
	load_process(area, 1,  MEM_SIZE / 2);
//	printf("Introducing contestants...\n");
//	printf("* Player %d, weighing %lu bytes, \"%s\" (\"%s\") !\n",
//			area->players[0].ordinal_number,
//			length1,
//			area->players[0].name,
//			area->players[0].comment);
//	printf("* Player %d, weighing %lu bytes, \"%s\" (\"%s\") !\n",
//			area->players[1].ordinal_number,
//			length2,
//			area->players[1].name,
//			area->players[1].comment);
	fflush(stdout);
	return (1);
}

int32_t		read_arguments(	t_area* const restrict area,
							const u_char* const restrict p1,
							const u_char* const restrict p2,
							const size_t length1,
							const size_t length2 )
{
	SN_PLAYERS = 2;
	return initialization_players(area, p1, p2, length1, length2);
}

