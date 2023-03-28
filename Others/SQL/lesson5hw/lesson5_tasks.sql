USE shop;

/*
 * Домашнее задание к занятию (видеоуроку) №5.
 */

/*
 * Практическое задание по теме «Операторы, фильтрация, сортировка и ограничение»
 */

/* 
 * Таск 1.
 * Пусть в таблице users поля created_at и updated_at оказались незаполненными. Заполните их текущими датой и временем.
 */
SELECT * FROM users;
INSERT INTO users (name, birthday_at, created_at, updated_at) VALUES
	('Антон', '1994-7-02', NULL, NULL),
	('Антон', '1994-7-02', NOW(), NULL),
	('Антон', '1994-7-02', NULL, NOW());
DELETE FROM users WHERE name = 'Антон';

-- вариант через if
UPDATE users 
	SET created_at = IF(created_at IS NULL, NOW(), created_at),
		updated_at = IF(updated_at IS NULL, NOW(), updated_at)
	WHERE created_at IS NULL OR updated_at IS NULL;

-- вариант через case
UPDATE users 
	SET created_at = CASE WHEN created_at IS NULL THEN NOW() ELSE created_at END,
		updated_at = CASE WHEN updated_at IS NULL THEN NOW() ELSE updated_at END
	WHERE (created_at IS NULL) OR (updated_at IS NULL);

/*
 * Таск 2.
 * Таблица users была неудачно спроектирована. Записи created_at и updated_at были заданы типом VARCHAR и в них долгое
 * время помещались значения в формате 20.10.2017 8:10. Необходимо преобразовать поля к типу DATETIME, сохранив введённые
 * ранее значения.
 */

DROP TABLE IF EXISTS users_invaild;
CREATE TABLE users_invaild (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) COMMENT 'Имя покупателя',
  birthday_at DATE COMMENT 'Дата рождения',
  created_at VARCHAR(64) DEFAULT '20.10.2017 8:10',
  updated_at VARCHAR(64) DEFAULT '20.10.2017 8:10'
) COMMENT = 'Покупатели';

INSERT INTO users_invaild (name, birthday_at, created_at, updated_at) VALUES
  ('Геннадий', '1990-10-05', '20.10.2017 8:10', '20.10.2017 06:12'),
  ('Наталья', '1984-11-12', '20.10.2017 1:02', '20.10.2017 8:10'),
  ('Александр', '1985-05-20', '20.10.2017 15:10', '20.10.2017 14:10'),
  ('Иван', '1998-01-12', NULL, NULL);
 
 SELECT * FROM users_invaild;

-- Результат через str_to_date и alter table modify.
UPDATE users_invaild 
	SET created_at = STR_TO_DATE(created_at,'%d.%m.%Y %H:%i'),
		updated_at = STR_TO_DATE(updated_at,'%d.%m.%Y %H:%i');
ALTER TABLE users_invaild
	MODIFY created_at DATETIME,
	MODIFY updated_at DATETIME;

/*
 * Таск 3.
 * В таблице складских запасов storehouses_products в поле value могут встречаться самые разные цифры: 0, если товар закончился
 * и выше нуля, если на складе имеются запасы. 
 * Необходимо отсортировать записи таким образом, чтобы они выводились в порядке увеличения значения value.
 * Однако нулевые запасы должны выводиться в конце, после всех записей.
 */

TRUNCATE TABLE storehouses;
INSERT INTO storehouses SET name = 'Склад №1';
TRUNCATE TABLE storehouses_products; 
INSERT INTO storehouses_products (storehouse_id, product_id, value) VALUES
	(1, 1, 999999),
	(1, 1, 0),
	(1, 2, 0),
	(1, 3, 0),
	(1, 4, 15),
	(1, 5, 100),
	(1, 6, 0);

-- первый вариант. Вначале сортировка по условию value = 0, а потом для каждой отсортированной группы идет сортировка по возрастанию.
SELECT * FROM storehouses_products
ORDER BY value = 0, value ASC;

-- второй вариант с использованием case ..when .. then ...
-- max_int_unsigned = 4294967295
SELECT * FROM storehouses_products
ORDER BY 
	CASE WHEN value = 0 THEN 4294967295 ELSE value END ASC;

/*
 * Таск 4.
 * (по желанию) Из таблицы users необходимо извлечь пользователей, родившихся в августе и мае.
 * Месяцы заданы в виде списка английских названий (may, august)
 */

SELECT * FROM users WHERE MONTHNAME(birthday_at) = 'may' OR MONTHNAME(birthday_at) = 'august';

/*
 * Таск 5.
 * (по желанию) Из таблицы catalogs извлекаются записи при помощи запроса. SELECT * FROM catalogs WHERE id IN (5, 1, 2); 
 * Отсортируйте записи в порядке, заданном в списке IN.
 */

SELECT * FROM catalogs WHERE id IN (5, 1, 2)
ORDER BY id != 5, id; 


/*
 * Практическое задание теме «Агрегация данных»
 */

/* 
 * Таск 1.
 * Подсчитайте средний возраст пользователей в таблице users.
 */

SELECT birthday_at, TIMESTAMPDIFF(YEAR, birthday_at, NOW()) FROM users;

-- средний возраст пользователей в таблице users:
SELECT AVG(age) 
FROM  
	(SELECT TIMESTAMPDIFF(YEAR, birthday_at, NOW()) AS age FROM users) AS sub_tbl;


/* 
 * Таск 2.
 * Подсчитайте количество дней рождения, которые приходятся на каждый из дней недели. Следует учесть, что необходимы дни 
 * недели текущего года, а не года рождения.
 */

SELECT 
-- 	GROUP_CONCAT(name SEPARATOR ', ') AS birthday_users,
	DAYNAME(DATE(CONCAT_WS('-', YEAR(NOW()), MONTH(birthday_at), DAY(birthday_at)))) AS day_of_week,
	COUNT(*) AS amount
FROM users
GROUP BY day_of_week;
