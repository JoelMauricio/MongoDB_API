#!/usr/bin/env sh

source ./.env
uvicorn main:app --reload --host $HOST --port $PORT