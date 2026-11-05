"""
================================================================================
                    PROJECT ASSIGNMENT DETAILS
================================================================================
  📌 Name          : Umesh Kumar
  📌 ERP           : RU-26-00504
  📌 University    : Rungta International Skills University
  📌 Section       : B
  📌 Submitted To  : Satyaprakash Sir
================================================================================
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------
# ⚙️ CONFIGURATION & CONSTANTS
# ------------------------------------------------------------------------------
CSV_FILE = Path(__file__).with_name("employees.csv")


def load_and_clean_data():
    """
    📥 LOAD & CLEAN DATASET
    -----------------------
    Reads the dataset from CSV, performs structural validation, handles string 
    formatting, converts types, removes duplicates, and imputes missing values.
    """
    # 🔍 Step 1: Check CSV file existence
    if not CSV_FILE.exists():
        print("Error: employees.csv file not found!")
        return None, None

    # 📖 Step 2: Attempt loading dataset
    try:
        df = pd.read_csv(CSV_FILE)
    except Exception as error:
        print("Error reading CSV:", error)
        return None, None

    # ✅ Step 3: Validate column requirements
    required_columns = [
        "Emp_ID", "Name", "Department", "Salary", "Experience"
    ]

    if not all(col in df.columns for col in required_columns):
        print("Error: Required columns are missing!")
        return None, None

    # 🧹 Step 4: Sanitize text columns (strip whitespace)
    for col in ["Emp_ID", "Name", "Department"]:
        df[col] = df[col].astype("string").str.strip()

    # 🔢 Step 5: Convert numerical columns safely
    df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")
    df["Experience"] = pd.to_numeric(
        df["Experience"], errors="coerce"
    )

    original_count = len(df)

    # ✂️ Step 6: Deduplicate records based on Employee ID
    df = df.drop_duplicates(
        subset=["Emp_ID"], keep="first"
    ).copy()

    duplicates_removed = original_count - len(df)

    # 💰 Step 7: Handle missing salary values using mean imputation
    valid_salaries = df["Salary"].dropna()

    if valid_salaries.empty:
        print("Error: No valid salaries found!")
        return None, None

    salary_mean = valid_salaries.mean()
    missing_count = int(df["Salary"].isna().sum())

    df["Salary"] = df["Salary"].fillna(salary_mean)

    # 🗑️ Step 8: Remove invalid core records
    df = df.dropna(
        subset=["Emp_ID", "Name", "Department"]
    ).copy()

    cleaning_needed = (
        duplicates_removed > 0 or missing_count > 0
    )

    # 📊 Step 9: Package cleaning report statistics
    cleaning_info = {
        "needed": cleaning_needed,
        "duplicates": duplicates_removed,
        "missing": missing_count,
        "mean": salary_mean,
        "rows": len(df)
    }

    return df, cleaning_info


def show_summary(df):
    """
    📊 DISPLAY STATISTICAL SUMMARY
    ------------------------------
    Computes and prints total workforce metrics, average salary, highest paid 
    employee details, and overall company payroll.
    """
    total_employees = len(df)
    average_salary = df["Salary"].mean()

    highest_employee = df.loc[df["Salary"].idxmax()]
    total_payroll = df["Salary"].sum()

    print(
        f"Employees: {total_employees} | "
        f"Average salary: {average_salary:.2f}"
    )

    print(
        f"Highest paid: {highest_employee['Name']} "
        f"({highest_employee['Salary']:.0f})"
    )

    if total_employees > 1:
        print(f"Total payroll: {total_payroll:.0f}")


def show_cleaning_report(cleaning_info):
    """
    📝 DATA CLEANING AUDIT REPORT
    -----------------------------
    Displays metrics on duplicate removals, missing value imputations, 
    and total clean records available for processing.
    """
    print(
        f"Duplicates removed: {cleaning_info['duplicates']}"
    )

    if cleaning_info["missing"] > 0:
        print(
            "Missing Salary filled with mean: "
            f"{cleaning_info['mean']:.2f}"
        )

    print(f"Cleaned rows: {cleaning_info['rows']}")


def department_report(df):
    """
    🏢 DEPARTMENT AGGREGATION & DATA VISUALIZATION
    ------------------------------------------------
    - Groups records by department and computes average salaries.
    - Filters employees above a user-specified threshold.
    - Generates and displays a styled Matplotlib bar chart.
    """
    # 📌 Grouping and aggregated analytics
    report = df.groupby(
        "Department", sort=False
    ).agg(
        Employees=("Emp_ID", "count"),
        Average_Salary=("Salary", "mean")
    )

    for department, row in report.iterrows():

        count = int(row["Employees"])
        employee_word = (
            "employee" if count == 1 else "employees"
        )

        print(
            f"{department}: {count} {employee_word} "
            f"| Avg salary: {row['Average_Salary']:.2f}"
        )

    # 🔎 Salary Filter Section
    try:
        limit = float(input("Enter salary limit: "))
    except ValueError:
        print("Invalid salary input!")
        return

    result = df[df["Salary"] > limit].sort_values(
        "Salary", ascending=True
    )

    if result.empty:
        print(f"Above {limit:g}: No employees found")
    else:
        names = [
            f"{row['Name']} ({row['Salary']:.0f})"
            for _, row in result.iterrows()
        ]

        print(
            f"Above {limit:g}: " + " | ".join(names)
        )

    # 🎨 Visual Chart Generation (Matplotlib)
    ax = report["Average_Salary"].plot(
        kind="bar",
        figsize=(8, 5),
        title="Department-wise Average Salary"
    )

    ax.set_xlabel("Department")
    ax.set_ylabel("Average Salary")

    ax.bar_label(
        ax.containers[0],
        fmt="%.2f",
        padding=3
    )

    plt.tight_layout()
    plt.show()

    print(
        "Bar chart 'Department-wise Average Salary' displayed"
    )


def main():
    """
    🚀 MAIN EXECUTION CONTROL LOOP
    ------------------------------
    Orchestrates application workflow, presents the interactive menu, 
    and handles user navigation choices.
    """
    # 🎬 Load and clean dataset initially
    df, cleaning_info = load_and_clean_data()

    if df is None:
        return

    # 🔄 Interactive User Interface Loop
    while True:

        print("\n====================================")
        print("           📊 MAIN MENU             ")
        print("====================================")
        print(" 1️⃣  Employee Summary")
        print(" 2️⃣  Department Report & Salary Filter")
        print(" 3️⃣  Exit")
        print("------------------------------------")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            if cleaning_info["needed"]:
                show_cleaning_report(cleaning_info)
            else:
                show_summary(df)

        elif choice == "2":
            department_report(df)

        elif choice == "3":
            print("\n👋 Exiting program. Have a great day!")
            break

        else:
            print("Invalid choice! Please select 1, 2 or 3.")


# ------------------------------------------------------------------------------
# 🏁 SCRIPT ENTRY POINT
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
