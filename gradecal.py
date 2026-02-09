no_of_subjects=int(input("enter number of subjects : "))
sub1=int(input("enter the marks of Science : "))
sub2=int(input("enter the marks of Maths : "))
sub3=int(input("enter the marks of Social : "))
sub4=int(input("enter the marks of Hindi : "))
sub5=int(input("enter the marks of Telugu : "))
total_marks=sub1+sub2+sub3+sub4+sub5

max_mark=100*no_of_subjects
marks_ratio=total_marks/max_mark
percentage=marks_ratio*100
print(total_marks)
print(percentage)
if percentage>=90 and percentage<=100:
    print("very Good --'A'")
elif percentage>=80:
    print("GOOD---'B'")
elif percentage>=60 :
    print("Average----'C'")
else:
    print("poor you can improve")