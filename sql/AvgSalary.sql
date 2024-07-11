-- https://school.programmers.co.kr/learn/courses/30/lessons/284529

select EMP.DEPT_ID, DPT.DEPT_NAME_EN, EMP.AVG_SAL
from (
    select DEPT_ID, round(avg(SAL), 0) as AVG_SAL
    from HR_EMPLOYEES 
    group by DEPT_ID
) as EMP 
    left join HR_DEPARTMENT as DPT 
    on EMP.DEPT_ID = DPT.DEPT_ID 
order by EMP.AVG_SAL desc
;