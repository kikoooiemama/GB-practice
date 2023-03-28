/*
 * ћодифицируем базу
 */
USE vk;
-- совершенствуем таблицу дружбы
-- добавл€ем ограничение, что отправитель запроса на дружбу 
-- не может быть одновременно и получателем

ALTER TABLE friend_requests 
ADD CONSTRAINT sender_not_reciever_check
CHECK (from_user_id != to_user_id);


SELECT * FROM friend_requests;

-- добавл€ем ограничение, что номер телефона должен состо€ть из 11
-- символов и только из цифр
-- https://regex101.com/
ALTER TABLE users 
ADD CONSTRAINT phone_check
CHECK (REGEXP_LIKE(phone, '^[0-9]{11}$'));

-- делаем foreign key на media
ALTER TABLE profiles 
ADD CONSTRAINT fk_profiles_media
FOREIGN KEY (photo_id) REFERENCES media (id);

/* 
  C - Create = INSERT
  R - Read   = SELECT
  U - Update = UPDATE
  D - Delete = DELETE
*/

/*
 * INSERT
 * https://dev.mysql.com/doc/refman/8.0/en/insert.html
 */

-- добавл€ем пользовател€
INSERT INTO users (id, first_name, last_name, email, phone, password_hash)
VALUES (DEFAULT, 'Alex', 'Stepanov', 'alex@mail.com', '89213546566', 'aaa');

SELECT * FROM users;

-- добавл€ем повторно того же пользовател€, ошибка не возникает
INSERT IGNORE INTO users (id, first_name, last_name, email, phone, password_hash)
VALUES (DEFAULT, 'Alex', 'Stepanov', 'alex@mail.com', '89213546566', 'aaa');

-- не указываем default значени€
INSERT users (first_name, last_name, email, phone)
VALUES ('Lena', 'Stepanova', 'lena@mail.com', '89213546568');

-- не указываем названи€ колонок
INSERT users 
VALUES (DEFAULT, 'Chris', 'Ivanov', 'chris@mail.com', '89213546560', DEFAULT, DEFAULT);

-- €вно задаем id
INSERT INTO users (id, first_name, last_name, email, phone)
VALUES (55, 'Jane', 'Kvanov', 'jane@mail.com', '89293546560');

-- пробуем добавить id меньше текущего
INSERT INTO users (id, first_name, last_name, email, phone) VALUES 
(45, 'Jane', 'Night', 'jane_n@mail.com', '89293946560');

-- добавл€ем несколько пользователей
INSERT INTO users (first_name, last_name, email, phone)
VALUES ('Igor', 'Petrov', 'igor@mail.com', '89213549560'),
		('Oksana', 'Petrova', 'oksana@mail.com', '89213549561');


-- добавл€ем через SET
INSERT INTO users 
SET first_name = 'Iren',
	last_name = 'Sidorova',
	email = 'iren@mail.com',
	phone  = '89213541560';

-- получаем код создани€ таблицы users
SHOW CREATE TABLE users;
-- код создани€ таблицы users
CREATE TABLE `users` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `first_name` varchar(145) NOT NULL,
  `last_name` varchar(145) NOT NULL,
  `email` varchar(145) NOT NULL,
  `phone` char(11) NOT NULL,
  `password_hash` char(65) DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `phone` (`phone`),
  KEY `email_2` (`email`)
);

-- переключаемс€ к Ѕƒ test2 и добавл€ем в неЄ таблицу users
USE test2;

-- ƒобавл€ем данные в test2 гыукы
INSERT INTO users (first_name, last_name, email, phone)
VALUES ('Alina', 'Kobrina', 'alina@mail.com', '89210549561');

-- ѕереключаемс€ обратно к Ѕƒ vk
USE vk;
-- ¬ыполн€ем INSERT ... SELECT 
INSERT users (first_name, last_name, email, phone)
SELECT first_name, last_name, email, phone FROM test2.users;

/*
 * SELECT
 * https://dev.mysql.com/doc/refman/8.0/en/select.html
 */

-- выбираем константы

SELECT 'hello!';

SELECT 1+10;

-- выбираем все пол€ users

SELECT * FROM users;


-- выбираем только имена users

SELECT first_name FROM users;

-- выбираем только уникальные имена

SELECT DISTINCT first_name FROM users;


SELECT * FROM users WHERE last_name = 'Petrov';

SELECT * FROM users WHERE id <= 10;

SELECT * FROM users WHERE id BETWEEN 3 AND 7;

-- выбираем пользователей, у которых нет hash парол€ 
SELECT * FROM users WHERE password_hash IS NULL;

-- выбираем пользователей, у которых есть hash парол€ 

SELECT * FROM users WHERE password_hash IS NOT NULL;

-- выбираем четырех пользователей
SELECT * FROM users Limit 4;


-- выбираем четырех последних пользователей
SELECT * FROM users ORDER BY id DESC Limit 4;

-- выбираем четвертого пользовател€ (четвертый номер id по пор€дку)

SELECT * FROM users ORDER BY id LIMIT 1 OFFSET 3;

SELECT * FROM users ORDER BY id LIMIT 3,1;


/*
 * UPDATE
 * https://dev.mysql.com/doc/refman/8.0/en/update.html 
*/

INSERT INTO messages (from_user_id, to_user_id, txt)
VALUES (45, 55, 'Hi!');

INSERT INTO messages (from_user_id, to_user_id, txt)
VALUES (45, 55, 'I hate you!');

SELECT * FROM messages;

-- мен€ем статус на сообщение доставлено

UPDATE messages 
SET is_delivered = TRUE;

-- мен€ем текст сообщени€

UPDATE messages 
SET txt = 'I love you'
WHERE id = 5;

/*
 * DELETE
 * https://dev.mysql.com/doc/refman/8.0/en/delete.html 
 * TRUNCATE
 * https://dev.mysql.com/doc/refman/8.0/en/truncate-table.html
*/

-- удал€ем пользовател€ с фамилией —тепанов

DELETE FROM users WHERE last_name = 'Stepanov';

SELECT * FROM users;

-- удал€ем все строки из messages
DELETE FROM messages;

SELECT * FROM messages;

-- удал€ем все строки из messages
TRUNCATE TABLE messages;

-- Ќельз€ так почистить таблицу, на которую есть внешние ключи
TRUNCATE TABLE users;

-- обнул€ем ограничение на проверку наличи€ на таблицу внешних ключей,
-- чистим таблицы, возвращаем проверку
SET FOREIGN_KEY_CHECKS = 0;

TRUNCATE TABLE users;
SELECT * FROM users;

SET FOREIGN_KEY_CHECKS = 1;

-- добавл€ем посты и лайки...

CREATE TABLE posts(
	id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	user_id BIGINT UNSIGNED NOT NULL,
	txt TEXT NOT NULL,
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
	updated_at DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
	INDEX user_idx (user_id),
	CONSTRAINT user_posts_fk FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE posts_likes (
	post_id BIGINT UNSIGNED NOT NULL,
	user_id BIGINT UNSIGNED NOT NULL,
	like_type BOOLEAN DEFAULT TRUE,
	PRIMARY KEY (post_id, user_id),
	INDEX post_idx (post_id),
	INDEX user_idx (user_id),
	CONSTRAINT posts_likes_fk FOREIGN KEY (post_id) REFERENCES posts (id),
	CONSTRAINT users_likes_fk FOREIGN KEY (user_id) REFERENCES users (id)
);

