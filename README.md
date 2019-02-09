# MyFlaskApp
app.py and postgresApp.py renders the same webpage, but by using MySQL and postgresSQL respectively. To run the scripts make sure MySQL is downloaded (if running app.py) and install possible missing python packages with 'pip'.

To set up the databases run 'psql' from the terminal to edit postgresSQL. Then run:

```
CREATE DATABASE myflaskapp;
```

Change to the database with the command '\c myflaskapp', and then create the following tables with the following commands:

```
CREATE TABLE users(id SERIAL PRIMARY KEY, name VARCHAR(100), email VARCHAR(100), username VARCHAR(100), password VARCHAR(100), register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
```

```
CREATE TABLE articles(id SERIAL PRIMARY KEY, title VARCHAR(255), author VARCHAR(100), body TEXT, create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
```

The last configuration is to change the username for the login in the 'postgresApp.py' script (comment show where). 

Simalar setup should be made with MySQL, but no need to change username in 'app.py'.