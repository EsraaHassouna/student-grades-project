# 🎓 My First Small Project in Python

This is my first simple Python project after returning to coding 🚀.  
It manages a list of students with their grades and calculates the **average Math grade**.

---

## 🛠️ Features
- Stores student names and grades in different subjects (Math, Science, English).  
- Prints each student's Math grade individually.  
- Calculates and displays the average Math grade for all students.  
- Add new student data
- Input validation with exception handling
---

## Example: Accessing Sara’s Grades and Adding Age
We can directly search for **Sara** inside the list of dictionaries using `next()`:

```python
sara = next((student for student in stuList if student['name'] == 'Sara'), None)


## 📂 Technologies Used
- Python 3.10  

---

## ▶️ How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/YourUsername/YourRepoName.git
   ```
2. Go to the project folder:
   ```bash
   cd YourRepoName
   ```
3. Run the Python script:
   ```bash
   python main.py
   ```

---

## 📸 Sample Output
```
The math grade of Omar is 90
The math grade of Sara is 85
The math grade of Ali is 78
The math grade of Lina is 92
The average of math grades is 86.25
Enter Sara's age: abc
Age must be a positive number
{'name': 'Sara', 'grades': {'Math': 85, 'Science': 95, 'English': 80}}

```

---
Project structure
   student-grades-project/
   │── student_grades.py   # Main project file
   │── README.md           # Project description
