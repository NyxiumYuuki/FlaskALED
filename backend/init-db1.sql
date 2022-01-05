-- Table: users

CREATE TABLE IF NOT EXISTS users
(
    id serial PRIMARY KEY,
    email character varying(320) NOT NULL,
    hash_pass bytea NOT NULL,
    salt bytea NOT NULL,
    is_admin boolean NOT NULL DEFAULT FALSE
)