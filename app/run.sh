#bin/bash

python3 src/get_data.py ./test_data.csv
python3 src/analise_data.py ./test_data.csv
python3 src/create_model.py 
while true; do
  sleep 1
done