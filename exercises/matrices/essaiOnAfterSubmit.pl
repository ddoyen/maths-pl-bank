extends = /template/mathbasic.pl

title = essai $% {\tt onAfterSubmit } %$

lang = fr

before==
a=2
==

text== 
Cliquez sur "Valider".
== 

form==
<script>
function onAfterSubmitPL() {
    console.log("coucou"); 
}
</script>
==

evaluator ==
score = 100
==





