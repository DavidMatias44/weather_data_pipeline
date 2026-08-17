#! /bin/bash

set -e

psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" <<-EOSQL
    CREATE SCHEMA IF NOT EXISTS ${DB_SCHEMA};
    CREATE TABLE IF NOT EXISTS ${DB_SCHEMA}.${DB_RAW_DATA_TABLE} (
        time TIMESTAMP PRIMARY KEY,
        latitude REAL,
        longitude REAL,
        elevation INTEGER,
        temperature REAL,
        precip_prob SMALLINT,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP(0)
    );
EOSQL
