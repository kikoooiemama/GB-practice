USE shop;

/*
 * Домашнее задание к занятию (видеоуроку) №11.
 */

/*
 * Практическое задание по теме “Оптимизация запросов”
 */

/* 
 * Таск 1.
 * Создайте таблицу logs типа Archive.
 * Пусть при каждом создании записи в таблицах users, catalogs и products в таблицу logs помещается время и дата создания записи,
 * название таблицы, идентификатор первичного ключа и содержимое поля name.
 */

SHOW ENGINES;

DROP TABLE IF EXISTS logs;
CREATE TABLE logs (
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	table_name VARCHAR(255)  NOT NULL,
	primary_key_id BIGINT NOT NULL,
	name_value VARCHAR(255) NOT NULL
	) ENGINE = ARCHIVE;

-- движок archive не поддерживает транзакции и индексы. 
-- делаем триггеры на добавления записей в таблицы users, catalogs и products

DROP TRIGGER IF EXISTS log_entry_users;
DELIMITER //
CREATE TRIGGER log_entry_users AFTER INSERT ON users
FOR EACH ROW 
BEGIN 
	INSERT INTO logs (table_name, primary_key_id, name_value) VALUES ('users', NEW.id, NEW.name);
END //

DELIMITER ;

DROP TRIGGER IF EXISTS log_entry_catalogs;
DELIMITER //
CREATE TRIGGER log_entry_catalogs AFTER INSERT ON catalogs
FOR EACH ROW 
BEGIN 
	INSERT INTO logs (table_name, primary_key_id, name_value) VALUES ('catalogs', NEW.id, NEW.name);
END //

DELIMITER ;

DROP TRIGGER IF EXISTS log_entry_products;
DELIMITER //
CREATE TRIGGER log_entry_products AFTER INSERT ON products
FOR EACH ROW 
BEGIN 
	INSERT INTO logs (table_name, primary_key_id, name_value) VALUES ('products', NEW.id, NEW.name);
END //

DELIMITER ;

-- INSERT INTO users (name, birthday_at) VALUES ('Nikolay', '1996-06-17');
-- 
-- INSERT INTO catalogs (name) VALUES ('Блоки питания');
-- 
-- INSERT INTO products (name, description, price, catalog_id) 
-- 	VALUES ('Chieftec GPS-750C 750W',
-- 		'Блок питания Chieftec Power Smart Series 750W [GPS-750C] – компонент с прекрасными характеристиками, который можно поставить в различные ПК.',
-- 		6600,
-- 		7);
