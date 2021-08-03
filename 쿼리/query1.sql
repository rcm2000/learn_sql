
SELECT * FROM emp;
-- 1
SELECT * FROM emp WHERE empname like '김%' AND hdate >= '2000-01-01'
-- 2
SELECT * FROM emp WHERE ROUND(salary/12,0) > 150 and (empname like '홍%' or empname like '이%') ORDER BY salary ;
-- 3
SELECT empno,empname,deptno,salary,ROUND(salary * 0.089,0) AS tax, ROUND(salary*(1-0.089)) AS atsalary FROM emp ORDER BY DATE_FORMAT(hdate,'%Y') AND salary
-- 4
SELECT empno,empname,deptno,salary,ROUND(salary/12,0) as msalary,DATE_FORMAT(hdate,'%M') as hmonth FROM emp



SELECT DATE_FORMAT(hdate,'%Y') AS YEAR,
ROUND(AVG(salary),1) AS avg_salary
FROM emp
GROUP BY DATE_FORMAT(hdate,'%Y')
HAVING ROUND(AVG(salary),1) >= 3000
-- 2.
SELECT deptno,DATE_FORMAT(hdate,'%Y') AS YEAR,
ROUND(AVG(salary),1) AS avg_salary
FROM emp
GROUP BY deptno,DATE_FORMAT(hdate,'%Y')