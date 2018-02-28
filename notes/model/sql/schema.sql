drop table if exists notes;
create table notes (
    id integer primary key autoincrement,
    note text not null,
    publish_date text not null,
    visits integer not null,
    user_id integer not null
);

drop table if exists users;
create table users (
    user_id integer primary key autoincrement,
    user_name text not null,
    passwd text not null
);

