texliste.pdf: texliste.tex liste.txt
	pdflatex $<

liste.txt: *.py
	ls *.py | sort > liste.txt
	python makelist.py liste.txt $@

clean: liste.txt texliste.aux texliste.log
	rm $^
