#!/usr/bin/env python3
# coding: utf-8

import sys, json, jsonpickle, time

from sandboxio import output, get_context, get_answers


class StopEvaluatorExec(Exception):
    pass


def add_try_clause(code, excpt):
    """Add a try/except clause, excepting 'excpt' around code."""
    code = code.replace('\t', '    ')
    return ("try:\n" + '\n'.join(["    " + line for line in code.split('\n')])
            + "\nexcept " + excpt.__name__ + ":\n    pass")


missing_evaluator_main_stderr = """\
The key 'evaluator_main' was not found in the context.
When using this grader, the PL must declare a script inside a key 'evaluator'. This script have
access to every variable declared in the PL and its 'before' script.
It should declare a variable 'grade' which should contain a tuple (int, feedback) where int is the grade between [0, 100]."""

missing_score_stderr = """\
'evaluator' did not declare the variable 'score'.
The script have access to every variable declared in the PL and its 'before' script.
It should declare a variable 'grade' which should contain a tuple (int, feedback) where int is the grade between [0, 100]."""

if __name__ == "__main__":
    if len(sys.argv) < 5:
        msg = ("Sandbox did not call grader properly:\n"
               +"Usage: python3 grader.py [input_json] [output_json] [answer_file] [feedback_file]")
        print(msg, file=sys.stderr)
        sys.exit(1)
    
    dic = get_context()
    dic['response'] = get_answers()
    if 'eval_main' in dic:
        glob = {}
        dic['StopEvaluatorExec'] = StopEvaluatorExec
        code=""
        if 'eval_head' in dic:
            code+=dic['eval_head']
        if 'eval_param' in dic:
            code+=dic['eval_param']
        code+=dic['eval_main']
        if 'eval_feedback' in dic:
            code+=dic['eval_feedback']
        exec(add_try_clause(code, StopEvaluatorExec), dic)
        exec("", glob)
        for key in glob:
            if key in dic and dic[key] == glob[key]:
                del dic[key]
    else:
        print(missing_evaluator_stderr, file=sys.stderr)
        sys.exit(1)
    
    if 'score' not in dic:
        print(missing_grade_stderr, file=sys.stderr)
        sys.exit(1)
    score=dic['score']    
    
    if score==-1:
        feedback="<span style='color:blue'>Attention ! </span>"
    elif score==100:
        feedback="<span style='color:green'>Bonne réponse. </span>"
    else:
        feedback="<span style='color:orange'>Réponse incorrecte. </span>"
    
    if dic['feedback']:
        feedback+= dic['feedback']
    

    output(score,feedback,dic)

