#!/usr/bin/env python3
# coding: utf-8

import sys, json, jsonpickle, time

from sandboxio import output, get_context, get_answers

def format_analysis(score,text,lang):
    if lang=='en':
        warning="Warning !"
        goodans="Good answer."
        badans="Bad answer."
    if lang=='fr':
        warning="Attention !"
        goodans="Bonne réponse."
        badans="Mauvaise réponse."    
    if score==-1:
        color1='#e7f3fe'
        color2='#2196F3'
        msg=warning
    elif score==100:
        color1='#ddffdd'
        color2='#4CAF50'
        msg=goodans
    else:
        color1='#ffffcc'
        color2='#ffeb3b'
        msg=badans
    format_text="""<div style='margin-bottom: 15px;padding: 4px 12px;background-color: {};border-left: 6px solid {}'>
            <p><strong>{}</strong> {} </p>
            </div>""".format(color1,color2,msg,text)
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
        code+=dic['evaluator']
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
    
    if 'feedback' in dic:
        feedback= dic['feedback']
    else:
        feedback=""

    if 'lang' in dic:
        lang= dic['lang']
    else:
        lang="fr"

    format_feedback=format_analysis(score,feedback,lang)  

    output(score,format_feedback,dic)








