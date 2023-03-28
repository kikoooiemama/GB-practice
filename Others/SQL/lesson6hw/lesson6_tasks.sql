USE vk_lesson6;
/*
 * Домашнее задание к занятию (вебинару) №6.
*/


/*
 * Таск 1.
 * Проанализировать запросы, которые выполнялись на занятии, определить возможные корректировки и/или улучшения (JOIN пока не применять).
 */

-- Понравилось что на занятии наконец то появились переменные, поэтому я считаю введение переменной того же пользователя с id = 1 очень полезным.
-- Введя такую переменную мы всегда можем к ней обращаться и четко знать что это за пользователь.

SET @request_state_id := (SELECT id FROM friend_requests_types WHERE name = 'accepted');
SELECT @request_state_id;

SET @request_user_id := (SELECT id FROM users WHERE email = 'greenfelder.antwan@example.org');
SELECT @request_user_id;

-- UPDATE 
SELECT concat(first_name, ' ',last_name) AS name
FROM users
WHERE id IN (
	SELECT to_user_id FROM friend_requests WHERE from_user_id = @request_user_id AND request_type = @request_state_id
		UNION 
	SELECT from_user_id FROM friend_requests WHERE to_user_id = @request_user_id AND request_type = @request_state_id
);

-- Таким образом все условия, что использовали id = 1, можно заменить на id = @request_user_id


/*
 * Таск 2
 * Пусть задан некоторый пользователь. 
 * Из всех друзей этого пользователя найдите человека, который больше всех общался с нашим пользователем.
 */

-- У нас задан пользователь. Надо найти человека, который отправил заданному пользователю больше всего сообщений! И при этом найденный человек, должен быть другом пользователя!

SET @request_state_id := (SELECT id FROM friend_requests_types WHERE name = 'accepted');
SELECT @request_state_id;

-- заданный юзер
-- SET @specified_user_id := (SELECT id FROM users WHERE email = 'greenfelder.antwan@example.org');
SET @specified_user_id := (SELECT id FROM users WHERE id = 3);
SELECT @specified_user_id;

SELECT 
  (SELECT first_name FROM users WHERE id = messages.from_user_id) AS first_name,
  (SELECT last_name FROM users WHERE id = messages.from_user_id) AS last_name,
  COUNT(*) AS messages_sent
FROM messages
WHERE to_user_id = @specified_user_id AND from_user_id IN (
	SELECT to_user_id FROM friend_requests WHERE from_user_id = @specified_user_id AND request_type = @request_state_id
		UNION 
	SELECT from_user_id FROM friend_requests WHERE to_user_id = @specified_user_id AND request_type = @request_state_id
)
GROUP BY from_user_id
ORDER BY messages_sent DESC
LIMIT 1;


/*
 * Таск 3
 * Подсчитать общее количество лайков, которые получили 10 самых молодых пользователей.
 */

-- Как я понял, нужно найти все посты 10 самых молодых пользователей и суммировать количество лайков на всех этих постах (т.к. лайки в нашей бд только у постов).

-- Считаем лайки под каждым постом
SELECT user_id,
	(SELECT 
		sum((SELECT count(*) FROM posts_likes WHERE like_type = TRUE AND post_id = posts.id)) FROM posts WHERE user_id = profiles.user_id
	) AS sum_of_likes_for_user,
	TIMESTAMPDIFF(YEAR, birthday, NOW()) AS age
FROM profiles
ORDER BY (NOW() - birthday)
LIMIT 10;

-- Обьединяем с предыдущим, определяем авторов постов и суммируем.
SELECT SUM(sum_of_likes_for_user) AS result 
FROM (SELECT 
		(SELECT 
			sum((SELECT count(*) FROM posts_likes WHERE like_type = TRUE AND post_id = posts.id)) FROM posts WHERE user_id = profiles.user_id
		) AS sum_of_likes_for_user
	FROM profiles
	ORDER BY (NOW() - birthday)
	LIMIT 10)
AS my_result;


/*
 * Таск 4
 * Определить кто больше поставил лайков (всего) - мужчины или женщины?
 */

SELECT 
	COUNT(*) AS number_of_likes,
	(SELECT gender FROM profiles WHERE user_id=posts_likes.user_id) AS gender 
FROM posts_likes WHERE like_type = TRUE
GROUP BY gender;

-- получилось что женщины - 16, мужчины - 5.

/*
 * Таск 5
 * Найти 10 пользователей, которые проявляют наименьшую активность в использовании социальной сети.
 */

-- Под активностью как я понял это суммарное количество всего того, что делал пользователь:
-- 1) количество постов,
-- 2) количество лайков,
-- 3) количество сообщений, отправленных другим пользователям,
-- 4) количество запросов в друзья, отправленных другим другим пользователям,
-- 5) количество выложенных пользователем медиафайлов,
-- 6) количество сообществ, в которых состоит пользователь.

-- промежуточная таблица:
SELECT 
	concat(first_name, ' ',last_name) AS name,
	(SELECT count(*) FROM posts WHERE user_id = users.id) AS number_of_posts,
	(SELECT count(*) FROM posts_likes WHERE user_id = users.id) AS number_of_likes,
	(SELECT count(*) FROM messages WHERE from_user_id = users.id) AS number_of_messages,
	(SELECT count(*) FROM friend_requests WHERE from_user_id = users.id) AS number_of_requests,
	(SELECT count(*) FROM communities_users WHERE user_id = users.id) AS number_of_communities,
	(SELECT count(*) FROM media WHERE user_id = users.id) AS number_of_media
FROM users;


-- результат
SELECT name, number_of_posts + number_of_likes + number_of_messages + number_of_requests + number_of_communities + number_of_media AS sum_all 
FROM(
	SELECT 
		concat(first_name, ' ',last_name) AS name,
		(SELECT count(*) FROM posts WHERE user_id = users.id) AS number_of_posts,
		(SELECT count(*) FROM posts_likes WHERE user_id = users.id) AS number_of_likes,
		(SELECT count(*) FROM messages WHERE from_user_id = users.id) AS number_of_messages,
		(SELECT count(*) FROM friend_requests WHERE from_user_id = users.id) AS number_of_requests,
		(SELECT count(*) FROM communities_users WHERE user_id = users.id) AS number_of_communities,
		(SELECT count(*) FROM media WHERE user_id = users.id) AS number_of_media
	FROM users
) AS subusers_table
ORDER BY sum_all
LIMIT 10;