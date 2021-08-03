SELECT * FROM dept;
SELECT * FROM EMP;
SELECT * FROM TITLE;
#5
SELECT deptno,ROUND(AVG(salary/12),0) AS msalary FROM emp GROUP BY deptno HAVING ROUND(AVG(salary/12),0) >= 300

#6
SELECT deptno, ROUND(AVG(salary),0) AS salaryavg
FROM emp INNER JOIN title
ON emp.titleno = title.titleno
WHERE title.titlename = '사원' OR title.titlename = '대리'
GROUP BY deptno

#7
SELECT ROUND(AVG(salary/12),0) AS msalary FROM emp WHERE (DATE_FORMAT(hdate,'%Y') >= 2000) and (DATE_FORMAT(hdate,'%Y') <= 2002)

#8
SELECT AVG(salary),deptno,
RANK() OVER (ORDER BY salary DESC) RANK
 FROM emp GROUP BY deptno

#9
SELECT emp.*, dept.deptname,dept.deptloc 
FROM emp INNER JOIN dept
ON emp.deptno = dept.deptno
WHERE dept.deptloc = '서울'
#9_2
SELECT *
FROM emp
WHERE deptno in (SELECT deptno FROM dept WHERE (deptloc = '서울'OR deptloc = '부산'));


#10
SELECT *
FROM emp
WHERE deptno in (SELECT deptno FROM emp WHERE empname = '이영자');
#11
SELECT emp.*
FROM emp
WHERE titleno in (SELECT titleno FROM emp WHERE empname = '김강국')

#12
SELECT emp.empname,dept.deptname,dept.deptloc,title.titlename,emp.salary FROM emp 
LEFT JOIN dept ON emp.deptno = dept.deptno
JOIN title ON emp.titleno = title.titleno
WHERE salary > (SELECT AVG(salary) FROM emp WHERE dept.deptloc = '대전'))

#13
SELECT * FROM emp 
LEFT JOIN dept ON emp.deptno = dept.deptno
JOIN title ON emp.titleno = title.titleno

SELECT e1.empno, e1.empname , e2.empname FROM emp e1
		INNER JOIN emp  e2 ON e1.manager = e2.empno