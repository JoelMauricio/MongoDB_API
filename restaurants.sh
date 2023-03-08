source ./.env
uvicorn restaurants:app --reload --host $HOST --port $PORT