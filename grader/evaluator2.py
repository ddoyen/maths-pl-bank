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
    
    if 'feedback' in dic:
        feedback2= dic['feedback']
    
    if score==-1:
        feedback="""<div style='margin-bottom: 15px;padding: 4px 12px;background-color: #e7f3fe;border-left: 6px solid #2196F3;'>
        <p><strong>Attention !</strong> {} </p>
        </div>""".format(feedback2)
    elif score==100:
        feedback="""<div style='  margin-bottom: 15px;padding: 4px 12px;background-color: #ddffdd;border-left: 6px solid #4CAF50;'>
        <p><strong>Bonne réponse. </strong> {} </p>
        </div>""".format(feedback2)
    else:
        feedback="""<div style='  margin-bottom: 15px;padding: 4px 12px;background-color: #ffffcc;border-left: 6px solid #ffeb3b;'>
        <p><strong>Réponse incorrecte. </strong> {} </p>
        </div>""".format(feedback2)


    output(score,feedback,dic)


