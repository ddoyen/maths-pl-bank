#!/usr/bin/env python3
# coding: utf-8

import sys, json, jsonpickle
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
    
    if 'before' in dic:
        glob = {}
        dic['StopBeforeExec'] = StopBeforeExec
        code=""
        if 'headbefore' in dic:
            code+=dic['headbefore']+ '\n'
        code+=dic['before']+ '\n'
        if 'footerbefore' in dic:
            code+=dic['footerbefore']
        exec(add_try_clause(code, StopBeforeExec), dic)
        exec("", glob)
        for key in glob:
            if key in dic and dic[key] == glob[key]:
                del dic[key]
    else:
        print(("Builder 'before2' need a script declared in the key 'before'. "
               + "See documentation related to this builder."),
              file = sys.stderr)
        sys.exit(1)

    dic['nbattempt']=0

    dic['inputmode'] = "initial"    
    
    dic['form0']=dic['form']+"\n <div style='width:100%;height:200px;'></div>"

    dic['form']=build_form(dic['form0'],dic)

    if 'pagestyle' in dic:
        dic['form']+="""
            <style>
            {}
            </style>
            """.format(dic['pagestyle'])

    with open(output_json, "w+") as f:
        f.write(jsonpickle.encode(dic, unpicklable=False))
    
    sys.exit(0)






