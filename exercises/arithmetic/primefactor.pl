extends = /template/mathexpr.pl

title = Décomposition en facteurs premiers

lang = fr

virtualKeyboards = elementary

text ==
Décomposer $% {{n}} %$ en produit de facteurs premiers.
==

textError %=
{"1": "Votre réponse n'est pas un produit de facteurs entiers.",
"2": "Votre réponse n'est pas un produit de facteurs premiers.",
"3": "Votre réponse n'est pas égale à $% {number} %$"}
==

before ==
while True:
    n=randint(10,100)
    dicfactors=factorint(n)
    if sum(list(dicfactors.values()))>2:
        break
==

evaluator==
def list2dicfactors(listfactors):
    dicfactors={}
    for f in listfactors:
        if type(f)==sp.Pow:
            if isinstance(f.args[0],sp.Integer) and isinstance(f.args[1],sp.Integer):
                p=f.args[0]
                k=f.args[1]
            else:
                raise ValueError
        elif isinstance(f,sp.Integer):
            p=f
            k=1
        else:
            raise ValueError
        if p in dicfactors:
            dicfactors[p]+=k
        else:
            dicfactors[p]=k
    return dicfactors
try:
    ans=str2expr(answer['1'])
    if type(ans)==sp.Mul:
        dicfactors=list2dicfactors(ans.args)
    else:
        dicfactors=list2dicfactors([ans])
    if not all(isprime(p) for p in dicfactors.keys()):
        score=0
        feedback=textError['2']
    elif not is_equal(ans,n):
        score=0
        feedback=textError['3'].format(number=n)
    else:
        score=100
        feedback=""
except:
    score=-1
    feedback=textError['1']
==
