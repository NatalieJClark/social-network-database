-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users cascade;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    email TEXT
);

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title TEXT,
    content TEXT,
    total_views INTEGER,
    user_id INTEGER,
    constraint fk_user foreign key(user_id) references users(id) on delete cascade
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (username, email) VALUES ('natalie', 'natalie@email.com');
INSERT INTO users (username, email) VALUES ('jayne', 'jayne@email.com');
INSERT INTO users (username, email) VALUES ('matt', 'matt@email.com');

INSERT INTO posts (title, content, total_views, user_id) VALUES ('Title 1', 'Content 1', 576, 1);
INSERT INTO posts (title, content, total_views, user_id) VALUES ('Title 2', 'Content 2', 89, 2);
INSERT INTO posts (title, content, total_views, user_id) VALUES ('Title 3', 'Content 3', 123, 3);
