/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   vm_operations2.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dwiegand <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/05/30 10:50:20 by axtazy            #+#    #+#             */
/*   Updated: 2019/06/13 18:42:40 by dwiegand         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "virtual_machine.h"

int			sub_op(t_area *area, t_process *process) // dir_size = 4ca
{
	if (R_T(OCT00) && R_T(OCT01) && R_T(OCT02))
	{
		if (IS_REG(PPC(2)) && IS_REG(PPC(3)) && IS_REG(PPC(4)))
		{
			PREG(PPC(4)) = PREG(PPC(2)) - PREG(PPC(3));
			CARRY = ((PREG(PPC(4)) == 0) ? true : false);
		}
	}
	PC = SHIFT(2 + shift_size(PPC(1), 3, 4));
	return 1;
}

int			and_op(t_area *area, t_process *process) // dir_size = 4ca
{
	uint32_t	shift;
	int32_t		result;

	shift = 2;
	if (RDI_T(OCT00) && RDI_T(OCT01) && R_T(OCT02)
		&& check_registers(area, process, 3, 4))
	{
		result = get_argument(area, process, &shift, OCT00);
		result &= get_argument(area, process, &shift, OCT01);
		PREG(PPC(shift)) = result;
		CARRY = ((result == 0) ? true : false);
	}
	PC = SHIFT(2 + shift_size(PPC(1), 3, 4));
	return 1;
}

int			or_op(t_area *area, t_process *process) // dir_size = 4ca
{
	uint32_t	shift;
	int32_t		result;

	shift = 2;
	if (RDI_T(OCT00) && RDI_T(OCT01) && R_T(OCT02)
		&& check_registers(area, process, 3, 4))
	{
		result = get_argument(area, process, &shift, OCT00);
		result |= get_argument(area, process, &shift, OCT01);
		PREG(PPC(shift)) = result;
		CARRY = ((result == 0) ? true : false);
	}
	PC = SHIFT(2 + shift_size(PPC(1), 3, 4));
	return 1;
}

int			xor_op(t_area *area, t_process *process) // dir_size = 4ca
{
	uint32_t	shift;
	int32_t		result;

	shift = 2;
	if (RDI_T(OCT00) && RDI_T(OCT01) && R_T(OCT02)
		&& check_registers(area, process, 3, 4))
	{
		result = get_argument(area, process, &shift, OCT00);
		result ^= get_argument(area, process, &shift, OCT01);
		PREG(PPC(shift)) = result;
		CARRY = ((result == 0) ? true : false);
	}
	PC = SHIFT(2 + shift_size(PPC(1), 3, 4));
	return 1;
}

int			zjmp_op(t_area *area, t_process *process) // dir_size = 2
{
	if (CARRY == true)
		PC = ISHIFT(((int32_t)get16(area, process, 1)));
	else
		PC = SHIFT(3);
	return 1;
}