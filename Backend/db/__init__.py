# psql -U postgres -h localhost
# CREATE DATABASE blogdbcourse;
# CREATE USER jay with ENCRYPTED PASSWORD 'pwd';
# GRANT ALL PRIVILEGES ON DATABASE blogdbcourse to jay;
# \dn - To view schema
# ALTER SCHEMA public OWNER TO jay;
# ALTER ROLE jay WITH SUPERUSER;
# SELECT usename, usecreatedb, usesuper, valuntil, useconfig FROM pg_user;
