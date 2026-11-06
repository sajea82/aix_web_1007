-- 주석 : user -> c##user
alter session set "_ORACLE_SCRIPT"=true;

-- ora_user 사용자 등록 명령어 / 패스워드 1111
create user ora_user identified by 1111;
create user ora_user2 identified by 1111;

-- 사용권한
grant connect, resource, dba to ora_user;
grant connect, resource, dba to ora_user2;