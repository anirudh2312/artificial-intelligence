Please find the youtube link where I have explained both the algorithms that I have implememnted for this project and compared their results. Here is the link: https://www.youtube.com/watch?v=Gd_MwHBGC30

Given the heatmap (possible areas of finding the missing person), the project aims to analyze and implement search algorithm which maximizes the cumulative probability distribution of the heatmap in lesser amount of time. Implemented the complete coverage algorithm and then one of its variant algorithm which increased the efficiency of the search path 10 times for the given heatmap.

cc.py is the implementation of the Complete Coverage algorithm.

cc_var.py is the implementation of the variation alogirthm of complete coverage.

Heatmap1 and heatmap2 have the coordinates of the wild park and the corresponding probability of finding the person at those coordinates.

output_cc_heatmap1 is the output of cc.py on heatmap1
output_cc_heatmap2 is the output of cc.py on heatmap2
output_cc_var_heatmap1 is the output of cc_var.py on heatmap1
output_cc_var_heatmap2 is the output of cc_var.py on heatmap2

Graphical_and_tabular_summary.pdf file analyze the differences between both the algorithms, both graphically and in tabular form.  

The output files show the coordinates in an order in which UAV should visit first so as to minimize the amount of time to search. 

