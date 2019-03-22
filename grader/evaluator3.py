#!/usr/bin/env python3
# coding: utf-8

import sys, json, jsonpickle, time

from sandboxio import output, get_context, get_answers

from jinja2 import Template

def build_form(template_form,dic):
    dinput=dic['input']
    script=""
    links=""
    contextform={}
    for name,config in dinput.items():
        type=config['type']
        context = {**config,**dic,'name':name}
        contextform['input_'+name]=Template(dic[type+'_container']).render(context)
        script=script+'\n'+Template(dic[type+'_script']).render(context)
        links=links+dic[type+'_links']
    form=links
    form+=Template(template_form).render(contextform)
    form+="""
                <script>
                {}
                </script>
                """.format(script)
    return form

def format_analysis(msg,text,n,lang):
    dcls={'warning':'alert-info','retry':'alert-warning','fail':'alert-danger','success':'alert-success'}
    ditext={'en':{'warning':'Warning !','retry':'Try again !','fail':'Fail.','success':'Good.'},
        'fr':{'warning':'Attention !','retry':'Essaie encore !','fail':'Mauvaise réponse.','success':'Bonne réponse.'}}
    cls=dcls[msg]
    itext=ditext[lang][msg]
    if msg=='warning' or msg=='retry':
        format_text="""<div class="alert {}">
  <strong>{}</strong> {} <br> Il reste {} tentatives.</div>""".format(cls,itext,text,n)
    else:
        format_text="""<div class="alert {}">
  <strong>{}</strong> {}</div>""".format(cls,itext,text)
    return format_text


class StopEvaluatorExec(Exception):
    pass


def add_try_clause(code, excpt):
    """Add a try/except clause, excepting 'excpt' around code."""
    code = code.replace('\t', '    ')
    return ("try:\n" + '\n'.join(["    " + line for line in code.split('\n')])
            + "\nexcept " + excpt.__name__ + ":\n    pass")

missing_evaluator_stderr = """\
The key 'evaluator' was not found in the context.
When using this grader, the PL must declare a script inside a key 'evaluator'. This script have
access to every variable declared in the PL and its 'before' script."""

missing_score_stderr = """\
'evaluator' did not declare the variable 'score'.
The script have access to every variable declared in the PL and its 'before' script.
It should declare a variable 'score' which should contain an integer between [0, 100]."""

if __name__ == "__main__":
    if len(sys.argv) < 5:
        msg = ("Sandbox did not call grader properly:\n"
               +"Usage: python3 grader.py [input_json] [output_json] [answer_file] [feedback_file]")
        print(msg, file=sys.stderr)
        sys.exit(1)
    
    dic = get_context()
    dic['answer'] = get_answers()
    if 'evaluator' in dic:
        glob = {}
        dic['StopEvaluatorExec'] = StopEvaluatorExec
        code=""
        if 'headevaluator' in dic:
            code+=dic['headevaluator']+'\n'
        code+=dic['evaluator']+'\n'
        if 'footerevaluator' in dic:
            code+=dic['footerevaluator']
        exec(add_try_clause(code, StopEvaluatorExec), dic)
        exec("", glob)
        for key in glob:
            if key in dic and dic[key] == glob[key]:
                del dic[key]
    else:
        print(missing_evaluator_stderr, file=sys.stderr)
        sys.exit(1)

    if 'score' in dic:
        score=dic['score']    
    else:
        print(missing_score_stderr, file=sys.stderr)
        sys.exit(1)

    if 'maxattempt' in dic:
        maxattempt=int(dic['maxattempt']) 
    else:
        maxattempt=1

    if 'feedback' in dic:
        feedback= dic['feedback']
    else:
        feedback=""

    if 'lang' in dic:
        lang= dic['lang']
    else:
        lang="fr"

    
    if score>-1:
        dic['nbattempt'] +=1

    nbattempt=dic['nbattempt']

    if (dic['nbattempt'] < int(dic['maxattempt'])) and score<100:
        dic['inputmode'] = "retry"
    else:
        dic['inputmode'] = "final"

    if score==100:
        format_feedback=format_analysis('success',feedback,0,lang)
    elif score==-1:
        format_feedback=format_analysis('warning',feedback,maxattempt-nbattempt,lang)
    else:
        if nbattempt<maxattempt:
            format_feedback=format_analysis('retry',feedback,maxattempt-nbattempt,lang)
        else:
            format_feedback=format_analysis('fail',feedback,0,lang)


    dic['form']=build_form(dic['form0'],dic)

    if 'pagestyle' in dic:
        dic['form']+="""
            <style>
            {}
            </style>
            """.format(dic['pagestyle'])


    output(score,format_feedback,dic)
