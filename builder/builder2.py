#!/usr/bin/env python3
# coding: utf-8

import sys, json, jsonpickle


class StopBeforeExec(Exception):
    pass


def add_try_clause(code, excpt):
    """Add a try/except clause, excepting 'excpt' around code."""
    code = code.replace('\t', '    ')
    return ("try:\n" + '\n'.join(["    " + line for line in code.split('\n')])
            + "\nexcept " + excpt.__name__ + ":\n    pass")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        msg = ("Sandbox did not call builder properly:\n"
               +"Usage: python3 builder.py [input_json] [output_json]")
        print(msg, file=sys.stderr)
        sys.exit(1)
    input_json = sys.argv[1]
    output_json = sys.argv[2]
    
    with open(input_json, "r") as f:
        dic = json.load(f)
    
    if 'form_help' in dic:
        if dic['form_help']!="":
            dic['form']+="""
            <details>
            <summary>Syntaxe attendue.</summary>
            {}
            </details>
            """.format(dic['form_help'])
    
    if 'builder_main' in dic:
        glob = {}
        dic['StopBeforeExec'] = StopBeforeExec
        code=""
        if 'builder_head' in dic:
            code+=dic['builder_head']
        if 'builder_param' in dic:
            code+=dic['builder_param']
        code+=dic['builder_main']
        if 'builder_statement' in dic:
            code+=dic['builder_statement']
        exec(add_try_clause(code, StopBeforeExec), dic)
        exec("", glob)
        for key in glob:
            if key in dic and dic[key] == glob[key]:
                del dic[key]
    else:
        print(("Builder 'before' need a script declared in the key 'before'. "
               + "See documentation related to this builder."),
              file = sys.stderr)
        sys.exit(1)
            
    with open(output_json, "w+") as f:
        f.write(jsonpickle.encode(dic, unpicklable=False))
    
    sys.exit(0)


