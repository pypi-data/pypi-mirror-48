/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   vm_ops_methods.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dwiegand <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/06/04 01:03:50 by axtazy            #+#    #+#             */
/*   Updated: 2019/06/13 18:32:10 by dwiegand         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "virtual_machine.h"

uint32_t	shift_size(uint8_t arg_byte, int32_t arg_n, uint32_t dir_size)
{
	uint32_t	shift;

	shift = 0;
	arg_byte >>= (4 - arg_n) * 2;
	while (arg_n)
	{
		if (D_T((arg_byte & 0x03)))
			shift += dir_size;
		else if (I_T((arg_byte & 0x03)))
			shift += 2;
		else if (R_T((arg_byte & 0x03)))
			shift += 1;
		arg_byte >>= 2;
		arg_n--;
	}
	return (shift);
}

int32_t		get_argument(t_area *area,
							t_process *process,
							uint32_t *shift,
							uint8_t type)
{
	if (R_T(type))
	{
		*shift += 1;
		return (PREG(PPC(*shift - 1)));
	}
	else if (D_T(type))
	{
		*shift += 4;
		return (get32(area, process, *shift - 4));
	}
	else
	{
		*shift += 2;
		return (get32(area,
				process, get16(area, process, *shift - 2) % IDX_MOD));
	}
}


int32_t		get_argument2(t_area *area,
							t_process *process,
							uint32_t *shift,
							uint8_t type)
{
	if (R_T(type))
	{
		*shift += 1;
		return (PREG(PPC(*shift - 1)));
	}
	else if (D_T(type))
	{
		*shift += 2;
		return (get16(area, process, *shift - 2));
	}
	else
	{
		*shift += 2;
		return (get32(area,
				process, get16(area, process, *shift - 2) % IDX_MOD));
	}
}

/* - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - */

int 		escape(uint8_t arg, int32_t dir_size)
{
	if (R_T(arg))
		return (1);
	else if (I_T(arg))
		return (2);
	else
		return (dir_size);
}

int 		check_registers(t_area *area,
							t_process *process,
							int32_t	n_args,
							int32_t	dir_size)
{
	uint8_t		args_type;
	int32_t		shift;

	shift = 2;
	args_type = PPC(1);
	while (n_args)
	{
		if (R_T((args_type & 0xC0) >> 6) && !IS_REG(PPC(shift)))
			return (0);
		shift += escape((args_type & 0xC0) >> 6, dir_size);
		args_type <<= 2;
		n_args--;
	}
	return (1);
}