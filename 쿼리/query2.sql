SELECT * FROM emp;
SELECT empname,salary,ROUND(salary * 0.1,0) AS tax, ROUND(salary*(1-0.1)) AS atsalary FROM emp

SELECT empname,salary,DATE_FORMAT(hdate,'%Y') AS YEAR FROM emp WHERE DATE_FORMAT(hdate,'%Y') < 2001 AND salary < 4000 

SELECT empname,manager FROM emp WHERE empname like '%자%' AND manager IS NOT NULL

SELECT *,
(CASE WHEN salary < 2000 THEN '하' WHEN (salary >= 2000 AND salary < 4000) THEN '중' ELSE '고' END) AS rank
FROM emp

