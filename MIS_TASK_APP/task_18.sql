pg_dump -U postgres -d TASK_MIS_APP -F c -f "C:\postgres_data\TASK_MIS_APP.backup" --for backup ADD

pg_restore -U postgres -d TASK_MIS_APP_RESTORE "C:\postgres_data\TASK_MIS_APP.backup" --for restore the DATABASE

