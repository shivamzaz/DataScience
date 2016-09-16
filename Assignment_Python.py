STR=raw_input()
To_list=map(int,STR.split(" "))
Empt_dict={}
for iterator in range(3,len(To_list),1):
	Empt_dict[To_list[iterator]]=To_list[0]*pow(To_list[iterator],2)+To_list[1]*To_list[iterator]+To_list[2]
update_dict=sorted(Empt_dict.items(), key=lambda x:x[1])
Emp_Str=""
for iterator in range(len(update_dict)):
	update_dict[iterator]=map(str,list(update_dict[iterator]))
	Emp_Str+=",".join(update_dict[iterator])+" "
print Emp_Str
