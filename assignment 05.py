#Task 01: Create a Dictionary of Student Marks
#Create a dictionary with student names as keys and their marks as values
# students_marks = {
#     'Alice': 85,
#     'Bob': 92,
#     'Charlie': 78,
#     'Diana': 88
# }

# # Ask the user to input a student's name
# student_name = input("Enter the student's name: ")

# #Retrieve and display the corresponding marks
# if student_name in students_marks:
#     print(f"{student_name}'s marks: {students_marks[student_name]}")
# else:
#     #Display an appropriate message if the student's name is not found
#     print(f"Sorry, no marks found for {student_name}.")


#Task 02:Demonstrate List Slicing
# lets create a list of numbers from 1 to 10
numbers=list(range(1,11))
print("original list",numbers)
#Extract the first five elements from the list
Extract_num=numbers[:5]
#Reverses these extracted elements
reversed_num=Extract_num[::-1]
print(f"Extracted first five element :{Extract_num}")
print(f"reverse of extracted elements:{reversed_num}")