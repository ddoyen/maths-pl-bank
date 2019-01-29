@ /utils/sandboxio.py
@ /utils/plrandom.py [plrandom.py]
@ /utils/utilsmath.py [utilsmath.py]
@ /utils/prettyfb.py [prettyfb.py]
@ /builder/builder2.py [builder.py]
@ /grader/evaluator2.py [grader.py]

title = Title

headbefore ==
from plrandom import rd
rd.seed(seed)
import sympy as sp
import utilsmath as ut
if 'param' in locals():
    ut.LatexPrinter._settings.update(eval(param))
==

before ==
==

form==
<div class="input-group">
<input id="form_answer" type="text" class="form-control" value="{{ answers__.answer }}" required/>
</div>
==



headevaluator ==
import sympy as sp
import utilsmath as ut
import prettyfb as fb
if 'param' in locals():
    ut.LatexPrinter._settings.update(eval(param))
==

evaluator ==
==




