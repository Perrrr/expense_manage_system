CREATE TABLE IF NOT EXISTS users (
    id serial primary key,
    public_id uuid not null unique,
    email varchar(80) not null unique,
    prefix_mobile  varchar(10) not null,
    mobile_number varchar(80) not null unique,
    activated boolean not null default false,
    last_accessed_at timestamp default CURRENT_TIMESTAMP,
    last_login_at timestamp default CURRENT_TIMESTAMP,
    is_online boolean not null default false,
    failed_password_attempts integer not null default 0,
    last_password_reset_at timestamp default CURRENT_TIMESTAMP,
    note varchar(80),
    created_at timestamp default CURRENT_TIMESTAMP,
    updated_at timestamp default CURRENT_TIMESTAMP,
    deleted_at timestamp default NULL
);

CREATE TABLE IF NOT EXISTS profile (
    id serial primary key,
    user_id integer not null,
    first_name varchar(80) not null,
    last_name varchar(80) not null,
    avatar_icon varchar(80) not null,
    avatar_color varchar(80) not null,
    image_url varchar(80) not null,
    created_at timestamp default CURRENT_TIMESTAMP,
    updated_at timestamp default CURRENT_TIMESTAMP,
    deleted_at timestamp default NULL
)