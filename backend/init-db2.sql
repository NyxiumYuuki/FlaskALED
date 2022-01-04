-- Table: logs

CREATE TABLE IF NOT EXISTS logs
(
    id serial PRIMARY KEY,
    date timestamp NOT NULL,
    id_user integer,
    ip character varying(15) NOT NULL,
    "table" character varying(25) NOT NULL,
    action character varying(50) NOT NULL,
    message character varying(512) NOT NULL,
    has_succeeded boolean NOT NULL,
    status_code smallint NOT NULL
)