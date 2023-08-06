/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dwiegand <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/05/29 16:45:37 by axtazy            #+#    #+#             */
/*   Updated: 2019/07/04 20:58:26 by dwiegand         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "virtual_machine.h"

int32_t		virtual_machine(u_char *p1, int p1_size, u_char *p2, int p2_size)
{
	int32_t		game_status;
	t_area		*area;

	area = NULL;
	if ((area = initialization_area()) == NULL)
		return 0;
	if ((read_arguments(area, p1, p2, p1_size, p2_size)) == 0)
		return 0;
	game_status = play_game(area);

	free_args(&area);
	return game_status;
}
