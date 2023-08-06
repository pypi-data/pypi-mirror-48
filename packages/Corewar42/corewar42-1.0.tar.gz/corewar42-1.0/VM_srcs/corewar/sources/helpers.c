/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   helpers.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: axtazy <marvin@42.fr>                      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/05/29 15:15:04 by axtazy            #+#    #+#             */
/*   Updated: 2019/06/10 03:31:09 by axtazy           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "virtual_machine.h"

void		bytes_reverse(void *param, size_t size)
{
	size_t 	i;
	char 	tmp;

	i = 0;
	while (i < size / 2)
	{
		tmp = *(((char *)param) + i);
		*(((char *)param) + i) = *(((char *)param) + size - 1 - i);
		*(((char *)param) + size - 1 - i) = tmp;
		i++;
	}
}

void		print_map(uint8_t *map)
{
	unsigned char	l;
	unsigned char	r;

	for (int i = 0; i < 64; i++)
	{
		for (int j = 0; j < 64; j++)
		{
			l = (((map[j + i * 64]) >> 4) & 0x0F);
			r = ((map[j + i * 64]) & 0x0F);
			if (l > 9)
				printf("%c", l % 10 + 'a');
			else
				printf("%c", l + '0');
			if (r > 9)
				printf("%c", r % 10 + 'a');
			else
				printf("%c", r + '0');
			printf(" ");
		}
		printf("\n");
	}
}
