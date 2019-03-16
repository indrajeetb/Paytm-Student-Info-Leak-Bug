# Paytm Student Info Leak Bug

Paytm has a feature called **'Fees'** using which user can pay fees of their school or college. While making payment user needs to enter his / her roll number , which is then matched with the student data provided by that respective school / college and information is displayed. 

## The Bug
There is no limit on how many times we can check the details so once the roll number format of an institute is known , one can get the details of all students studying in that institute . Student details depends on what that school / college have shared with Paytm. 

## Demo
In the demo I tried to get the student details of **'Assam Don Bosco University'**. I got the following details of all the students studying in Assam Don Bosco University :
1. Student Name
2. Course Enrolled
3. Father's name

These details vary based on what a specific school / college has shared with Paytm.

To get the student details first we must know the roll number format and in case of Assam Don Bosco University the roll no. format is **'DC[XXXX][YYY][ZZZZ]'** . Here
1. XXXX - Year when the student joined the university.
2. YYY - Course enrolled
3. ZZZZ - Roll number.

Once the format is known, we can use the script paytm.py to get all the student details.

### Video POC 1

[![Video POC 1](http://img.youtube.com/vi/0zU5sf2f9DI/0.jpg)](http://www.youtube.com/watch?v=0zU5sf2f9DI "Paytm Student Info Leak Flaw
")

### Video POC 2

[![Video POC 2 ](http://img.youtube.com/vi/wHMbkp3NI3I/0.jpg)](http://www.youtube.com/watch?v=wHMbkp3NI3I "Paytm Student Info Leak Flaw 2
")

## Timeline

* Feb 9, 2019 - Initial Report
* Feb 11 , 2019 - Got reply from Paytm asking to show POC in browser
* Feb 15, 2019 - Report closed, Bug not accepted as Low Impact

**PS : The bug is not yet fixed as of 3rd March 2019 and anyone can get entire student list of any college / schools that are registered with paytm if the roll number format is known**


