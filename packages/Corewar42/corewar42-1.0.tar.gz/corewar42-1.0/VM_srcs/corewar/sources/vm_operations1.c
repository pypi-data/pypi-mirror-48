/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   vm_operations1.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dwiegand <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/05/30 10:49:37 by axtazy            #+#    #+#             */
/*   Updated: 2019/07/03 20:21:48 by dwiegand         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "virtual_machine.h"

int			next_op(t_area *area, t_process *process) // dir_size = 4
{
	u_char	op_byte;

	op_byte = MAP[PC];
	if (op_byte > 0 && op_byte < 17)
	{
		process->f = g_ops[op_byte].f;
		process->sleep = SN_CYCLES + g_ops[op_byte].sleep - 1;
	}
	else
	{
		PC = SHIFT(1);
		process->f = g_ops[0].f;
		process->sleep = SN_CYCLES + 1;
	}
	return 1;
}

int			live_op(t_area *area, t_process *process) // dir_size = 4
{
	int32_t		value;

	LIVE_S = true;
	value = get32(area, process, 1);
	if (value > -5 && value < 0)
	{
		area->players[(~(value))].last_live = SN_CYCLES;
		area->win = ~value;
	}
	SLIVES_IN_ROUND++;
	PC = SHIFT(5);
	return 1;
}

int			ld_op(t_area *area, t_process *process) // dir_size = 4ca
{
	uint32_t	shift;
	int32_t 	result;

	shift = 2;
	if (DI_T(OCT00) && R_T(OCT01))
	{
		result = get_argument(area, process, &shift, OCT00);
//		if (I_T(OCT00))
//			result %= IDX_MOD;
		if (IS_REG(PPC(shift)))
		{
			PREG(PPC(shift)) = result;
			CARRY = ((result == 0) ? true : false);
		}
	}
	PC = SHIFT(2 + shift_size(PPC(1), 2, 4));
	return 1;
}

int			st_op(t_area *area, t_process *process) // dir_size = 4a
{
	uint32_t	shift;

	shift = shift_size(PPC(1), 2, 4);
	if (R_T(OCT00) && RI_T(OCT01)
	&& check_registers(area, process, 2, 4))
	{
		if (IS_REG(PPC(2)))
		{
			if (R_T(OCT01) && IS_REG(PPC(3)))
			{
				PREG(PPC(3)) = PREG(PPC(2));
			}
			else
			{
				set32(area, process,
						get16(area, process, 3) % IDX_MOD, PREG(PPC(2)));
			}
		}
	}
	PC = SHIFT(2 + shift);
	return 1;
}

int			add_op(t_area *area, t_process *process) // dir_size = 4ca
{
	if (R_T(OCT00) && R_T(OCT01) && R_T(OCT02))
	{
		if (IS_REG(PPC(2)) && IS_REG(PPC(3)) && IS_REG(PPC(4)))
		{
			PREG(PPC(4)) = PREG(PPC(2)) + PREG(PPC(3));
			CARRY = (PREG(PPC(4)) == 0) ? true : false;
		}
	}
	PC = SHIFT(2 + shift_size(PPC(1), 3, 4));
	return 1;
}