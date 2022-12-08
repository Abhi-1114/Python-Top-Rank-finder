stg=int(input("Provide strength of the class: "))
name=[]
first_term=[]
second_term=[]
for i in range(stg):
    name.append(input("Name of student: ").split(","))
    for j in range(stg):
        first_term.append((input("Provide first term mark: ")))
        break
    for j in range(stg):
        second_term.append(input("Provide second term mark: "))
        break

max_s=max(second_term)
numb=second_term.index(max_s)
top=name[numb]
rank1=first_term[numb]
sort_f=sorted(first_term , reverse=True)
rank_f=sort_f.index(rank1)
print(top,"is the topper ","Jump= ",(rank_f+1)-1)
