# Demo 

from timemanage import *

my_course=COURSE("CSE","F1101","Sandeep Reddy Wanga",["12-12-2023"])
sec=SECTIONS("Lecture",["Tuesday"],["12-01"])
my_course.add(sec)
print(my_course)
get_section=my_course.get_all_section()
for i in get_section:
    print(i)

my_timetable=TIMETABLE()
my_timetable.enroll_subject(my_course)
my_timetable.clashes()
my_timetable.export_to_csv()







