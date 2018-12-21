All: ejecutarpy compilartex eliminartex

ejecutarpy:
	python relatividad.py

compilartex:
	pdflatex Cantidades_relativistas.tex

eliminartex:
	rm *p.tex *.aux *.log
