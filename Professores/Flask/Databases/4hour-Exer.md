# ExAMPles aND mORe  

## 1. Introduction to SQL Exercises:

### Easy Exercise:
**Task:** Create a table to store employee information with columns for `employee_id`, `employee_name`, and `salary`.

**Solution:**
```sql
CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100),
    salary DECIMAL(10, 2)
);
```

### Complex Exercise:
**Task:** Modify the table to include a new column for `department_id` and create a foreign key relationship with a `Departments` table.

**Solution:**
```sql
ALTER TABLE Employees
ADD COLUMN department_id INT,
ADD CONSTRAINT fk_department_id
    FOREIGN KEY (department_id)
    REFERENCES Departments(department_id);
```

---

## 2. Retrieving Data with SELECT Exercises:

### Easy Exercise:
**Task:** Retrieve all columns for all employees.

**Solution:**
```sql
SELECT * FROM Employees;
```

### Complex Exercise:
**Task:** Retrieve the names of employees who have a salary greater than the average salary.

**Solution:**
```sql
SELECT employee_name
FROM Employees
WHERE salary > (SELECT AVG(salary) FROM Employees);
```

---

## 3. Modifying Data Exercises:

### Easy Exercise:
**Task:** Insert a new employee into the table.

**Solution:**
```sql
INSERT INTO Employees (employee_id, employee_name, salary)
VALUES (1, 'John Doe', 50000.00);
```

### Complex Exercise:
**Task:** Update the salary of all employees in the 'Sales' department to be 10% higher.

**Solution:**
```sql
UPDATE Employees
SET salary = salary * 1.10
WHERE department_id = (SELECT department_id FROM Departments WHERE department_name = 'Sales');
```

---

## 4. Joins and Relationships Exercises:

### Easy Exercise:
**Task:** Retrieve employee names along with their corresponding department names.

**Solution:**
```sql
SELECT Employees.employee_name, Departments.department_name
FROM Employees
JOIN Departments
ON Employees.department_id = Departments.department_id;
```

### Complex Exercise:
**Task:** Retrieve the department(s) with the highest average employee salary.

**Solution:**
```sql
WITH AvgSalaries AS (
    SELECT department_id, AVG(salary) as avg_salary
    FROM Employees
    GROUP BY department_id
)
SELECT Departments.department_name
FROM AvgSalaries
JOIN Departments
ON AvgSalaries.department_id = Departments.department_id
WHERE avg_salary = (SELECT MAX(avg_salary) FROM AvgSalaries);
```
---

## Interaction with SQLAlchemy
To interact with the database manually using SQLAlchemy, you can use various methods and tools to execute SQL queries, inspect the database, and modify data. Here's how you can manually interact with the database:

### 1. **Using the Python Shell:**

You can use the Python shell to interact with the database interactively.

```bash
python

# Inside the Python shell
from your_app import db, User

# Create a new user
new_user = User(username='john_doe')
db.session.add(new_user)
db.session.commit()

# Query the database
user = User.query.filter_by(username='john_doe').first()
print(user)
```

### 2. **SQLAlchemy Console (Flask-SQLAlchemy):**

Flask-SQLAlchemy provides a useful command-line interface for interacting with the database. Run the following command to open the interactive console:

```bash
flask shell
```

You can then execute SQLAlchemy commands as shown in the Python shell example above.

### 3. **Database Management Tools:**

You can use database management tools like **DB Browser for SQLite** (for SQLite) or **pgAdmin** (for PostgreSQL) to interact with the database. These tools provide a graphical interface to view and manipulate the data.

### 4. **SQL Queries:**

You can directly execute SQL queries using SQLAlchemy's `execute` function.

```python
from sqlalchemy import text

# Execute a raw SQL query
result = db.engine.execute(text("SELECT * FROM users"))
for row in result:
    print(row)
```

### 5. **SQLAlchemy ORM:**

Use SQLAlchemy's ORM features to interact with the database in a more structured manner. You can create, read, update, and delete records using ORM.

```python
# Creating a new user
new_user = User(username='alice')
db.session.add(new_user)
db.session.commit()

# Querying the database
user = User.query.filter_by(username='alice').first()
print(user)

# Updating a record
user.username = 'new_username'
db.session.commit()

# Deleting a record
db.session.delete(user)
db.session.commit()
```
---

## SQL Topics to Learn:

### 1. **Indexes:**
   - **Explanation:** Indexes are data structures that speed up data retrieval in SQL by allowing the database server to find rows more quickly.
   - **Notes:**
     - Use indexes on columns commonly used in WHERE, JOIN, and ORDER BY clauses.
     - Common types: B-tree, Hash, Bitmap.
   - **Example:**
     ```sql
     CREATE INDEX idx_username ON Users(username);
     ```

### 2. **Transactions:**
   - **Explanation:** Transactions ensure that a series of SQL queries are executed as a single, atomic unit of work. They maintain data consistency and integrity.
   - **Notes:**
     - ACID properties: Atomicity, Consistency, Isolation, Durability.
     - Begin a transaction with START TRANSACTION.
   - **Example:**
     ```sql
     START TRANSACTION;
     -- SQL queries
     COMMIT;
     ```

### 3. **Views:**
   - **Explanation:** Views are virtual tables derived from the result of a SELECT query. They simplify complex queries and provide a layer of abstraction.
   - **Notes:**
     - Views don't store data themselves; they store the SQL query.
   - **Example:**
     ```sql
     CREATE VIEW high_earners AS
     SELECT name, salary FROM Employees WHERE salary > 50000;
     ```

### 4. **Stored Procedures:**
   - **Explanation:** Stored procedures are prepared SQL code that you can save, reuse, and share, improving code modularity and security.
   - **Notes:**
     - Parameters can be passed to stored procedures.
     - Reduce network traffic.
   - **Example:**
     ```sql
     DELIMITER //
     CREATE PROCEDURE GetEmployee(IN employee_id INT)
     BEGIN
         SELECT * FROM Employees WHERE id = employee_id;
     END //
     DELIMITER ;
     ```

### 5. **Triggers:**
   - **Explanation:** Triggers are special kinds of stored procedures that are activated ("triggered") in response to certain events on a particular table.
   - **Notes:**
     - Common events: INSERT, UPDATE, DELETE.
     - Use with caution to avoid performance issues.
   - **Example:**
     ```sql
     CREATE TRIGGER after_insert AFTER INSERT ON Employees
     FOR EACH ROW
     BEGIN
         INSERT INTO AuditLog (event_type, event_description)
         VALUES ('INSERT', 'New employee added');
     END;
     ```

### 6. **Database Design and Normalization:**
   - **Explanation:** Database design involves organizing data into tables, choosing appropriate data types, and applying normalization techniques to reduce redundancy and maintain data integrity.
   - **Notes:**
     - Normal forms: 1NF, 2NF, 3NF, BCNF, 4NF, 5NF.
     - Avoid data duplication.
   - **Example:**
     ```sql
     CREATE TABLE Users (
         user_id INT PRIMARY KEY,
         username VARCHAR(50) UNIQUE,
         email VARCHAR(100)
     );
     ```

### 7. **Performance Optimization:**
   - **Explanation:** Performance optimization involves tuning SQL queries, indexing, and database configuration to improve query execution speed and resource usage.
   - **Notes:**
     - Analyze query execution plans to identify bottlenecks.
     - Use EXPLAIN to analyze query performance.
   - **Example:**
     ```sql
     EXPLAIN SELECT * FROM Users WHERE age > 30;
     ```

### 8. **Recursive Queries:**
   - **Explanation:** Recursive queries involve querying a table in a self-referencing manner, often used in hierarchical data structures.
   - **Notes:**
     - Commonly used with Common Table Expressions (CTE).
     - Requires support from the DBMS (e.g., PostgreSQL).
   - **Example:**
     ```sql
     WITH RECURSIVE EmployeePaths AS (
         SELECT id, name, manager_id
         FROM Employees
         WHERE id = 1
         UNION ALL
         SELECT e.id, e.name, e.manager_id
         FROM Employees e
         INNER JOIN EmployeePaths ep ON e.manager_id = ep.id
     )
     SELECT * FROM EmployeePaths;
     ```

### 9. **JSON and XML Data Handling:**
   - **Explanation:** SQL supports storing, querying, and manipulating JSON and XML data formats, providing flexibility in handling structured and unstructured data.
   - **Notes:**
     - JSON functions: JSON_QUERY, JSON_ARRAYAGG, JSON_OBJECT, etc.
     - XML functions: XMLQUERY, XMLEXISTS, XMLTABLE, etc.
   - **Example (JSON):**
     ```sql
     SELECT name
     FROM Employees
     WHERE JSON_VALUE(details, '$.department') = 'Sales';
     ```

---
