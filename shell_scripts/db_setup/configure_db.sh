sleep 20s
echo "localhost:5432:postgres:postgres:test@123" > ~/.pgpass
chmod 0600 ~/.pgpass #file permission settings
psql -h localhost -p 5432 -d postgres -U postgres <<EOF
-- Your SQL queries go here
CREATE ROLE user1 WITH LOGIN SUPERUSER PASSWORD '1234';
CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE embeddingStore (id bigserial primary key, name text,embedding vector(512));
-- Additional queries...
EOF
