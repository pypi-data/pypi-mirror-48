
AMPLPY
------

AMPL API is an interface that allows developers to access the features of the
AMPL interpreter from within a programming language. All model generation and
solver interaction is handled directly by AMPL, which leads to great stability
and speed; the library just acts as an intermediary, and the added overhead
(in terms of memory and CPU usage) depends mostly on how much data is read
back from AMPL, the size of the model as such is irrelevant. Functions for
directly assigning data to AMPL parameters and sets are provided, which can
be used instead of the normal AMPL data reading procedures.  AMPL API has been
written with usability in mind, and it is easy to access its functionalities
from C++, Java, C#, MATLAB, R and Python.

The AMPL API can function as an add-on to any existing AMPL installation. If
you do not yet have an AMPL installation on the computer where you will be
working with the API, see our
`demo page <http://ampl.com/try-ampl/download-a-free-demo/>`_
or
`trial page <http://ampl.com/try-ampl/request-a-full-trial/>`_
to download a working version that can be installed quickly.

Documentation:
``````````````

* http://amplpy.readthedocs.io
* http://ampl.com/api/nightly/python/

Repositories:
`````````````

* GitHub Repository: https://github.com/ampl/amplpy
* PyPI Repository: https://pypi.python.org/pypi/amplpy


