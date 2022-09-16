CREATE DATABASE videorenamer;
USE videorenamer;
create table usage_log (
RECORDID int not null AUTO_INCREMENT,
USERNAME varchar(255),
DATE date,
TIME time,
FILENAME0 varchar(255),
FILENAME1 varchar(255),
DURATION float(10),
primary key (RECORDID)
);

CREATE DATABASE Version_Control;
USE Version_Control;
CREATE TABLE version_log (
RECORDID INT NOT NULL auto_increment,
APPLICATION VARCHAR(255) NOT NULL,
VERSION_NUMBER decimal(3,2) NOT NULL,
UPDATE_DATE DATETIME,
PRIMARY KEY (RECORDID)
);