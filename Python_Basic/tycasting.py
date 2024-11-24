#Type casting = str(), int(), float(), bool();
# type() function use to check the type of variable

first_name= "Parth"
last_name="Shrivastava"
age=21
is_Student= True
gpa= 9.00

print(type(first_name),type(last_name))
print(type(age))
print(type(is_Student))
print(type(gpa))

#typecast----
print(f"My GPA is: {gpa}")
gpa= int(gpa)
print(f"My GPA is: {gpa}")

name= first_name+" "+last_name;
print(f"My name is {name}")

#name= first_name+gpa TypeError: can only concatenate str (not "int") to str

a="Parth";
a=bool(a);
print(a);
a="";
a=bool(a);
print(a);