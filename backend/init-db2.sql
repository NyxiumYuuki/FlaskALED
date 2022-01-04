-- Table: logs

CREATE TABLE IF NOT EXISTS logs
(
    id integer NOT NULL,
    date date NOT NULL,
    id_user integer NOT NULL,
    ip character varying(15) NOT NULL,
    "table" character varying(25) NOT NULL,
    action character varying(50) NOT NULL,
    has_succeeded boolean NOT NULL,
    status_code smallint NOT NULL,
    CONSTRAINT logs_pkey PRIMARY KEY(id)
)