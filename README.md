Task 01: Create a Dictionary of Student Marks
we create a dictionary with students name as keys and their marks as values
then we take student name as a input from the user named 'student_name'
then we write a program to find that name is present in the dictionary or not 
if present then it will give its corrosponding value and if not present it show marks for this name does not exits.
if student_name in students_marks:
    print(f"{student_name}'s marks: {students_marks[student_name]}")
else:
    print(f"Sorry, no marks found for {student_name}.")


Task 02:Demonstrate List Slicing
lets create a list of numbers from 1 to 10 using range 
numbers=list(range(1,11))
print("original list",numbers)
Extract the first five elements from the list using indexing named 'Etract_num'
Reverses these extracted elements also using indexing named 'reversed_num'
then print the both extracted and reversed extracted lists as
rint(f"Extracted first five element :{Extract_num}")
print(f"reverse of extracted elements:{reversed_num}")
get result as
original list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted first five element :[1, 2, 3, 4, 5]
reverse of extracted elements:[5, 4, 3, 2, 1]
