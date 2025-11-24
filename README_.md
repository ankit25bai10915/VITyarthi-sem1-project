# 📊 Where Is My Money Going?

### A Terminal-Based Python Expense Tracker

------------------------------------------------------------------------

## 📌 Problem Identification

Many individuals struggle to track their daily expenses and understand
where their money is being spent. Without a simple and accessible
system, spending habits often go unnoticed, leading to poor financial
management and budget imbalance.

This project addresses the need for a **simple, beginner-friendly
expense tracking system** that runs entirely in the Python terminal.

------------------------------------------------------------------------

## 🎯 Objectives & Expected Outcomes

### Objectives

-   Allow users to easily record daily expenses.
-   Categorize expenses for better analysis.
-   Display all recorded expenses clearly.
-   Calculate total spending and identify the highest spending category.

### Expected Outcomes

-   Improved awareness of personal spending patterns.
-   Prevention of overspending.
-   Better financial planning and budgeting habits.

------------------------------------------------------------------------

## 🧠 Concepts Applied

This project applies fundamental Python programming concepts: -
Functions and modular programming\
- Lists and dictionaries\
- Loops and conditional statements\
- Error handling using try-except\
- User input validation\
- Basic data analysis logic

------------------------------------------------------------------------

## 🛠 Tools & Technologies Used

-   **Python 3**
-   Standard Python libraries only (No external dependencies)
-   Terminal / Command Line Interface (CLI)

------------------------------------------------------------------------

## 🧩 Structured Development Process

### 1. Problem Definition

Users lack a simple tool to track and analyze daily expenses in
real-time.

### 2. Requirement Analysis

-   Add new expenses
-   View all expenses
-   Calculate total amount spent
-   Identify most spent category
-   Exit option

### 3. Top-Down Design / Modularization

The program is divided into the following modules: - `add_expense()` -
`view_all_expenses()` - `view_total_spent()` - `main_menu()`

Each module performs a specific task, improving readability and
maintainability.

### 4. Algorithm Development

1.  Display menu options.
2.  Take user input for selection.
3.  Perform actions based on choice:
    -   Store expenses in a list of dictionaries.
    -   Calculate totals using loops.
4.  Repeat until user chooses Exit.

### 5. Implementation

The solution is implemented as a terminal-based Python application that
stores expense data in memory and processes it in real-time, allowing
users to view summaries and analyze spending trends effectively.

### 6. Testing and Refinement

-   Tested for invalid numeric input handling.
-   Verified category-wise calculations.
-   Refined user interface for clarity and usability.
-   Ensured smooth looping menu experience.

------------------------------------------------------------------------

## ▶ How To Run The Program

1.  Make sure Python is installed.
2.  Clone this repository:

``` bash
git clone https://github.com/your-username/where-is-my-money-going.git
```

3.  Navigate to the folder and run:

``` bash
python code.py
```

------------------------------------------------------------------------

## 📷 Sample Features

-   Add Expense\
-   View All Expenses\
-   View Total Amount\
-   Discover Highest Spending Category

------------------------------------------------------------------------

## 🚀 Future Enhancements

-   Save expenses to a file (CSV / JSON)
-   Monthly expense reports
-   Graphical User Interface (GUI)
-   Budget limit warnings
-   Data visualization

------------------------------------------------------------------------

## ✅ Conclusion

This project offers a practical solution to a real-world financial
problem using basic Python programming. It demonstrates structured
development, clear logic flow, and effective modular design, making it
ideal for beginners and academic submissions.
