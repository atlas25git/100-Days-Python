#package differs from mmodule in terms of sheer amount of code contained
#pypi-> python package index
#installing package:->preferences->project_Interpreter

from prettytable import PrettyTable as pt 

table = pt();
table.add_column("Name",["1","2","3"])
table.add_column("LName",["11","22","33"])
table.align="l"
print(table)
