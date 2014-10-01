all: readstud.py
	python $<
	rm students.pickle

readstud.py: students.py
	python $<

clean: students.pickle
	rm $^
