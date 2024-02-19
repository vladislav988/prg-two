CREATE TABLE IF NOT EXISTS певцы(
id serial PRIMARY KEY,
name varchar(50)
);

CREATE TABLE альбомы(
id serial PRIMARY KEY,
name varchar(50)
);
CREATE TABLE жанры(
id serial PRIMARY KEY,
name varchar(50)
);
CREATE TABLE сборнки(
id serial PRIMARY KEY,
name varchar(50),
year_of_release serial
);

CREATE TABLE певцы(
id serial PRIMARY KEY,
name varchar(30)
);

CREATE TABLE песни(
id serial PRIMARY KEY,
name varchar(50),
альбом serial,
длительность integer
);

CREATE TABLE певцы_жанры(
певец serial,
альбом serial
);

CREATE TABLE песни_сборники(
псеня serial,
сборник serial
);