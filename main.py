import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

# employee_data = pd.read_sql("SELECT * FROM employees;", conn)
# print(employee_data)

# employees_first_and_last = pd.read_sql("""
# SELECT firstName, lastName
#     FROM employees;
# """, conn).head()
# print(employees_first_and_last)

# # ------------------------------------------- Aliasing columns -------------------------------------------
# employees_first_and_last = pd.read_sql("""
# SELECT firstName AS name
#     FROM employees;
# """, conn).head()
# print(employees_first_and_last)


# # -------------------------------------- CASE to Bin Column Values ---------------------------------------
# employees_by_role = pd.read_sql("""
# SELECT firstName, lastName, jobTitle,
#     CASE
#     WHEN jobTitle = "Sales Rep" THEN  "Sales Rep"
#     ELSE "Not Sales Rep"
#     END AS role
# FROM employees
# """, conn).head(10)
# print(employees_by_role)

# # ---------------------------------- CASE to Make Values Human-Readable ----------------------------------
# employees_with_location = pd.read_sql("""
# SELECT firstName, lastName, officeCode,
#     CASE
#     WHEN officeCode = "1" THEN "San Francisco, CA"
#     WHEN officeCode = "2" THEN "Boston, MA"
#     WHEN officeCode = "3" THEN "New York, NY"
#     WHEN officeCode = "4" THEN "Paris, France"
#     WHEN officeCode = "5" THEN "Tokyo, Japan"
#     END AS office
# FROM employees
# """, conn).head(10)

# print(employees_with_location)

# # -------------------------- CASE to Make Values Human-Readable (Shorter form) ---------------------------
# employees_with_location = pd.read_sql("""
# SELECT firstName, lastName, officeCode,
#     CASE officeCode
#     WHEN "1" THEN "San Francisco, CA"
#     WHEN "2" THEN "Boston, MA"
#     WHEN "3" THEN "New York, NY"
#     WHEN "4" THEN "Paris, France"
#     WHEN "5" THEN "Tokyo, Japan"
#     END AS office
# FROM employees
# """, conn).head(10)

# print(employees_with_location)

# ======================================================= Built-In SQL Functions for String Manipulation ========================================================

# # -------------------------------- Length of firt names of all employees ---------------------------------
# employee_name_lengths = pd.read_sql("""
# SELECT length(firstName) AS name_length
#   FROM employees;
# """, conn).head()

# print(employee_name_lengths)

# # ----------------------------- Capitalize all letters of names of employees -----------------------------
# upper_employees = pd.read_sql("""
# SELECT upper(firstName) AS name_in_all_caps
#   FROM employees;
# """, conn).head()

# print(upper_employees)

# # ------------------------------------ Return substring of firstName -------------------------------------
# employees_initials = pd.read_sql("""
# SELECT substr(firstName, 1, 1) AS first_initial
#   FROM employees;
# """, conn).head()

# print(employees_initials)

# # ---------------------- Return substring of firstName (Add a . after each letter) -----------------------
# employees_initials = pd.read_sql("""
# SELECT substr(firstName, 1, 1) || "." AS first_initial
#   FROM employees;
# """, conn).head()

# print(employees_initials)

# # ------------------------------- Combine first and last name as fullname --------------------------------
# employees_initials = pd.read_sql("""
# SELECT firstName || lastName AS full_name
#   FROM employees;
# """, conn).head()

# print(employees_initials)

# # -------------------- Combine first and last name as fullname (add space in between) --------------------
# employees_initials = pd.read_sql("""
# SELECT firstName || " " || lastName AS full_name
#   FROM employees;
# """, conn).head()

# print(employees_initials)

# ========================================================= Built-In SQL Functions for Math Operations ==========================================================

# # Basic SELECT operation
# order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn)
# print(order_details)

# # ----------------------------------------------- Rounding -----------------------------------------------
# rounded_prices = pd.read_sql("""
# SELECT round(priceEach) AS rounded_price
#     FROM orderDetails
# """, conn) 
# print(rounded_prices)

# # ------------------------------------------ CASTing as Integer ------------------------------------------
# rounded_prices = pd.read_sql("""
# SELECT CAST(round(priceEach) AS INTEGER) AS rounded_price_int
#     FROM orderDetails
# """, conn) 
# print(rounded_prices)

# ==================================================================== Basic Math Operations ====================================================================

# totals = pd.read_sql("""
# SELECT priceEach * quantityOrdered AS total_price
#     FROM orderDetails
# """, conn)

# print(totals)

# ===================================================== Built-In SQL Functions for Date and Time Operations =====================================================

# # Basic retrieval
# orders = pd.read_sql("""
# SELECT * FROM orders
# """, conn)
# print(orders)

# # ----------------- Difference between requiredDate and orderDate (doesnt work - need to specify) ----------------
# days_remaining = pd.read_sql("""
# SELECT requiredDate - orderDate
#   FROM orders;
# """, conn)

# print(days_remaining)

# # ----------------- Difference between requiredDate and orderDate using julianday function ----------------
# days_remaining = pd.read_sql("""
# SELECT julianday(requiredDate) - julianday(orderDate) AS days_from_order_to_required
#     FROM orders
# """, conn)

# print(days_remaining)

# # ----------------- Select order dates as well as dates 1 week after the order dates -----------------
# order_dates = pd.read_sql("""
# SELECT orderDate, date(orderDate, "+7 days") AS one_week_later
#     FROM orders
# """, conn)

# print(order_dates)

# # ----------------- Using strftime -----------------
# order_dates = pd.read_sql("""
# SELECT orderDate,
#        strftime("%m", orderDate) AS month,
#        strftime("%Y", orderDate) AS year,
#        strftime("%d", orderDate) AS day
#   FROM orders;
# """, conn)

# print(order_dates)

conn.close()