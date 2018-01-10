# Setting up enviroment
env : environment.yml
	conda env create -f environment.yml

# Assembles and cleans all files in data/ directory
process : data/
	mkdir processed/
	python assemble.py
	python clean.py

# Runs predictions and returns accuracy scores
predict : processed/
	python predict.py

