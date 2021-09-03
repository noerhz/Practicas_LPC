#!/bin/bash
# Menu simple en bash

nombres='Noe Alfredo Jorge Salir'
PS3='Seleccione una opcion: '

select nombre in $nombres
do
	if [ $nombre == 'Salir' ]
	then
		break
	fi
	echo Hola $nombre
done

echo Adios