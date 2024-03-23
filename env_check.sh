#!/bin/bash

if ! [ -e .env ]; then
	echo """
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
API_TOKEN=
API_URL=
	""" > .env
fi