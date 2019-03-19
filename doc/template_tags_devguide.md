* This document gives some guideline on how to create new template tags to facilitate the inclusion of complex `html` code in the `text` and `form` tags of a `pl` exercise. 

# The basic ingredients.

Assume we are creating a template tag `my_tag`, whose purpose is to insert specially formatted input field in the `form` part of an exercise. 

Such an input field could be, for instance a drop-down list of items to select from
~~~~
<span style = 'display:inline-block;' id = 'name'>
  <select>
		 <option value='item_1'> item_1 </option>
		 <option value='item_2'> item_2 </option>
		 <option value='item_3'> item_3 </option>
  </select>
</span>
~~~~~

The 



