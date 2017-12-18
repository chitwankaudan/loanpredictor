#Setting up enviroment
env : environment.yml
	conda env create -f environment.yml

process : data/
	mkdir processed/
	python assemble.py


