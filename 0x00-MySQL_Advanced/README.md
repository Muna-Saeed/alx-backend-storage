# 0x00 MySQL Advanced

This project consists of SQL scripts and tasks focused on advanced MySQL concepts and operations. The tasks cover a range of topics including table creation, indexing, stored procedures, triggers, views, and more.

## General Information

- All scripts are designed to be executed on Ubuntu 18.04 LTS using MySQL 5.7.
- Each task is accompanied by its specific requirements and expected outcomes.
- The project directory structure follows the convention of naming each task's script with a corresponding number.

## Installation and Execution

To run the scripts, follow these steps:

1. Ensure you have MySQL 5.7 installed on Ubuntu 18.04 LTS.
2. Clone this repository to your local machine.
3. Navigate to the `0x00-MySQL_Advanced` directory.
4. Execute the desired script using the MySQL client, providing appropriate credentials and database names when necessary.

Example:
```bash
$ cat 0-uniq_users.sql | mysql -uroot -p holberton
```

## Task Descriptions

Each task in the project has specific requirements and objectives. Below is a brief overview of each task:

1. **We are all unique!**: Create a table with unique constraints.
2. **In and not out**: Create a table with an enumeration and default values.
3. **Best band ever!**: Rank bands by country origin based on the number of fans.
4. **Old school band**: List bands with a specific style and rank them by longevity.
5. **Buy buy buy**: Create a trigger to decrease item quantity after adding an order.
6. **Email validation to sent**: Create a trigger to reset a flag when an email is changed.
7. **Add bonus**: Create a stored procedure to add a new correction score for a student.
8. **Average score**: Create a stored procedure to compute and store the average score for a student.
9. **Optimize simple search**: Create an index on the first letter of a name.
10. **Optimize search and score**: Create an index on the first letter of a name and the score.
11. **No table for a meeting**: Create a view listing students needing a meeting based on specific criteria.

## Concepts

For this project, we expect you to look at these concepts:
- Advanced SQL
- MySQL cheatsheet
- MySQL Performance: How To Leverage MySQL Database Indexing
- Stored Procedure
- Triggers
- Views
- Functions and Operators
- Trigger Syntax and Examples
- CREATE TABLE Statement
- CREATE PROCEDURE and CREATE FUNCTION Statements
- CREATE INDEX Statement
- CREATE VIEW Statement

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- How to create tables with constraints
- How to optimize queries by adding indexes
- What is and how to implement stored procedures and functions in MySQL
- What is and how to implement views in MySQL
- What is and how to implement triggers in MySQL

## Resources

Read or watch:
- [MySQL cheatsheet](https://devhints.io/mysql)
- [MySQL Performance: How To Leverage MySQL Database Indexing](https://www.digitalocean.com/community/tutorials/how-to-leverage-mysql-indexing-to-optimize-query-performance)
- [Stored Procedure](https://dev.mysql.com/doc/refman/5.7/en/stored-routines.html)
- [Triggers](https://dev.mysql.com/doc/refman/5.7/en/triggers.html)
- [Views](https://dev.mysql.com/doc/refman/5.7/en/views.html)
- [Functions and Operators](https://dev.mysql.com/doc/refman/5.7/en/functions.html)
- [Trigger Syntax and Examples](https://dev.mysql.com/doc/refman/5.7/en/trigger-syntax.html)
- [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/5.7/en/create-table.html)
- [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html)
- [CREATE INDEX Statement](https://dev.mysql.com/doc/refman/5.7/en/create-index.html)
- [CREATE VIEW Statement](https://dev.mysql.com/doc/refman/5.7/en/create-view.html)

## Credits

This project is a part of the curriculum provided by [Holberton School](https://www.holbertonschool.com/).

## Author

Muna Saeed
