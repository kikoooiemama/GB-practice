USE shop;

/*
 * Домашнее задание к занятию (видеоуроку) №9.
 */

/*
 * Практическое задание по теме “Транзакции, переменные, представления”
 */

/* 
 * Таск 1.
 * В базе данных shop и sample присутствуют одни и те же таблицы, учебной базы данных.
 * Переместите запись id = 1 из таблицы shop.users в таблицу sample.users. Используйте транзакции.
 */
USE shop;

START TRANSACTION;

INSERT INTO sample.users (name, birthday_at, created_at, updated_at)
SELECT users.name, users.birthday_at, users.created_at, users.updated_at
FROM users
WHERE users.id = 1;

DELETE FROM users WHERE id = 1;

COMMIT;

-- DROP DATABASE IF EXISTS sample;
-- CREATE DATABASE sample;
-- USE sample;
-- DROP TABLE IF EXISTS users;
-- CREATE TABLE users (
--   id SERIAL PRIMARY KEY,
--   name VARCHAR(255) COMMENT 'Имя покупателя',
--   birthday_at DATE COMMENT 'Дата рождения',
--   created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
--   updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
-- ) COMMENT = 'Покупатели';

-- INSERT INTO users (id, name, birthday_at) VALUES
--   (1, 'Геннадий', '1990-10-05');

/* 
 * Таск 2.
 * Создайте представление, которое выводит название name товарной позиции из таблицы products
 *  и соответствующее название каталога name из таблицы catalogs.
 */
CREATE OR REPLACE VIEW cut_products (product_name, catalog_name) AS
	SELECT 	p.name, c.name
	FROM catalogs c JOIN products p 
	ON c.id = p.catalog_id;

SELECT * FROM cut_products cp;


/*
 * Практическое задание по теме “Администрирование MySQL” (эта тема изучается по вашему желанию)
 */

/* 
 * Таск 1.
 * Создайте двух пользователей которые имеют доступ к базе данных shop. 
 * Первому пользователю shop_read должны быть доступны только запросы на чтение данных,
 * второму пользователю shop — любые операции в пределах базы данных shop.
 */

-- создаем первого пользователя без пароля (можно и паролем, но в задании не указано), по-умолчанию у него нет прав - только usage.
CREATE USER shop_read;
SHOW GRANTS FOR shop_read;
-- задаем первому пользователю только права на чтение таблиц из db shop.
GRANT SELECT ON shop.* TO shop_read;

-- создаем второго пользователя без пароля (можно и паролем, но в задании не указано), по-умолчанию у него нет прав - только usage.
CREATE USER shop;
SHOW GRANTS FOR shop;
-- даем права пользователю shop в пределах базы данных shop.
GRANT ALL ON shop.* TO shop;
-- все права, включая право выдавать различные привелегии в пределах базы данных shop.
GRANT GRANT OPTION ON shop.* TO shop;


/*
 * Практическое задание по теме “Хранимые процедуры и функции, триггеры"
 */

SELECT HOUR(NOW());

/* 
 * Таск 1.
 * Создайте хранимую функцию hello(), которая будет возвращать приветствие, в зависимости от текущего времени суток.
 * С 6:00 до 12:00 функция должна возвращать фразу "Доброе утро",
 * с 12:00 до 18:00 функция должна возвращать фразу "Добрый день",
 * с 18:00 до 00:00 — "Добрый вечер",
 * с 00:00 до 6:00 — "Доброй ночи".
 */

DROP FUNCTION IF EXISTS hello;
DELIMITER //
CREATE FUNCTION hello()
RETURNS varchar(64) DETERMINISTIC
BEGIN 
	DECLARE hours INT;
	SET hours = HOUR(CURRENT_TIME());
	IF (hours >= 6 AND hours < 12) THEN
		RETURN 'Доброе утро';
	ELSEIF (hours >= 12 AND hours < 18) THEN
		RETURN 'Добрый день';
	ELSEIF (hours >= 18) THEN	
		RETURN 'Добрый вечер';
	ELSE 
		RETURN 'Доброй ночи';
	END IF;
END //
DELIMITER ;

SELECT hello();

/* 
 * Таск 2.
 * В таблице products есть два текстовых поля: name с названием товара и description с его описанием.
 * Допустимо присутствие обоих полей или одно из них. Ситуация, когда оба поля принимают неопределенное значение NULL неприемлема.
 * Используя триггеры, добейтесь того, чтобы одно из этих полей или оба поля были заполнены.
 * При попытке присвоить полям NULL-значение необходимо отменить операцию.
 */

-- Не совсем понимаю задание, некорректное условие какое-то. Триггеры же действуют только при update, delete, insert.
-- Если в таблице уже есть NULL значения, тригеры этого не исправят же. А что бы создать процедуру по добавлению данных,
-- то нужны данные, которых нет как бы..
-- Как я понял при добавлении (insert) хотя бы одно значение должно быть не NULL. А при обновлении (update) NULL-значение вообще
-- нельзя никому присваивать в принципе.

-- Триггер на добавление. Если оба значения NULL - ошибка, если хотя бы одно не NULL, то запись проходит.
DROP TRIGGER IF EXISTS check_product_before_insert;
DELIMITER //
CREATE TRIGGER check_product_before_insert BEFORE INSERT ON products
FOR EACH ROW 
BEGIN 
	IF (COALESCE(NEW.name, NEW.description) IS NULL) THEN 
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'INSERT canceled. Parameters NAME and DESCRIPTION are NULL.';
	END IF;
END //
DELIMITER ;

-- INSERT INTO products (name) VALUES ('qq');
-- 
-- INSERT INTO products (price) VALUES ('123123');
-- 
-- INSERT INTO products (description) VALUES ('qq');
-- 
-- INSERT INTO products (name, description) VALUES (NULL, NULL);
-- 
-- INSERT INTO products (name, description) VALUES ('first', NULL);
-- 
-- INSERT INTO products (name, description) VALUES (NULL, 'first');
-- 
-- INSERT INTO products (name, description) VALUES ('one', 'two');
-- 
-- INSERT INTO products (name, description) VALUES (NULL, NULL);

-- Тригер на обновление данных. При попытке присвоить полям (обоим, как я понимаю) NULL-значение операция отменяется.
-- Если хотя бы одному полю, которое не NULL, пытаемся присвоить значение NULL, то операция отменяется, т.к. нельзя присваивать NULL
-- значения ни одному из полей, нельзя затирать данные.
-- Если обоим полям с NULL присваивается NULL, то операция отменяется.
-- Если только одному полю с изначальным значением NULL присваивается NULL, а другому присваивается не NULL, то операция выполняется,
-- т.к. условие что хотя бы одно поле будет не NULL соблюдается.

DROP TRIGGER IF EXISTS check_product_before_update;
DELIMITER //
CREATE TRIGGER check_product_before_update BEFORE UPDATE ON products
FOR EACH ROW 
BEGIN 
	IF (NEW.name IS NULL) AND (OLD.name IS NOT NULL) THEN 
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'UPDATE canceled. The "name" parameter is not NULL. Therefore, parameter "name" cannot be assigned a NULL value.';
	END IF;
	IF(NEW.description IS NULL) AND (OLD.description IS NOT NULL) THEN 
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'UPDATE canceled. The "description" parameter is not NULL. Therefore, parameter "description" cannot be assigned a NULL value.';
	END IF;
	-- если таблица имеет NULL, NULL значения и мы пытаемся присвоить снова значения NULL, NULL, то ошибка
	IF(COALESCE(NEW.name, NEW.description) IS NULL) THEN 
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'UPDATE canceled. Parameters NAME and DESCRIPTION are NULL.';
	END IF;
END //
DELIMITER ;

-- UPDATE products SET name = NULL WHERE id = 10;
-- 
-- UPDATE products SET name = 'privet', description = NULL WHERE id = 14;
-- 
-- UPDATE products SET name = NULL, description = 'privet' WHERE id = 14;
-- 
-- UPDATE products SET description = NULL WHERE id = 11;
-- 
-- UPDATE products SET name = 'two' WHERE id = 12;
-- 
-- UPDATE products SET description = 'two' WHERE id = 13;
-- 
-- UPDATE products SET name = 'two' WHERE id = 13;
-- 
-- UPDATE products SET description = 'two' WHERE id = 12;
-- 
-- UPDATE products SET description = 'two' WHERE id = 15;
-- 
-- UPDATE products SET name = 'two' WHERE id = 16;

/* 
 * Таск 3.
 * (по желанию) Напишите хранимую функцию для вычисления произвольного числа Фибоначчи.
 * Числами Фибоначчи называется последовательность в которой число равно сумме двух предыдущих чисел.
 * Вызов функции FIBONACCI(10) должен возвращать число 55.
 */

DROP FUNCTION IF EXISTS FIBONACCI;
DELIMITER //
CREATE FUNCTION FIBONACCI(serial_number INT UNSIGNED)
RETURNS BIGINT UNSIGNED DETERMINISTIC
BEGIN
	DECLARE i INT DEFAULT 3;
	DECLARE answer, a, b BIGINT UNSIGNED DEFAULT 0;
	DECLARE error_message TEXT;
	IF(serial_number > 93) THEN
		SET error_message =  CONCAT('Число Фибоначчи под номером ', serial_number, ' выходит из диапазона BIGINT UNSIGNED и не может быть подсчитано.');
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = error_message;
	END IF;
	IF(serial_number = 0) THEN
		RETURN 0;
	ELSEIF(serial_number < 3) THEN 
		RETURN 1;
	END IF;
	SET a = 1;
	SET b = 1;
	WHILE i < (serial_number + 1) DO
		SET answer = a + b;
		SET a = b;
		SET b = answer;
		SET i = i + 1;
	END WHILE;
	RETURN answer;
END //
DELIMITER ;

SELECT FIBONACCI(0) AS result;

SELECT FIBONACCI(2) AS result;

SELECT FIBONACCI(10) AS result;

SELECT FIBONACCI(93) AS result;

SELECT FIBONACCI(100) AS result;
