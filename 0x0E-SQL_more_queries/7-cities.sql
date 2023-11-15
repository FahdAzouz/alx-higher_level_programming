-- Creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Create table 'cities' in db 'hbtn_0d_usa'
-- id INT unique, auto generated, not null, primary key
-- state_id INT not null, foreign key that references id of 'states' table
-- name VARCHAR(256) not null
-- If table already exists, script should not fail
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities
(
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY (state_id)
		REFERENCES hbtn_0d_usa.states(id)
);
