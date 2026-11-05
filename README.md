# Employee Management System (EMS)

An interactive Python application designed to process, clean, analyze, and visualize employee data from a CSV file.

---

## 📌 Project Details

- **Project ID:** PS-21
- **Student Name:** Umesh Kumar
- **ERP:** RU-26-00504
- **University:** Rungta International Skills University
- **Section:** B
- **Submitted To:** [@SATYAPRAKASHSETHY](https://github.com/SATYAPRAKASHSETHY)

---

## 🚀 Key Features

1. **Automated Data Cleaning & Imputation:**
   - Detects missing CSV file or column schema mismatches.
   - Cleans string whitespace across core text columns (`Emp_ID`, `Name`, `Department`).
   - Safely casts numeric fields (`Salary`, `Experience`).
   - Removes duplicate records based on unique `Emp_ID`.
   - Fills missing `Salary` values with the calculated column mean.

2. **Workforce Summary Analytics:**
   - Displays total employee count and overall average salary.
   - Identifies the highest-paid employee.
   - Calculates and displays total company payroll.

3. **Department-Wise Insights & Filtering:**
   - Groups data by department to show headcounts and average salaries.
   - Interactive prompt to filter and display employees earning above a custom salary threshold.

4. **Data Visualization:**
   - Renders a interactive Matplotlib bar chart illustrating **Department-wise Average Salary** with precise value labels on each bar.

---

## 📁 File Structure

```text
.
├── one.py          # Main Python application script
├── employees.csv   # Target dataset (Required)
└── README.md       # Project documentation
```

---

## 📋 CSV Format Requirements

The input file `employees.csv` must be placed in the same directory as `one.py` and contain at least the following header structure:

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `Emp_ID` | String | Unique Identifier for each employee |
| `Name` | String | Full Name of the employee |
| `Department` | String | Assigned Department |
| `Salary` | Numeric | Monthly/Annual Salary amount |
| `Experience` | Numeric | Years of Experience |

---

## 💻 How to Run

1. **Prerequisites:** Make sure Python 3.8+ is installed along with the required libraries:
   ```bash
   pip install pandas matplotlib
   ```

2. **Execute the Script:**
   ```bash
   python one.py
   ```

3. **Menu Options:**
   - Choose `1` to view **Employee Summary** / Data Cleaning Audit Report.
   - Choose `2` to view **Department Breakdown**, filter by salary, and display the Matplotlib chart.
   - Choose `3` to exit the application.