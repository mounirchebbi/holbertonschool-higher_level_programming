-- create user with all priviledeges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEDGES on *.* to user_0d_1;
FLUSH PRIVILEDGES;
