-- Sentencias previas a la conexion con Django
ALTER ROLE userdjango SET client_encoding TO 'utf8';
ALTER ROLE userdjango SET default_transaction_isolation TO 'read committed';
ALTER ROLE userdjango SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE db_final_orm TO userdjango;
GRANT ALL PRIVILEGES ON SCHEMA public TO userdjango;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO userdjango;


SELECT * FROM laboratorio_producto;