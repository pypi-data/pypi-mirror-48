python -m cProfile -s time -o t.prof speed_iba_exp_passive.py
echo "Run:"
echo "snakeviz t.prof"
