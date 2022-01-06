-- Table: users

CREATE TABLE IF NOT EXISTS users
(
    id serial PRIMARY KEY,
    email character varying(320) NOT NULL,
    nickname character varying(50) NOT NULL,
    hash_pass bytea NOT NULL,
    salt bytea NOT NULL,
    is_admin boolean NOT NULL DEFAULT FALSE
);

INSERT INTO users VALUES(0,'admin@admin.admin','Admin',decode('e5ed79b503704ed20a1d250770db68182118de7fe0236db9bbfb0dd9684087d6', 'hex'),decode('7012f69f1ac7c23c5dca498c30fa94527b507cc9e40fab9bae284d1465a37724', 'hex'),TRUE);