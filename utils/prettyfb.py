

def msg_analysis(score,texterror,lang):
    if lang=='en':
        if score==-1:
            msg="""<div style='margin-bottom: 15px;padding: 4px 12px;background-color: #e7f3fe;border-left: 6px solid #2196F3;'>
            <p><strong>Warning !</strong> {} </p>
            </div>""".format(texterror)
        elif score==100:
            msg="""<div style='  margin-bottom: 15px;padding: 4px 12px;background-color: #ddffdd;border-left: 6px solid #4CAF50;'>
            <p><strong>Good answer. </strong> {} </p>
            </div>""".format(texterror)
        else:
            msg="""<div style='  margin-bottom: 15px;padding: 4px 12px;background-color: #ffffcc;border-left: 6px solid #ffeb3b;'>
            <p><strong>Bad answer. </strong> {} </p>
            </div>""".format(texterror)
    if lang=='fr':
        if score==-1:
            msg="""<div style='margin-bottom: 15px;padding: 4px 12px;background-color: #e7f3fe;border-left: 6px solid #2196F3;'>
            <p><strong>Attention !</strong> {} </p>
            </div>""".format(texterror)
        elif score==100:
            msg="""<div style='  margin-bottom: 15px;padding: 4px 12px;background-color: #ddffdd;border-left: 6px solid #4CAF50;'>
            <p><strong>Bonne réponse. </strong> {} </p>
            </div>""".format(texterror)
        else:
            msg="""<div style='  margin-bottom: 15px;padding: 4px 12px;background-color: #ffffcc;border-left: 6px solid #ffeb3b;'>
            <p><strong>Réponse incorrecte. </strong> {} </p>
            </div>""".format(texterror)
    return msg
