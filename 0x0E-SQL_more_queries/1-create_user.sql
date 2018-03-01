--  creates the MySQL server user user_0d_1
CREATE IF NOT EXISTS USER 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
