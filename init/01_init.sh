#! /bin/bash

set -e

psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" <<-EOSQL
    CREATE SCHEMA IF NOT EXISTS ${POSTGRES_SCHEMA};
    CREATE TABLE IF NOT EXISTS ${POSTGRES_SCHEMA}.${POSTGRES_RAW_DATA_TABLE} (
        id SERIAL PRIMARY KEY,
        time TIMESTAMP,
        latitude REAL,
        longitude REAL,
        elevation INTEGER,
        temperature REAL,
        precip_prob SMALLINT,
        valid_from TIMESTAMP,
        valid_to TIMESTAMP DEFAULT NULL
    );
EOSQL
