SELECT * FROM dept;
SELECT * FROM EMP;
SELECT * FROM TITLE;

#1
SELECT emp.empno,emp.empname,title.titlename,dept.deptname,dept.deptloc FROM emp 
LEFT JOIN dept ON emp.deptno = dept.deptno
JOIN title ON emp.titleno = title.titleno
WHERE DATE_FORMAT(Hdate,'%Y') >= 2000

#2
SELECT deptname, ROUND(AVG(salary),0) AS salaryavg
FROM emp INNER JOIN dept
ON emp.deptno = dept.deptno
GROUP BY deptname
HAVING salaryavg > 3000
#3 _ 경기지역이 없어서 부산으로 변경
SELECT ROUND(AVG(salary),0) AS salavg,dept.deptloc 
FROM emp INNER JOIN dept
ON emp.deptno = dept.deptno
WHERE dept.deptloc = '부산'

#4
SELECT empname, round(DATEDIFF(curdate(),hdate)/30,0) as '근속월수'
FROM emp
WHERE titleno in (SELECT titleno FROM emp WHERE empname = '홍영자')

#5
SELECT RANK() OVER (ORDER BY round(DATEDIFF(curdate(),hdate)/365,0) desc) as 순위,empname, round(DATEDIFF(curdate(),hdate)/365,0) as '근속년수', title.titlename, dept.deptname FROM emp 
LEFT JOIN dept ON emp.deptno = dept.deptno
JOIN title ON emp.titleno = title.titleno



 
