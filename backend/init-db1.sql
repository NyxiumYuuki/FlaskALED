-- Table: users

CREATE TABLE IF NOT EXISTS users
(
    id integer NOT NULL,
    email character varying(320) NOT NULL,
    login character varying(32) NOT NULL,
    hash_pass character varying(256) NOT NULL,
    is_admin boolean NOT NULL DEFAULT FALSE,
    CONSTRAINT users_pkey PRIMARY KEY(id)
)