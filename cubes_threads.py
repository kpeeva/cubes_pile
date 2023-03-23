"""
Pseudocode for pile of cubes using threads and queues:

Import the required modules 'Queue' and 'Thread'
Function 'read_input' that takes a queue as an argument.
1 Read the number of test cases.
2 Put the number of test cases in the queue.
3 For each test case,
- Read the number of cubes.
- Append the number of cubes to the 'side_lengths' list.
For each cube,
- Read the side length.
- Append the side length to the 'side_lengths' list.
Put the 'side_lengths' list in the queue.
Function 'process_input' that takes a queue as an argument.
1 While the queue is not empty,
a Get the next data from the queue.
b If the data is "STOP", break from the loop.
c Extract the number of test cases and the side lengths from the data.
d For each test case,
- Calculate the pile volume.
- Find the maximum cube side length.
- Create a list 'result' with the maximum cube side length as the first element.
- For each remaining cube,
* If the last cube in the 'side_lengths' list is less than or equal to the first cube and less than or equal to the last element in the 'result' list,
- Pop the first cube from the 'side_lengths' list and assign it to 'max_cube'.
* If the first cube in the 'side_lengths' list is less than the last cube and less than or equal to the last element in the 'result' list,
- Pop the last cube from the 'side_lengths' list and assign it to 'max_cube'.
* Otherwise, print "No" and the pile volume, and break from the loop.
* Append the 'max_cube' to the 'result' list.
- If the loop completes without breaking, print "Yes" and the pile volume.
Define the function 'pile_of_cubes' that initializes the queue and creates two threads:
1 A 'reader' thread that runs the 'read_input' function.
2 A 'processor' thread that runs the 'process_input' function.
Start both threads and wait for the 'reader' thread to complete.
Put a "STOP" signal in the queue to terminate the 'processor' thread and wait for it to complete."""