DROP DATABASE IF EXISTS lesson4_task3;

CREATE DATABASE lesson4_task3;

USE lesson4_task3;

CREATE TABLE media_types(
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(50) NOT NULL UNIQUE
);

INSERT INTO `media_types` (`id`, `name`) VALUES (1, 'ad');
INSERT INTO `media_types` (`id`, `name`) VALUES (4, 'nesciunt');
INSERT INTO `media_types` (`id`, `name`) VALUES (2, 'nobis');
INSERT INTO `media_types` (`id`, `name`) VALUES (3, 'voluptas');

-- Написать запрос для переименования названий типов медиа (колонка name в media_types), которые вы получили в пункте 2 в image, audio, video, document

UPDATE media_types 
SET name = CASE id 
        WHEN 1 THEN 'image' 
        WHEN 2 THEN 'audio' 
        WHEN 3 THEN 'video' 
        WHEN 4 THEN 'document' 
    END
WHERE id IN (1,2,3,4);

CREATE TABLE users(
	id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	first_name VARCHAR(145) NOT NULL,
	last_name VARCHAR(145) NOT NULL,
	email VARCHAR(145) NOT NULL UNIQUE,
	phone CHAR(11) NOT NULL,
	password_hash CHAR(65) DEFAULT NULL,
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, -- NOW()
	INDEX (phone),
	INDEX (email)
);

CREATE TABLE friend_requests(
	from_user_id BIGINT UNSIGNED NOT NULL,
	to_user_id BIGINT UNSIGNED NOT NULL,
	accepted BOOLEAN DEFAULT FALSE,
	PRIMARY KEY(from_user_id, to_user_id),
	INDEX friend_requests_from_user_id_idx (from_user_id),
	INDEX friend_requests_to_user_id_idx (to_user_id),
	CONSTRAINT fk_friend_requests_from_user_id FOREIGN KEY (from_user_id) REFERENCES users (id),
	CONSTRAINT fk_friend_requests_to_user_id FOREIGN KEY (to_user_id) REFERENCES users (id)
);

-- Заполним таблицу, добавим Петю и Васю
INSERT INTO users VALUES (DEFAULT, 'Petya', 'Petukhov', 'petya@mail.com', '89212223334', DEFAULT, DEFAULT);
INSERT INTO users VALUES (DEFAULT, 'Vasya', 'Vasilkov', 'vasya@mail.com', '89212023334', DEFAULT, DEFAULT);
INSERT INTO users VALUES (DEFAULT, 'Kolya', 'Ivanov', 'kolya@mail.com', '89333023334', DEFAULT, DEFAULT);

INSERT INTO friend_requests (from_user_id, to_user_id) VALUES (1, 2);
INSERT INTO friend_requests (from_user_id, to_user_id) VALUES (1, 3);
INSERT INTO friend_requests (from_user_id, to_user_id) VALUES (2, 2);
INSERT INTO friend_requests (from_user_id, to_user_id) VALUES (2, 3);
INSERT INTO friend_requests (from_user_id, to_user_id) VALUES (1, 1);
INSERT INTO friend_requests (from_user_id, to_user_id) VALUES (3, 3);

-- Написать запрос, удаляющий заявки в друзья самому себе.

DELETE FROM friend_requests 
WHERE from_user_id = to_user_id;


