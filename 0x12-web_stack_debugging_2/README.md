0-iamsomeoneelse
SET PASSWORD FOR 'replica_user'@'%' = PASSWORD('projectcorrection280hbtn');
CHANGE MASTER TO MASTER_PASSWORD='projectcorrection280hbtn';


mysql> SHOW MASTER STATUS;
+------------------+----------+-------------------------+------------------+-------------------+
| File             | Position | Binlog_Do_DB            | Binlog_Ignore_DB | Executed_Gtid_Set |
+------------------+----------+-------------------------+------------------+-------------------+
| mysql-bin.000002 |      510 | tyrell_corp,tyrell_corp |                  |                   |
+------------------+----------+-------------------------+------------------+-------------------+
1 row in set (0.00 sec)


CHANGE MASTER TO
  MASTER_HOST='54.175.126.159',
  MASTER_USER='replica_user',
  MASTER_PASSWORD='projectcorrection280hbtn',
  MASTER_LOG_FILE='mysql-bin.000002',
  MASTER_LOG_POS=510;
