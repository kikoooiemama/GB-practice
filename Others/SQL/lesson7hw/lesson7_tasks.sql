  USE shop;

/*
 * Домашнее задание к занятию (видеоуроку) №5.
 */
 
/* 
 * Таск 1.
 * Составьте список пользователей users, которые осуществили хотя бы один заказ orders в интернет магазине.
 */
 
SELECT * FROM orders;
INSERT INTO orders (user_id) VALUES
	('1'), 	('1'),	('1'),	('1'),	('2'),	('2'),	('2'),	('3'),	('4'),	('4'),	('4'),	('5'),	('5'),	('5'),	('5'),	('5'),	('5');
 
-- результат
SELECT name AS bueyrs FROM users
	WHERE EXISTS (SELECT 1 FROM orders WHERE user_id = users.id);
 
 /* 
 * Таск 2.
 * Выведите список товаров products и разделов catalogs, который соответствует товару.
 */
 
SELECT * FROM products p ;

-- результат
SELECT 
	p.name,
	p.description,
	p.price,
	c.name AS catalog_name
FROM catalogs c JOIN products p 
ON c.id = p.catalog_id;
 
 /* 
 * Таск 3.
 * (по желанию) Пусть имеется таблица рейсов flights (id, from, to) и таблица городов cities (label, name).
 *  Поля from, to и label содержат английские названия городов, поле name — русское. Выведите список рейсов flights с русскими названиями городов.
 */

-- результат
SELECT 
	id,
	(SELECT name FROM cities WHERE label = flights.from_name) AS 'from',
	(SELECT name FROM cities WHERE label = flights.name_to) AS 'to'
FROM flights;
	

-- таблицы
DROP TABLE IF EXISTS cities;
CREATE TABLE cities (
  label VARCHAR(128) NOT NULL,
  name VARCHAR(128),
  PRIMARY KEY (label)
);
INSERT INTO cities (label, name) VALUES
	('moscow', 'Москва'),
	('novgorod', 'Новгород'),
	('irkutsk', 'Иркутск'),
	('kazan','Казань'),
	('omsk','Омск');
SELECT * FROM cities;

DROP TABLE IF EXISTS flights;
CREATE TABLE flights (
  id SERIAL PRIMARY KEY,
  from_name VARCHAR(128) COMMENT 'Откуда',
  name_to VARCHAR(128) COMMENT 'Куда',
  KEY label_for_from_idx (from_name),
  KEY label_for_to_idx (name_to),
  CONSTRAINT label_for_from_fk FOREIGN KEY (from_name) REFERENCES cities (label), 
  CONSTRAINT label_for_to_fk FOREIGN KEY (name_to) REFERENCES cities (label)
);
INSERT INTO flights (from_name, name_to) VALUES
	('moscow', 'omsk'),
	('novgorod', 'kazan'),
	('irkutsk', 'moscow'),
	('omsk','irkutsk'),
	('moscow','kazan');
SELECT * FROM flights;