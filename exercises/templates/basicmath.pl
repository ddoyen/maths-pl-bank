@ lib:/utils/sandboxio.py
@ /utils/plrandom.py [plrandom.py]
@ /utils/utilsmath.py [utilsmath.py]
@ /utils/prettyfb.py [prettyfb.py]
@ /builder/before2.py [builder.py]
@ /grader/evaluator2.py [grader.py]

title = Title

headbefore ==
from plrandom import rd
rd.seed(seed)
import sympy as sp
import utilsmath as ut
if 'latexparam' in locals():
    ut.LatexPrinter._settings.update(eval(latexparam))
==

before ==
==

footerbefore ==
_strsympyvar={}
for _namevar in list(locals().keys()):
    if isinstance(locals()[_namevar],(sp.Basic,sp.Matrix)):
        _strsympyvar[_namevar]=str(locals()[_namevar])
==

form==
<div class="input-group">
<input id="form_1" type="text" class="form-control" value="{{ answers__.1 }}" required/>
</div>
==



headevaluator ==
import sympy as sp
import utilsmath as ut
import prettyfb as fb
if 'latexparam' in locals():
    ut.LatexPrinter._settings.update(eval(latexparam))
for _namevar in list(_strsympyvar.keys()):
    with sp.evaluate(False):
        locals()[_namevar]=sp.sympify(_strsympyvar[_namevar])
==

evaluator ==
==






