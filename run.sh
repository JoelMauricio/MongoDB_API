source ./.env
uvicorn main:app --workers 4 --host $HOST --port $PORT