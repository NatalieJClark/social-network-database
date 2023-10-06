# Two Tables Design Recipe Template


## 1. Extract nouns from the user stories or specification

```
As a social network user,
So I can have my information registered,
I'd like to have a user account with my email address.

As a social network user,
So I can have my information registered,
I'd like to have a user account with my username.

As a social network user,
So I can write on my timeline,
I'd like to create posts associated with my user account.

As a social network user,
So I can write on my timeline,
I'd like each of my posts to have a title and a content.

As a social network user,
So I can know who reads my posts,
I'd like each of my posts to have a number of views.
```

```
Nouns:
user account, email address, username
posts, title, content, number of views
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties                 |
| --------------------- | -------------------------- |
| user_account          | email, username            |
| post                  | title, content, total_views|

1. Name of the first table (always plural): `user_accounts` 

    Column names: `email`, `username`

2. Name of the second table (always plural): `posts` 

    Column names: `title`, `content`, `total_views`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
Table: user_accounts
email: text
username: text

Table: posts
title: text
content: text
total_views: int

```

## 4. Decide on The Tables Relationship

Most of the time, you'll be using a **one-to-many** relationship, and will need a **foreign key** on one of the two tables.

To decide on which one, answer these two questions:

1. Can one [TABLE ONE] have many [TABLE TWO]? (Yes/No)
2. Can one [TABLE TWO] have many [TABLE ONE]? (Yes/No)

You'll then be able to say that:

1. **[A] has many [B]**
2. And on the other side, **[B] belongs to [A]**
3. In that case, the foreign key is in the table [B]

Replace the relevant bits in this example with your own:

```
# EXAMPLE

1. Can one user_account have many posts? YES
2. Can one post have many user_accounts? NO

-> Therefore,
-> A user_account HAS MANY posts
-> A post BELONGS TO a user_account

-> Therefore, the foreign key is on the posts table (user_account_id)
```

*If you can answer YES to the two questions, you'll probably have to implement a Many-to-Many relationship, which is more complex and needs a third table (called a join table).*

## 5. Write the SQL

```sql
-- EXAMPLE
-- file: social_network.sql

-- Replace the table name, columm names and types.

-- Create the table without the foreign key first.
CREATE TABLE user_accounts (
  id SERIAL PRIMARY KEY,
  email text,
  username text
);

-- Then the table with the foreign key second.
CREATE TABLE  (
  id SERIAL PRIMARY KEY,
  title text,
  content text,
  total_views int,
  user_account_id int,
  constraint fk_user_account foreign key(user_account_id)
    references user_accounts(id)
    on delete cascade
);

```

## 6. Create the tables

```bash
psql -h 127.0.0.1 social_network < social_network.sql
```

