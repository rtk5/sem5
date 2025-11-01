## Unary



EMPLOYEE



σDno=5(EMPLOYEE)



πSsn,Fname,Dno(σDno=5(EMPLOYEE))



ρSsn→USN,Fname→Empname(πSsn,Fname,Dno(σDno=5(EMPLOYEE)))



## Binary



&nbsp;res1 = πSsn(σDno=5(EMPLOYEE))

&nbsp;

&nbsp;res2 = πMgr\_ssn(DEPARTMENT)

&nbsp;

&nbsp;res1∪res2



&nbsp;res1-res2





&nbsp;res1 = πSsn(σDno=5(EMPLOYEE))

&nbsp;

&nbsp;res2 = πMgr\_ssn,Dname(DEPARTMENT)

&nbsp;

&nbsp;res1 ⨯ res2

&nbsp;

## Aggregate



γcount(Ssn)→Total\_emp,sum(Salary)→Total\_sal,avg(Salary)→Avg\_sal,min(Salary)→Low\_salary,max(Salary)→Large\_sal(EMPLOYEE)



γDno;count(Ssn)→Total\_emp,sum(Salary)→Total\_sal,avg(Salary)→Avg\_sal,min(Salary)→Low\_salary,max(Salary)→Large\_sal(EMPLOYEE)









