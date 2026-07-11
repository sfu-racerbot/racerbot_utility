.PHONY: sim sim-teleop

sim:
	python3 cli.py start-sim

sim-teleop:
	python3 cli.py start-sim --teleop
