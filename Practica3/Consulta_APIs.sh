#!/bin/bash

echo "Informacion de Dominios"

apiKey="API key personal"
var1=google.com
var2=twitter.com
var3=youtube.com
var4=telmex.com
var5=reddit.com

for ((i=1; $i <= 5; i = $i+1)); do
	if [[ $i == 1 ]]; then
		dominio=$var1
	elif [[ $i == 2 ]]; then 
		dominio=$var2
	elif [[ $i == 3 ]]; then
		dominio=$var3
	elif [[ $i == 4 ]]; then
		dominio=$var4
	elif [[ $i == 5 ]]; then
		dominio=$var5
	fi
	
	url="https://api.hunter.io/v2/domain-search?domain=${dominio}&api_key=${apiKey}"
	curl -X GET -v ${url} -o ${dominio}.txt
done