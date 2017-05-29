# Leave application system
## Setting up environment for this project
1. This project was built using python 2.7.13.
2. The packages in the requirements.txt file should be installed.
```
pip install -r requirements.txt
```
3. As this is a mini application, SQLite Database was used.

4. open a terminal and clone the repository as follows:
```
git clone https://github.com/popsonebz/tangent_leave_app_solution.git
```
This creates a folder called tangent_leave_app_solution in the current directory.

5. switch to that directory

```
cd tangent_leave_app_solution
```
6. To create the database and tables, run the migration command
```
python manage.py migrate
```

7. We can now startup the server
```
python manage.py runserver localhost:8010
```
## Admin Operation

First of all, we need to add employees to the system

<http://localhost:8010/admin/add-employee/>

Note:

1. By default, all employees have 18 days of leave.
2. This page was just added based on initiative as it was not specified in the task.

## Employee Operation

1. To apply for leave, the employee visits this url

<http://localhost:8010/leave/apply>

2. He/She is redirected to the login page for authentication

3. If Authentication is successful, the application page is displayed.

4. On selecting the start and end dates, the following are checked:

- Both either start or end date or end date cannot be less than the current date.
- The end date cannot be less than the start date.
- Start date cannot later than end date.
- End date cannot be the same as start date.
- Notify the user when there is no working days within the specified period.
- Preventing duration which exceeds the maximum 18 days of leave allocated.

### Automatically Decline the following leave application:

- Employees who have not spent up to 3 months in the company from appying for leave.
- Employee who has exhausted his leave.
- Employee taking more than the remaining leave days he has.



