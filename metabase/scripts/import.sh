#!/bin/bash

metabase-import \
  --export-dir "./metabase" \
  --db-map "./db_map.json"
