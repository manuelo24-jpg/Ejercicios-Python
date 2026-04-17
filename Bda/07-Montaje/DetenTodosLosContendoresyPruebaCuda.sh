#!/bin/bash
clear
LISTACONTENEDORESACTIVOS=$(docker ps -q)
if [ -n "$LISTACONTENEDORESACTIVOS" ]; then
	echo -e "\e[32m Parando contenedores activos...\e[0m"
	docker stop $LISTACONTENEDORESACTIVOS
fi
echo -e "\e[32mLlamando desde la terminal a nvidia-smi"
echo -e "*******************************************************************\e[0m"
nvidia-smi


echo -e "\e[32mProbando nvidia-smi desde contenedor nvidia"
echo -e "*******************************************************************\e[0m"
docker run --rm --device nvidia.com/gpu=all nvidia/cuda:12.6.0-base-ubuntu24.04 nvidia-smi
