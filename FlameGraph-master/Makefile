# Default target
.PHONY: run
run:
	sudo perf record ./../main.exe -i ../inputs/pianoroom.ray --ppm -o ../output/pianoroom.ppm -H 500 -W 500

# Flamegraph target (modify as needed)
.PHONY: flame
flame:
	sudo perf script | ./stackcollapse-perf.pl > out.perf-folded
	sudo ./flamegraph.pl out.perf-folded > perf.svg
	sudo firefox perf.svgsudo perf script | ./stackcollapse-perf.pl > out.perf-folded

# Clean target
.PHONY: clean
clean:
	echo "nothing"

# Set default goal
.DEFAULT_GOAL := run
