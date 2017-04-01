#!/bin/sh

PASSWORD='demo-app-mf-1'

PGPASSWORD=$PASSWORD psql -h localhost -U demo-app-mf-1 demo-app-mf-1 < ~/projects/demo-app-mf-1/data/postgresql/schema.sql
PGPASSWORD=$PASSWORD psql -h localhost -U demo-app-mf-1 demo-app-mf-1 < ~/projects/demo-app-mf-1/data/postgresql/triggers.sql
PGPASSWORD=$PASSWORD psql -h localhost -U demo-app-mf-1 demo-app-mf-1 < ~/projects/demo-app-mf-1/data/postgresql/data.sql
