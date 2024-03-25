#!/bin/bash

if ! [ -e .env ]; then
	echo """
POSTGRES_DB=users
POSTGRES_USER=foundernest
POSTGRES_PASSWORD=password
API_TOKEN=
API_URL=
	""" > .env
fi