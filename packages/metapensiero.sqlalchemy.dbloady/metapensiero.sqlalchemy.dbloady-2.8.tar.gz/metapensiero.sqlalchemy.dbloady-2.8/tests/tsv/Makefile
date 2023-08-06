# -*- coding: utf-8 -*-
# :Project:   metapensiero.sqlalchemy.dbloady -- TSV functional test
# :Created:   lun 24 giu 2019 18:23:05 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2019 Lele Gaifax
#

PYTHON3 ?= python3.7

.PHONY: test
test: env
	env/bin/python test.py

env:
	$(PYTHON3) -m venv env
	env/bin/pip install --upgrade pip
	env/bin/pip install sqlalchemy
	env/bin/pip install -e ../.. .

.PHONY: clean
clean:

.PHONY: realclean
realclean: clean
	rm -rf env __pycache__ testdbloady.egg-info
