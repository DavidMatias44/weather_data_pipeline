#!/bin/bash

set -e

metabase-export \
  --export-dir "./metabase" \
  --include-dashboards
