#!/bin/bash
cd "$(dirname "$0")"
export PARENT_MODE=1
echo "Starting Parent View..."
( sleep 2 && open "http://127.0.0.1:5151" ) &
python3 app.py
