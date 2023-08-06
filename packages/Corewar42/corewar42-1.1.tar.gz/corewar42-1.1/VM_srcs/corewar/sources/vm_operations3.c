/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   vm_operations3.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: axtazy <marvin@42.fr>                      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/05/30 10:50:49 by axtazy            #+#    #+#             */
/*   Updated: 2019/06/05 14:33:28 by axtazy           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "virtual_machine.h"

int		ldi_op(t_area *area, t_process *process) // dir_size = 2a
{
	int32_t			result;
	uint32_t		shift;

	shift = 2;
	if (RDI_T(OCT00) && RD_T(OCT01) && R_T(OCT02)
		&& check_registers(area, process, 3, 2))
	{
		result = get_argument2(area, process, &shift, OCT00);
		if (I_T(OCT00))		// ???
			result %= IDX_MOD;
		result += get_argument2(area, process, &shift, OCT01);
		if (IS_REG(PPC(shift)))
		{
			PREG(PPC(shift)) = get32(area, process, result % IDX_MOD);
		}
	}
	PC = SHIFT(2 + shift_size(PPC(1), 3, 2));
	return 1;
}

int		sti_op(t_area *area, t_process *process) // dir_size = 2a
{
	int32_t		result;
	uint32_t	shift;
	uint32_t	fshift;

	shift = 3;
	fshift = shift_size(PPC(1), 3, 2);
	if (R_T(OCT00) && RDI_T(OCT01) && RD_T(OCT02)
		&& check_registers(area, process, 3, 2))
	{
			result = get_argument2(area, process, &shift, OCT01);
			result += get_argument2(area, process, &shift, OCT02);
			set32(area, process, result % IDX_MOD, PREG(PPC(2)));
	}
	PC = SHIFT(2 + fshift);
	return 1;
}

int		fork_op(t_area *area, t_process *process) // dir_size = 2
{
	int32_t		result;

	result = get16(area, process, 1);
	if ((new_process(area, process, result % IDX_MOD)) == 0)
		return (0);
	PC = SHIFT(3);
	return 1;
}

int		lld_op(t_area *area, t_process *process) // dir_size = 4ca
{
	int32_t		result;
	uint32_t	shift;

	shift = 2;
	if (DI_T(OCT00) && R_T(OCT01))
	{
		result = get_argument(area, process, &shift, OCT00);
		if (IS_REG(PPC(shift)))
		{
			PREG(PPC(shift)) = result;
			CARRY = ((result == 0) ? true : false);
		}
	}
	PC = SHIFT(2 + shift_size(PPC(1), 2, 4));
	return 1;
}

int		lldi_op(t_area *area, t_process *process) // dir_size = 2ca
{
	int32_t			result;
	uint32_t		shift;

	shift = 2;
	if (RDI_T(OCT00) && RD_T(OCT01) && R_T(OCT02)
		&& check_registers(area, process, 3, 2))
	{
		result = get_argument2(area, process, &shift, OCT00);
		if (I_T(OCT00))
			result %= IDX_MOD;
		result += get_argument2(area, process, &shift, OCT01);
		PREG(PPC(shift)) = get32(area, process, result);
		CARRY = (PREG(PPC(shift)) == 0) ? true : false;
	}
	PC = SHIFT(2 + shift_size(PPC(1), 3, 2));
	return 1;
}