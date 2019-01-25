@ /utils/sandboxio.py
@ /utils/plrandom.py [plrandom.py]
@ /utils/utilsmath.py [utilsmath.py]
@ /builder/builder2.py [builder.py]
@ /grader/evaluator2.py [grader.py]

title = Title

builder_head ==
from plrandom import rd
rd.seed(seed)
import sympy as sp
import utilsmath as ut
==

builder_main ==
pass
==

builder_statement ==
text = "Statement"
==

form==
<div class="input-group">
<input id="form_answer" type="text" class="form-control" value="{{ answers__.answer }}" required/>
</div>
==

eval_head==
import sympy as sp
import utilsmath as ut
==

eval_param ==
pass
==

eval_main==
score=100
==

eval_feedback==
==
