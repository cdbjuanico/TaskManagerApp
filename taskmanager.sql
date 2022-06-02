/*
Atento, Juanico, Ramis, Rosellon
CMSC 127 T1L
Milestone 03: SQL Queries
2022-05-16
*/

DROP DATABASE IF EXISTS taskmanager;
CREATE DATABASE taskmanager;
GRANT ALL ON taskmanager.* TO 'scott'@'localhost';

USE taskmanager;

CREATE TABLE category (
  categoryid INT(3) NOT NULL AUTO_INCREMENT,
  categoryname VARCHAR(30) NOT NULL,
  CONSTRAINT category_categoryid_pk PRIMARY KEY(categoryid),
  CONSTRAINT category_categoryname_uk UNIQUE(categoryname)
);

CREATE TABLE task (
  taskid INT(5) NOT NULL AUTO_INCREMENT,
  tododate DATE,
  taskname VARCHAR(50) NOT NULL,
  duedate DATE,
  status VARCHAR(10) DEFAULT 'UNFINISHED',
  CONSTRAINT task_taskid_pk PRIMARY KEY(taskid),
  CONSTRAINT task_taskname_uk UNIQUE(taskname)
);

CREATE TABLE belongs_to (
  categoryid INT(3),
  taskid INT(5),
  CONSTRAINT belongs_to_categoryid_taskid_pk PRIMARY KEY(categoryid, taskid),
  CONSTRAINT belongs_to_categoryid_fk FOREIGN KEY(categoryid) REFERENCES category(categoryid),
  CONSTRAINT belongs_to_taskid_fk FOREIGN KEY(taskid) REFERENCES task(taskid)
);
