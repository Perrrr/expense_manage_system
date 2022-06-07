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

CREATE TABLE IF NOT EXISTS application (
    id serial primary key,
    public_id uuid not null unique,
    name varchar(80) not null unique,
    description varchar(80),
    avatar_color varchar(80) not null,
    avatar_icon varchar(80) not null,
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
);

CREATE TABLE IF NOT EXISTS organizations (
    id serial primary key,
    public_id uuid not null unique,
    name varchar(80) not null,
    code varchar(80) not null unique,
    avatar_icon varchar(80) not null,
    avatar_color varchar(80) not null,
    image_url varchar(80) not null,
    description varchar(80) not null,
    created_at timestamp default CURRENT_TIMESTAMP,
    updated_at timestamp default CURRENT_TIMESTAMP,
    deleted_at timestamp default NULL
);

CREATE TABLE IF NOT EXISTS organizations_users (
    id serial primary key,
    organization_id integer not null,
    application_id integer not null,
    user_id integer not null,
    created_at timestamp default CURRENT_TIMESTAMP,
    updated_at timestamp default CURRENT_TIMESTAMP,
    deleted_at timestamp default NULL
);


CREATE TABLE IF NOT EXISTS organizations_users_roles (
    id serial primary key,
    organization_id integer not null,
    application_id integer not null,
    user_id integer not null,
    role_id integer not null,
    created_at timestamp default CURRENT_TIMESTAMP,
    updated_at timestamp default CURRENT_TIMESTAMP,
    deleted_at timestamp default NULL
);

CREATE TABLE IF NOT EXISTS roles (
    id serial primary key,
    public_id uuid not null unique,
    application_id integer not null,
    name varchar(80) not null,
    description varchar(80) not null,
    created_at timestamp default CURRENT_TIMESTAMP,
    updated_at timestamp default CURRENT_TIMESTAMP,
    deleted_at timestamp default NULL
);


CREATE TABLE IF NOT EXISTS roles_permissions (
    id serial primary key,
    application_id integer not null,
    role_id integer not null,
    permission_id integer not null,
    created_at timestamp default CURRENT_TIMESTAMP,
    updated_at timestamp default CURRENT_TIMESTAMP,
    deleted_at timestamp default NULL
);

CREATE TABLE IF NOT EXISTS permissions (
    id serial primary key,
    application_id integer not null,
    public_id uuid not null unique,
    name varchar(80) not null,
    method varchar(80) not null,
    description varchar(80) not null,
    created_at timestamp default CURRENT_TIMESTAMP,
    updated_at timestamp default CURRENT_TIMESTAMP,
    deleted_at timestamp default NULL
);

CREATE TABLE IF NOT EXISTS departments (
    id serial primary key,
    public_id uuid not null unique,
    organization_id integer not null,
    name varchar(80) not null,
    description varchar(80) not null,
    created_at timestamp default CURRENT_TIMESTAMP,
    updated_at timestamp default CURRENT_TIMESTAMP,
    deleted_at timestamp default NULL
);

CREATE TABLE IF NOT EXISTS departments_users (
    id serial primary key,
    department_id integer not null,
    user_id integer not null,
    created_at timestamp default CURRENT_TIMESTAMP,
    updated_at timestamp default CURRENT_TIMESTAMP,
    deleted_at timestamp default NULL
);

CREATE TABLE IF NOT EXISTS expense_categories (
    id serial primary key,
    public_id uuid not null unique,
    organization_id integer not null,
    avatar_icon varchar(80) not null,
    avatar_color varchar(80) not null,
    name varchar(80) not null,
    description varchar(80) not null,
    created_at timestamp default CURRENT_TIMESTAMP,
    updated_at timestamp default CURRENT_TIMESTAMP,
    deleted_at timestamp default NULL
);

CREATE TABLE IF NOT EXISTS currencies (
    id serial primary key,
    public_id uuid not null unique,
    organization_id integer not null,
    name varchar(80) not null,
    code varchar(80) not null,
    symbol varchar(80) not null,
    created_at timestamp default CURRENT_TIMESTAMP,
    updated_at timestamp default CURRENT_TIMESTAMP,
    deleted_at timestamp default NULL
);

CREATE TABLE IF NOT EXISTS projects (
    id serial primary key,
    code varchar(80) not null unique,
    public_id uuid not null unique,
    organization_id integer not null,
    avatar_color varchar(80) not null,
    avatar_icon varchar(80) not null,
    name varchar(80) not null,
    description varchar(80) not null,
    status varchar(80) not null,
    created_at timestamp default CURRENT_TIMESTAMP,
    updated_at timestamp default CURRENT_TIMESTAMP,
    deleted_at timestamp default NULL
);

CREATE TABLE IF NOT EXISTS projects_log (
    id serial primary key,
    project_id integer not null,
    user_id integer not null,
    action varchar(255) not null,
    subject varchar(255) not null,
    avatar_icon varchar(80) not null,
    avatar_color varchar(80) not null,
    created_at timestamp default CURRENT_TIMESTAMP,
    updated_at timestamp default CURRENT_TIMESTAMP,
    deleted_at timestamp default NULL
);

CREATE TABLE IF NOT EXISTS project_details (
    id serial primary key,
    project_id integer not null,
    bussiness_purpose text not null,
    duration_start date not null,
    duration_end date not null,
    created_at timestamp default CURRENT_TIMESTAMP,
    updated_at timestamp default CURRENT_TIMESTAMP,
    deleted_at timestamp default NULL
);

CREATE TABLE IF NOT EXISTS expense(
    id serial primary key,
    public_id uuid not null unique,
    expense_category_id integer not null,
    cliam_reimbursement boolean,
    description text not null,
    reference_number varchar(80) not null,
    currency_id integer not null,
    merchant_id integer not null,
    amount numeric not null,
    user_id integer not null,
    created_at timestamp default CURRENT_TIMESTAMP,
    updated_at timestamp default CURRENT_TIMESTAMP,
    deleted_at timestamp default NULL
);

CREATE TABLE IF NOT EXISTS merchant(
    id serial primary key,
    name varchar(80) not null,
    description varchar(80) not null,
    created_at timestamp default CURRENT_TIMESTAMP,
    updated_at timestamp default CURRENT_TIMESTAMP,
    deleted_at timestamp default NULL
);


CREATE TABLE IF NOT EXISTS project_expense(
    id serial primary key,
    project_id integer not null,
    expense_id integer not null,
    created_at timestamp default CURRENT_TIMESTAMP,
    updated_at timestamp default CURRENT_TIMESTAMP,
    deleted_at timestamp default NULL
);