# Define the sets

set1 = {'Ritik SIngh', 'Manish Prajapati', 'Manishka Pareta', 'K Harikumar Reddy', 'Harsh Patel', 'Parimal Patel', 'Pratik Hadvani', 'Bhargav Prajapati', 'Saurabh Mamidwar', 'Dinesh Pathak', 'Manish Nandal', 'Pankaj Jangid', 'Sandeep Baikan', 'Premalatha Nagula', 'Vikas Singh', 'Namah Jain', 'Khushali Samarth Baxi', 'Mayur Birle', 'Harshil Khant', 'Santhosh Malka', 'Archit Jain', 'Shahab Dad Khan', 'Utkarsh Mankad', 'Shailendrapal Singh Shekhawat', 'Namrata Chheda', 'Aravind Nallajerla', 'Narra Maneesha', 'Jaikumar Chandrapalka', 'Meet Dhanani', 'Mohammed Shoab Ansari', 'Anuja Yadav', 'Karan Raina', 'Monika Mishra', 'Noel Mathew', 'Omkar Mestry', 'Rajarshi Mondal', 'Thrishma Kaleru', 'Deepanshi Jain', 'Harshala Ramesh Khinde', 'Ankit Sanjivan Kadam', 'Raj Savsani', 'Mit Parekh', 'Chirag Changrani', 'Hansraj Rajesh Deghun', 'Shubhendra Singh'}

# updated
set2 = {'Utkarsh Mankad', 'Manishka Pareta', 'Pratik Hadvani', 'Namrata Chheda', 'Premalatha Nagula', 'Manish Prajapati', 'Santhosh Malka', 'Dinesh Pathak', 'K Harikumar Reddy', 'Ritik SIngh', 'Deepa Bhandary', 'Bhargav Prajapati', 'Noel Mathew', 'Ankit Sanjivan Kadam', 'Harsh Patel', 'Shailendrapal Singh Shekhawat', 'Shubhendra Singh', 'Aravind Nallajerla', 'Harshil Khant', 'Pramod Mishra', 'Jaikumar Chandrapalka', 'Vikas Singh', 'Deepanshi Jain', 'Raj Savsani', 'Krishnam Mishra', 'Archit Jain', 'Thrishma Kaleru', 'Shahab Dad Khan', 'Manish Nandal', 'Pankaj Jangid', 'Rajarshi Mondal', 'Mit Parekh', 'Monika Mishra', 'Omkar Mestry', 'Hansraj Rajesh Deghun', 'Harshala Ramesh Khinde', 'Khushali Samarth Baxi', 'Shraddha Gami', 'Anuja Yadav', 'Mohammed Shoab Ansari', 'Mayur Birle', 'Karan Raina', 'Saurabh Mamidwar', 'Chirag Changrani', 'Parimal Patel', 'Narra Maneesha', 'Meet Dhanani', 'Sandeep Baikan', 'Namah Jain'}

# Calculate differences
only_in_set1 = set1 - set2
only_in_set2 = set2 - set1

# Print the results
print("Names in Set1 but not in Set2:")
print(only_in_set1)

print("\nNames in Set2 but not in Set1:")
print(only_in_set2)
