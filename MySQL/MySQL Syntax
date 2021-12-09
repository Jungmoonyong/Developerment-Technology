## MySQL

- MySQL 이란 RDBMS 의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어입니다.

## SQL 문법

- 데이터 정의 언어 DDL
- 데이터 조작 언어 DML
- 데이터 제어 언어 DCL

## DDL

- Create
- Drop
- Alter

## DML

- Select
- Insert
- Update
- Delete

## DCL

- Grant
- Revoke

## Show

```sql
show databases;
show tables;
```

## Use

```sql
use members;
```

## desc

```sql
desc members;
```

## Create

```sql
create database [db_name];
create database members;

create table [name] [column_name] [data_type];
create table members(seq int, name char(20), email char(50));
```

## Drop

```sql
drop [database / table] [name];
drop table members;
```

## Insert

```sql
insert into [table_name] [column 1] values [data];
insert into members(seq, name, email) values(1, 'admin', 'admin@gmail.com');
insert into members(seq, name, email) values(2, 'moon', 'moon@gmail.com');
insert into members(seq, name, email) values(3, 'test', 'test@gmail.com');
insert into members(seq, name, email) values(4, 'guest', 'guest@gmail.com');
insert into members(seq, name, email) values(5, 'hi', 'hi@gmail.com');
```

## Select

```sql
select [column 1] from [table] where [condition];
select * from members;
select * from members where seq=1;
```

## Update

```sql
update table set [column 1]=[data 1] where [condition];
update members set name='test' where seq=1;
```

## Delete

```sql
delete from [table] where [condition];
delete from members where seq=1;
```

## 연산자

- 산술 연산자
    
    ```sql
    select 1+4;
    select 1+4*2;
    select * from members where seq=2-1;
    ```
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6ad9e357-3235-4a71-8e19-f0a7258d4bfc/Untitled.png)
    
- 비교 연산자
    
    ```sql
    select * from members where seq > 2;
    select * from members where seq >= 2;
    select * from members where seq < 3;
    select * from members where seq <> 3;
    select * from members where seq != 3;
    ```
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e2623cfa-12cf-4659-8276-eafc0ba6f9cc/Untitled.png)
    
- 논리 연산자
    
    ```sql
    not 1=2 True
    1=1 and 1=1 True
    1=1 or 1=2 True
    
    select * from members where not seq=1>2;
    select * from members where seq=1 or seq=5;
    select * from members where seq=1 and name='admin';
    ```
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1730e866-5b76-4636-8127-248f7deb98a1/Untitled.png)
    
- 비트 논리 연산자
    
    ```sql
    1=1 xor 1=2 True
    
    select 1&1;
    select 2&1;
    select 3&1;
    select 5&3;
    select 5|3;
    ```
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/214d08e1-0684-4fcb-a693-87768efe629b/Untitled.png)
    
- 연결 연산자
    
    ```sql
    select 'te' 'st'
    select * from members where name='ad' 'min';
    select concat('Jung', 'Moon', 'Yong');
    ```
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5a3197c7-e5df-4248-87cf-e4a203979b2c/Untitled.png)
    
- IN 연산자
    
    ```sql
    [컬럼 / 값] in (값1, 값2)
    select * from members where name in ('admin', 'moon');
    select * from members where name not in ('admin', 'moon');
    ```
    
- LIKE 연산자
    
    ```sql
    select * from members where name like '%admin%';
    select * from members where name like 'ad_in';
    select * from members where name like '%@gmail.com';
    ```
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3baa9391-d64e-41c2-8452-efbc46b3e475/Untitled.png)
    
    ## 함수
    

## 함수

- 문자열 함수
    
    ```sql
    select substring('test',1,1);
    select substring('test',2,1);
    select substring('test',3,1);
    select substring('test',4,1);
    
    select substr('test',1,1);
    select substr('test',2,1);
    select substr('test',3,1);
    select substr('test',4,1);
    
    select mid('test',1,1);
    select mid('test',2,1);
    select mid('test',3,1);
    select mid('test',4,1);
    ```
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3aac1577-3a2b-415d-b43f-60b27c68c21a/Untitled.png)
    
- 아스키 코드 변환 함수
    
    ```sql
    select ascii('a');
    select bin(ascii('a'));
    
    select ascii(substring('test',1,1));
    select ascii(substring('test',2,1));
    select ascii(substring('test',3,1));
    select ascii(substring('test',4,1));
    
    select char(97);
    select concat(char(97), char(100), char(109), char(105), char(110));
    ```
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fddcade9-0220-40de-b15e-7f88f5d4f396/Untitled.png)
    
- COUNT 함수
    
    ```sql
    select count(column) from [table]
    select count(*) from members;
    ```
    
- 길이 함수
    
    ```sql
    select length('test');
    select name, length(email) from members;
    ```
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ebd2db13-f640-4d17-9a1d-60a4b6902801/Untitled.png)
    

## 조건문

```sql
case when [condition] then [true] else [false] end
select case when 1=1 then 1 else 2 end;
select if(1=1, 1, 2);
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0d138a91-754b-4d3a-a969-ef12757ee89f/Untitled.png)

## Order By 절을 이용한 정렬

```sql
select column 1 , column 2 from table order by column [asc / desc]
select * from members order by seq asc;
select * from members order by seq desc;
select * from members order by 1;
```

## 레코드 출력 개수 제한

```sql
select column 1, column 2 from table limit [offset] , [row_count]
select column 1, column 2 from table limit [row_count]
select * from members limit 1;
	select * from members limit 0,1;
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fad65a9f-9dc0-4db8-acc2-4b0dcbc60bdf/Untitled.png)

## Group By

```sql
select name from test group by name;
select name, couunt(name), sum(quantity) from test group by name;
select name, couunt(name), sum(quantity) from test group by name having count(name) = 1;
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a821c669-fe02-4d67-8db7-88228eced336/Untitled.png)

## Sub Query

```sql
select column 1 , column 2 from table where [condition] = (select column from table where column=[value])

select Sub Query from Sub Query a where [column] = Sub Qeury

select : 스칼라 서브쿼리 하나의 레코드 , 하나의 데이터
from : 인라인 뷰 a 라는 가상 테이블로 서브쿼리가 실행되고 결과가
반환이 되는데 그 결과 반환되는데 a 라는 가상테이블을 형성이 됩니다
where : 일반 서브쿼리 연산자에 따라서 반환되는 레코드 개수 와 컬럼 수가
다르게 됩니다

단일 행 서브쿼리
select name, email from members where id=(select id from bbs where idx=192)
다중 행 서브쿼리
select name, email from members where id in(select id from bbs)

select * from members;
select name, (select version()) from members;
select name, (select email from members where seq=a.seq) from members.a;
select * from (select * from embers)a;
select * from (select * from embers)a where a.seq=1;
select * from members where seq=(select 1);
select * from members where seq=(select seq from members where name='admin');
select * from members where seq in(select seq from members);
```

## Union

```sql
select name from members union select email from members;
```

---

## Reference

Reference : 

[[무료] 성공적인 SQL 인젝션 공격을 위한, SQL 기본 문법 - 인프런 | 강의](https://www.inflearn.com/course/SQL-%EC%9D%B8%EC%A0%9D%EC%85%98-%EA%B3%B5%EA%B2%A9-%EA%B8%B0%EB%B3%B8-%EB%AC%B8%EB%B2%95/dashboard)
