# harbour_database

1. Oracle 11g express is used for Server side database service
2. user: haitong, password: 111111 need be added with create session and any privilege
	 	SQL> connect / as sysdba
		Connected.
		SQL> alter user sys identified by 111111;
		
		User altered.
		
		SQL> create user haitong identified by 111111;
		
		User created.
		
		SQL> grant create session to haitong;
		
		Grant succeeded.
		
		SQL> grant create session, grant any privilege to haitong;
		
		Grant succeeded.

3. 