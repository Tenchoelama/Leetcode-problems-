

-- 181. Employees Earning More Than Their Managers

Ans:
-- SELECT e.name AS Employee
-- FROM Employee e
-- JOIN Emoployee m ON e.managerID = m.id
-- WHERE e.salary > m.salary 

-- 182. Duplicate Emails

Ans:
-- SELECT email Email
-- FROM Person
-- GROUP BY email
-- HAVING COUNT(*) > 1;

-- 196. Delete Duplicate Emails

Ans:
-- delete p1 from person p1,person p2 
-- where p1.email=p2.email and p1.id>p2.id;

-- 197. Rising Temperature

-- ANS:
-- SELECT w2.id 
-- FROM Weather w1, Weather w2
-- WHERE w2.recordDate = w1.recordDate + INTERVAL 1 DAY
-- AND w2.temperature > w1.temperature 

-- 577. Employee Bonus

ANS:
-- SELECT Employee.name, Bonus.bonus
-- FROM Employee LEFT JOIN Bonus
-- ON Employee.empId = Bonus.empID
-- WHERE bonus < 1000 OR bonus is NULL;

-- 1741. Find Total Time Spent by Each Employee

ANS:
-- SELECT a.event_day AS day, a.emp_id, SUM(out_time - in_time) AS total_time
-- FROM Employees AS a
-- GROUP BY emp_id, event_day

-- 511. Game Play Analysis I

ANS
-- SELECT player_id, MIN(event_date) as first_login
-- FROM Activity
-- GROUP BY player_id

-- 584. Find Customer Referee

ANS
-- SELECT name
-- FROM Customer 
-- WHERE referee_id != 2 or referee_id is NULL