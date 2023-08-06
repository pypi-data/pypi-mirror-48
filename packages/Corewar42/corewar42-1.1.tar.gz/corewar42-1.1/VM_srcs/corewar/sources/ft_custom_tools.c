/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_custom_tools.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dwiegand <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/06/30 17:13:50 by dwiegand          #+#    #+#             */
/*   Updated: 2019/07/03 18:50:36 by dwiegand         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "virtual_machine.h"
#include "./../../libft/sources/ft_vector/ft_vector_assets.h"
#include "./../../libft/sources/ft_binary_heap/ft_binary_heap_assets.h"

inline int32_t	get_next_op_round(t_vector *p)
{
	return (((t_process *)(V_DATA(p)->begin[0]))->sleep);
}

inline void		move_first_process(t_vector *p)
{
	ft_bheap_sift_down(p, 0, &heap_cmp);
}

void			delete_process(void **p)
{
	if (p != NULL)
	{
		if (*p != NULL)
		{
			free(*p);
			*p = NULL;
		}
	}
}

int32_t			heap_cmp(void *p1, void *p2)
{
	if (((t_process *)p1)->sleep < ((t_process *)p2)->sleep)
		return (-1);
	else if (((t_process *)p1)->sleep == ((t_process *)p2)->sleep
		&& (((t_process *)p1)->ordinal_number
		> ((t_process *)p2)->ordinal_number))
		return (-1);
	else
		return (1);
}
