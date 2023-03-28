DROP DATABASE IF EXISTS vk;

CREATE DATABASE vk;

-- ���������� �� vk
USE vk;

-- ���������� ��� �������
SHOW tables;

/*
 * 1. �������� ������� users.
*/

/*
 * ������� � ��������������.
 * 
 * ��������: ���������� ������� ������ ������������������ �������������.
 * 
 * ��� ���� � �������������: ���� - ���������� ������������� ������������,
 * ���, �������, �������, �����.
 * 
 * ��� ��� � ��� ���� ���� - �� ���������� primary key. � ������ ������ ����������� �������
 * ������ ���� primary key. �� �������� ����� �� �������� � �����������, ��� ��� �������� � �������
 * ���������.
 * ����� ���� ������������� ����������������, ����� ��������� �������� (1,2,3,...)
 * 
 * �����, ����� ������������ ��� ����������� ����������� �������� ��� ��� ������.
 * ����� ��������� � ����������� ������� NOT NULL.
 * 
 * ����� ����� ������� ������ (���-������), � ����� � ������������ ���� ����������� �� �������� 
 * ������ ��� �����������.
 * ��������� � ����������� ������� password_hash DEFAULT NULL.
 * 
 * ����� ����� ������� ���� � ����� ����������� ������������.
 * ��������� ������� created_at, ������� �� ������� �������� ������� ���� � ����� ���������
 * DEFAULT CURRENT_TIMESTAMP.
 * 
 * ����� �� �����, ����� ����� � ������� ������������ ��� ����������� ���� �����������.
 * �� ����, ����� ������������ �� ��� ���������������� ��� ����� ������� �������� ��� ������
 * ��� ��������.
 * ���� ���������� � ����������� ������� UNIQUE,
 * ���� ������� UNIQUE INDEX �� ������ �� �������.
 * 
 * INDEX �������� �� ������� �����. ����� ������� ����� - �� primary key. �� primary key ����� ����
 * ������ ���� � �������.
 * 
 * ����� ������������ ������?
 * ����� �� ����� ���� �����-�� ���������� ��� ��������, ������� ��������� � �������.
 * ��������, �� ���� ��� ������������, ���� ��� email (��� ����� ������ ������ � ��).
 * �� email ���� ������, ������ ����� ���������� �������.
 * 
 * ���������� ������ - ��� �� ����� ������, ������� ������������� �����������, ��� ��� �������� � ������� ���������.
 * 
 * �������������� ��������� ������. ����� �������� - �������� �������� �������.
 * 
 */

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


-- �������� �������, ������� ���� � ����
INSERT INTO users VALUES (DEFAULT, 'Petya', 'Petukhov', 'petya@mail.com', '89212223334', DEFAULT, DEFAULT);
INSERT INTO users VALUES (DEFAULT, 'Vasya', 'Vasilkov', 'vasya@mail.com', '89212023334', DEFAULT, DEFAULT);

-- ��������� �� ���������� �������
SELECT * FROM users;

-- �������� �������
DESCRIBE users;

-- ������ �������� �������
SHOW CREATE TABLE users;

/*
 * 2. �������� ������� � �������� ������������, ����� �� ������� ��� ������ � ������� users
 * 
 * ��������: ���������� ������� ������ ���������� ������������� � ��������� �������.
 * 
 * ����� ������ ���������� ��� �����: ���, �������, ����������, �����, ������.
 * �� ��� ������� ������������ � ��� ������ �����������?
 * 
 * �� ����� ������� ��� � ������� ������ �� ������� users. �� ���� ������ �� �����������
 * ������������ � ������� users.
 *
 * ��������, � ���� id = 1 � ������� users. � ������� profiles �� ������ ������ � user_id = 1
 * � ����� �������������, ��� � ���� ������ ���������� ������ ���������� ����. �� ����, user_id = 1
 * ������� ��� � ���, ��� � ������ ���������� ���������� ������ ��� ������������ �� ������� users � 
 * id = 1 � �� ��� ���� �������.
 * 
 * ��� ����� ����� ��������� ��������� foreign key. �� �����������, ��� ��� ������� user_id ����������
 * id � ������� profiles. � ����� ��, ��� �� ���������� user_id, �������� �� ������������ ������� id � users.
 * CONSTRAINT fk_profiles_users FOREIGN KEY (user_id) REFERENCES users (id)
 * 
 * ������ ������������ ������������� ���� �������. ����� ���� � ������.
 * 
*/
-- 1:1 �����
CREATE TABLE profiles(
	user_id BIGINT UNSIGNED NOT NULL PRIMARY KEY,
	gender ENUM('f', 'm', 'x') NOT NULL,
	birthday DATE NOT NULL,
	photo_id INT UNSIGNED,
	city VARCHAR(130),
	country VARCHAR(130),
	FOREIGN KEY (user_id) REFERENCES users(id) -- ON DELETE CASCADE ON UPDATE CASCADE -- https://dev.mysql.com/doc/refman/8.0/en/create-table-foreign-keys.html 
	
);
 -- �������� ��� ������ ��� ������� photo_id, ����� �������������� media(id)
ALTER TABLE profiles MODIFY COLUMN photo_id BIGINT UNSIGNED;


/*
 * 3. ���������� � �������� ������� profiles, �����������, ������������, ���������
*/
DESCRIBE profiles;
-- ������� ������� � ������� ��������

ALTER TABLE profiles ADD COLUMN passport_number VARCHAR(10);
-- ������� �� ���
ALTER TABLE profiles MODIFY COLUMN passport_number VARCHAR(20);
-- ����������� ��
ALTER TABLE profiles RENAME COLUMN passport_number TO passport;
-- ������� ������ �� �������
ALTER TABLE profiles ADD KEY passport_idx (passport);
-- ������ ������
ALTER TABLE profiles DROP INDEX passport_idx;
-- ������ �������
ALTER TABLE profiles DROP COLUMN passport;

-- �������� �������, ������� ������� ��� ��� ��������� ���� � ����
INSERT INTO profiles VALUES (1, 'm', '1997-12-01', NULL, 'Moscow', 'Russia'); -- ������� ����
INSERT INTO profiles VALUES (2, 'm', '1988-11-02', NULL, 'Moscow', 'Russia'); -- ������� ����

-- �������� �������� ������� ��� ��������������� ������������
-- INSERT INTO profiles VALUES (3, 'm', '1988-11-02', NULL, 'Moscow', 'Russia'); 

SELECT * FROM profiles;
/*
 * 4. �������� ������� � ����������� �������������.
 * 
 * ��������: ���� ���������� ���� ������ ���������.
 * 
 * ���� ����� �������� ��������� ����, ������, �����, � ���� ����� �������� ����� ��������� ����, ������, �����.
 * ��� ����� �� ������ (�������������) � ������ (�������������).
 * 
 * ��� ��� ���������� ������� ��� ���������? ����������� ���������, ���������� ���������, ����� ���������,
 * ���� � ����� �������� ��������� � ���� � ����� ���������� ���������. ����� ����� ������� ���������� � ���,
 * ��������� �� ���������.
 * 
 * ����������� ��������� - ��� ��� ����. ����� �� ������� �� ��������� � ��������� �� ����� ��� � ������� �����������.
 * ����� �� ��� ������� ��� � ������� ����������� � ������� ���������?
 * ���, ��� ���������� ��� �������� � ������� users, �� ��� ������������� �����������.
 * �� ����� ������� ������ �� ����������� ���������, ���� �� ������� users. �� ���� ��� id �� ������� users.
 * 
 * ��������� ����������� ��������� ����� from_user_id. ������, � from_user_id �� ������ 1, id ����.
 * � ���� 1 �� ������ ����� � ������� users, ����� ��� ������ � id = 1, � ������� ��� � ������� ����.
 * 
 * ���������� ��� ����, ������� ���� to_user_id - ������ �� ���������� ��������� �� ������� users.
 * ����� ������� � to_user_id 2, ����� - id ���� �� ������� users.
 * 
 * 
 * ��� ���������� ����������, ����� �� ��� ���� ��������� � ������ �������. �� ����, ����� �� ��� ���-�� ���������
 * ���������������� ������ ��������� �� ���� � ����, ����� �� ���� ������ ��������� ��������� ����, ����������
 * �� ��� ��������� ��� ���������?
 * ��, ����������.
 * ��������� id ��������� � ����-����������� � primary key.
 * 
 * ��� ����� ����������� ��������� � �������� users � ���������� ��������� � �������� users ������� ��� ������
 * FOREIGN KEY, ������� ���������� �� ���� � �� �� ������� users id.
 * ����������� ��������� � ���������� ����� ��� ���������, ��� � �� ��������� ��� ������ ���������. Foreign key
 * ��� ����� �� ������������.
 * 
 * ��� �������� ������ ���� ���������, ������� �������� ����������� ��������� � ���������� id (��������, ����
 * ��� ���������, ������� �������� ���� �� ����� id = 1) �������� ������
 * ��� from_user_id. �� ������������, ��� ��� ����������� ��������� ��� ��������� ����� ������ ���������,
 * �� ����� ����������� � ���������� ������ ������� ��� �����������.
 * 
 * ���������� ��� ���������� ���������, to_user_id, ����� ������ ������ ��� ���������, ������� �� �������.
 * (��������, ��� ���������, ������� ������� ����)
 * 
*/

-- ����� ��������� : ���������
-- 1 : �
-- 1 : 1

CREATE TABLE messages(
	id SERIAL PRIMARY KEY, -- SERIAL = BIGINT UNSIGNED AUTO_INCREMENT NOT NULL
	from_user_id BIGINT UNSIGNED NOT NULL,
	to_user_id BIGINT UNSIGNED NOT NULL,
	txt TEXT NOT NULL,
	is_delivered BOOLEAN DEFAULT FALSE,
	created_at DATETIME NOT NULL DEFAULT NOW(),
	updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT "����� ���������� ������",
	INDEX messages_from_user_id_idx (from_user_id),
	INDEX messages_to_user_id_idx (to_user_id),
	CONSTRAINT fk_messages_from_user_id FOREIGN KEY (from_user_id) REFERENCES users (id),
	CONSTRAINT fk_messages_to_user_id FOREIGN KEY (to_user_id) REFERENCES users (id)
);

DESCRIBE messages;

-- ������� ��� ��������� �� ���� � ����, ���� ��������� �� ���� � ����
INSERT INTO messages VALUES (DEFAULT, 1, 2, 'Hi!', 1, DEFAULT, DEFAULT); -- ��������� �� ���� � ���� ����� 1
INSERT INTO messages VALUES (DEFAULT, 1, 2, 'Vasya!', 1, DEFAULT, DEFAULT); -- ��������� �� ���� � ���� ����� 2
INSERT INTO messages VALUES (DEFAULT, 2, 1, 'Hi, Petya', 1, DEFAULT, DEFAULT); -- ��������� �� ���� � ���� ����� 2

-- ������� �� ���������
SELECT * FROM messages;

/*
 * 5. �������� ������� �������� � ������.
 * 
 * ��������: ���� ����� �������� ���� � ������.
 * 
 * ���� ����� ��������� ������� �� ������ ����, ������, �����, ���� ����� ����� ��������� ������� ����, ������, �����.
 * ��� ����� �� ������ (�������������) � ������ (�������������).
 * 
 * ��� ��� ���������� ������� ��� �������� � ������? ����������� �������, ���������� �������,
 * ������ ������� (������ ��� ��������).
 * 
 * ����������� ��������, ������� �������� ��� �������� ������� messages.
 * �� �������� ������ ������ �� ����������� �������, from_user_id, � ���������� �������, to_user_id.
 * 
 * ��� ���������� ����������, ����� �� ��� ���� ������� �� ������ � ������ �������. 
 * �� ����, ���������� ����������, ����� �� ���� ������� ��������� �������� �� ������ ���� ������������?
 * ���, �� �����. ���� ����� ��������� ���� ������ ���� ������ �� ������. ������������� �� �����.
 * 
 * ������ ��� ����� ��������� ���������������� ���� ����������� ������� � ����������, ����� ���� �� ���
 * ��������� ��� ��������� ������ �� ������ ����.
 * ��� ����� �� ����� ������������ PRIMARY KEY �� ���� ��������, ��� ��� �� � ��� �� �����.
 * PRIMARY KEY ��� ����� �������������, ��� ���� (����, ����), ��� ���� - �����������, ���� - ����������,
 * ����� ����������� � ������� ����� ���� ���.
 * 
 * ���������� ������� messages ��������� foreign keys � �������.
 * 
*/

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


-- ������� ������ �� ������ �� ���� � ����
INSERT INTO friend_requests VALUES (1, 2, 1);

SELECT * FROM friend_requests;

INSERT INTO friend_requests (from_user_id, to_user_id) VALUES (2, 1);
-- INSERT INTO friend_requests (from_user_id, to_user_id) VALUES (3, 1);

/*
 * 6. �������� ������� ���������.
 * 
 * ��������: ���� ������� ����������.
 * 
 * ���� ����� ������� ����� ���������, ������ � ���������� ����� ���� ������ ���� ���������.
 * ����� �� ������ (������������) � ������ (�����������).
 * 
 * ��� ��� ���������� ������� ��� ����������? ��� ����, ��������, ��������, ��������� ����������.
 * 
 * ��������� ���������� - ��� ������������. ������, �� ����������� �����, �� ����� ������� ������ �� ������������
 * �� ������� users. �� ���� id ������������ �� ������� users. ����� �� ������� � foreign key.
 * ���������� ���������, ��� ��� ����� �� ������ � ������ ������ � ������������� foreign key ���������
 * �� ������� ������, �� ���� ���������� � ������ ������.
 * 
 * ��������� ����� ������ �� ��������� ���������� (admin_id) ��� �������� ������ ���� ���������, � ������� ���������
 * ������������ � ���������� id.
 * 
*/
CREATE TABLE communities(
	id SERIAL PRIMARY KEY,
	name VARCHAR(150) NOT NULL,
	description VARCHAR(255),
	admin_id BIGINT UNSIGNED NOT NULL,
	KEY (admin_id),
	FOREIGN KEY (admin_id) REFERENCES users(id)
);

-- ������� ���������� � ���������� �����
INSERT INTO communities VALUES (DEFAULT, 'Number1', 'I am number one', 1);
INSERT INTO communities VALUES (DEFAULT, 'Number2', 'I am number two', 1);


SELECT * FROM communities;
/*
 * 7. �������� ������� ��� �������� ���������� ��� ���� ���������� ���� ���������.
 * 
 * ��������: ���� ������� � ���������� Number1.
 * 
 * ���� ����� �������� �� ����� ������ ���������, ��� ���� � ����� ���������� ����� ���� ����� ����������.
 * ����� �� ������ � ������.
 * 
 * ��� ��� ���������� �������? ������������, ����������, � ������� �� �������, ���� ���������� � ����������.
 * 
 * ��� ��� ���� ����� �������� � ���������� Number1 ������ ���� ���, ���������� ������������� ������ ��� �� ����� (id),
 * ���������� ������������ ������� friend_requests ��� ����� � ������� �� ��������.
*/
-- ������������ : ����������
-- � : 1
-- 1 : �

-- ������� ����� ������������� � ���������
CREATE TABLE communities_users(
	community_id BIGINT UNSIGNED NOT NULL,
	user_id BIGINT UNSIGNED NOT NULL,
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY(community_id, user_id),
	KEY (community_id),
	KEY (user_id),
	FOREIGN KEY (community_id) REFERENCES communities (id),
	FOREIGN KEY (user_id) REFERENCES users(id)
);


-- ������� ������ ���� ���� �������� ���������� Number 1
INSERT INTO communities_users VALUES (1, 2, DEFAULT);

SELECT * FROM communities_users;
/*
 * 8. �������� ������� ��� �������� ����� ����� ������, ������� ����� ����������.
 * 
 * � �������-�������� ������ �� �������� ������ �� ������ �������.
 * � �������-�������� ������ �������� ������ ���� � ��������, � ������ ������ ���� ����
 * �����-����� � �������� �����-�����.
 * 
 * ����������� �������� ����� ������� ��� ������ �������, �����, ...
*/
CREATE TABLE media_types(
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(50) NOT NULL UNIQUE
);

-- ������� ���� � �������
INSERT INTO media_types VALUES (DEFAULT, '�����������');
INSERT INTO media_types VALUES (DEFAULT, '������');
INSERT INTO media_types VALUES (DEFAULT, '��������');

SELECT * FROM media_types;

/*
 * 9. �������� ������� ���� �����������.
 * 
 * ��������: ���� ��������� ����������.
 * 
 * ���� ����� �������� ����� ��������� �����������, ������ � ���������� ����� ���� ������ ���� ����� 
 * (���, ��� ��� �������).
 * ����� �� ������ (������������) � ������ (�����������).
 * 
 * ��� ��� ���������� ������� ��� ����������? ��� ����, ���������, ���, ��������, ������, ���� ����������.
 * 
 * ������ �� ��������� (������������) ������� �� �������� � ����� ���������� ���������, ��������� ������ ���
 * �������� ������ ����������� ������������ � foreign key.
 * 
 * ����� ���������� ���-�� ������� ��� �����-�����. ����� ������� �������� ���� ����������, ��������, "�����������",
 * "������", "��������". ������, �������� ����� ����������� � ��� ��� �������� � ����� �������� media_types � ��� �����
 * ������������ ������. ��� �� ����� ������� �� �������� ����, � ������ �� �������� ���� � �������� (�� ���� id ���� 
 * ���������� �� ������� media_types).
 * 
 * � ������� ���� ���������� ����� ���� ��������� ����������� (��� "�����������" ����� ���� � ��������� �����������),
 * ������ � ���������� ����� ���� ������ ���� ��� (����������1 ����� ������ ���� ��� - "�����������").
 * ��� ��� ����� �� ������ (����) � ������ (�����������).
 * 
 * ������� ������� media_types_id, ��� ������ id ���� �� media_types. ������� foreign key �� media_types_id
 * � media_types (id). ������ �� �������, ��� ��� ����� ����������� ����� ����, � ������ ����� ����� ��������
 * �� ����� ������� � ����� �������������� ����������. 
 * 
 * ��� � ������ ������� � ��� ���������� ��� ������ ����� �� ������ � ������, ������� �� ������� ����� �����.
*/
CREATE TABLE media (
	id SERIAL PRIMARY KEY,
	user_id BIGINT UNSIGNED NOT NULL,
	media_types_id INT UNSIGNED NOT NULL,
	file_name VARCHAR(255) COMMENT '/files/folder/img.png',
	file_size BIGINT UNSIGNED,
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	KEY (media_types_id),
	KEY (user_id),
	FOREIGN KEY (media_types_id) REFERENCES media_types(id),
	FOREIGN KEY (user_id) REFERENCES users(id)
);

-- ������� ��� �����������, ������� ������� ����
INSERT INTO media VALUES (DEFAULT, 1, 1, 'im.jpg', 100, DEFAULT);
INSERT INTO media VALUES (DEFAULT, 1, 1, 'im1.png', 78, DEFAULT);
-- ������� ��������, ������� ������� ����
INSERT INTO media VALUES (DEFAULT, 2, 3, 'doc.docx', 1024, DEFAULT);

SELECT * FROM media;

DESCRIBE media;

-- -------------------------------------------------------------------------------------------------------------------------
/*
 * �������� �������.
 * 
 * ������ ��������� ������� ��� ������ �� ����������� ��� ������ ��������� (�������) users, media, posts. 
 * ������� �� ������ �������, ��������� ���� ������ ����� ������� ������ ���� ��������� ������� � ������� ����� ������������.
 * 
 * ����� ����� ���� ���-�� ������� �������, �� ���� �� ������� ���.
 * ����� ���� ���� ���������� ��� �������: posts, media, users. �� � �� ������� ��� �� ������� � ������� REFERENCE.
 * ������� �� ��� ����������� ��� ����� ���� ���������� ������ ��� ������.
 * 
 * ����������� ��� ��������� ������� users, media. 
 * ������ ����� ������� likes_for_media, likes_for_users, likes_for_posts � posts.
 */
-- -------------------------------------------------------------------------------------------------------------------------

/**
 * ������� ������ �� ���� �����������. 
 */
CREATE TABLE likes_for_media (
	from_user_id BIGINT UNSIGNED NOT NULL,
	to_media_id BIGINT UNSIGNED NOT NULL,
	PRIMARY KEY(from_user_id, to_media_id),
	created_at DATETIME NOT NULL DEFAULT NOW(),
	INDEX like_from_user_id_idx_for_media (from_user_id),
	INDEX like_to_media_id_idx_for_media (to_media_id),
	CONSTRAINT fk_media_like_from_user_id FOREIGN KEY (from_user_id) REFERENCES users (id),
	CONSTRAINT fk_media_like_to_media_id FOREIGN KEY (to_media_id) REFERENCES media (id)
);

INSERT INTO likes_for_media VALUES (1, 1, DEFAULT);
INSERT INTO likes_for_media VALUES (1, 2, DEFAULT);

/**
 * ������� ������ �� ���� �������������. 
 */
CREATE TABLE likes_for_users (
	from_user_id BIGINT UNSIGNED NOT NULL,
	to_user_id BIGINT UNSIGNED NOT NULL,
	PRIMARY KEY(from_user_id, to_user_id),
	created_at DATETIME NOT NULL DEFAULT NOW(),
	INDEX like_from_user_id_idx_for_users (from_user_id),
	INDEX like_to_user_id_idx_for_users (to_user_id),
	CONSTRAINT fk_users_like_from_user_id FOREIGN KEY (from_user_id) REFERENCES users (id),
	CONSTRAINT fk_users_like_to_user_id FOREIGN KEY (to_user_id) REFERENCES users (id)
);

INSERT INTO likes_for_users VALUES (1, 1, DEFAULT);
INSERT INTO likes_for_users VALUES (1, 2, DEFAULT);
INSERT INTO likes_for_users VALUES (2, 1, DEFAULT);

/**
 * ������� ���� ������ ���� �������������.
 * 
 * ���� ����� ���� id. � ���� ���� to_user_id, �� ��������� �������� �������� ����. ���� ����� ����� from_user_id.
 * ����� � ����� ���� ����� ��������� � ���� ���������. ���� ���������� ���, �� ������ �� NULL.
 */
CREATE TABLE posts (
	id SERIAL PRIMARY KEY,
	from_user_id BIGINT UNSIGNED NOT NULL,
	to_user_id BIGINT UNSIGNED NOT NULL,
	txt TEXT NOT NULL,
	media_id BIGINT UNSIGNED DEFAULT NULL,
	created_at DATETIME NOT NULL DEFAULT NOW(),
	updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT "����� ���������� �����",
	INDEX posts_from_user_id_idx (from_user_id),
	INDEX posts_to_user_id_idx (to_user_id),
	INDEX posts_media_id_idx (media_id),
	FOREIGN KEY (from_user_id) REFERENCES users(id),
	FOREIGN KEY (to_user_id) REFERENCES users(id),
	FOREIGN KEY (media_id) REFERENCES media(id)
);

INSERT INTO posts VALUES (DEFAULT, 1, 1, '���� ��������� ���� ������ �����!', DEFAULT, DEFAULT, DEFAULT);
INSERT INTO posts VALUES (DEFAULT, 1, 2, '����, ���� �����!', 1, DEFAULT, DEFAULT);

/**
 * ������� ������ �� ���� ������ ���� �������������. 
 */
CREATE TABLE likes_for_posts (
	from_user_id BIGINT UNSIGNED NOT NULL,
	to_post_id BIGINT UNSIGNED NOT NULL,
	PRIMARY KEY(from_user_id, to_post_id),
	created_at DATETIME NOT NULL DEFAULT NOW(),
	INDEX like_from_user_id_idx_for_posts (from_user_id),
	INDEX like_to_post_id_idx_for_posts (to_post_id),
	CONSTRAINT fk_posts_like_from_user_id FOREIGN KEY (from_user_id) REFERENCES users (id),
	CONSTRAINT fk_posts_like_to_media_id FOREIGN KEY (to_post_id) REFERENCES posts (id)
);

INSERT INTO likes_for_posts VALUES (1, 1, DEFAULT);
INSERT INTO likes_for_posts VALUES (1, 2, DEFAULT);