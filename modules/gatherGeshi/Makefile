include ../Makefile.vars
resultsdir = ${results101dir}
repo = ${resultsdir}/101repo
orig = ${repo}/technologies/geshi
result = ${resultsdir}/geshi/src/geshi

run:
	@cp -r ${orig} ${resultsdir}
	@python program.py ${repo} ${result}

clean:
	@#no-op
