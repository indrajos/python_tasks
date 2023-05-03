CREATE DATABASE geo;

CREATE TABLE IF NOT EXISTS geo.countries (
	id integer PRIMARY KEY AUTO_INCREMENT,
	country text, 
	code text);
            

CREATE TABLE IF NOT EXISTS geo.cities (
	city_id integer PRIMARY KEY, 
	name text, 
	area integer,
	population integer,
	id integer REFERENCES countries(id));

INSERT INTO geo.countries (country, code)
VALUES 
('Lithuania', 'LT'),
('Latvia', 'LV'),
('Estonia', 'EE');

INSERT INTO geo.cities 
VALUES 
(1,'Vilnius', 401, 580020, (SELECT id FROM geo.countries WHERE code = 'LT')),
(2, 'Riga', 307, 605802, (SELECT id FROM geo.countries WHERE code = 'LV')),
(3, 'Tallinn', 159, 460642, (SELECT id FROM geo.countries WHERE code = 'EE'));




