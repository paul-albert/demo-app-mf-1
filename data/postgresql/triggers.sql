/* demo-app-mf-1 */

CREATE OR REPLACE FUNCTION set_client_name() RETURNS trigger AS
$$
BEGIN
    NEW.name = COALESCE(NEW.first_name, '') || ' ' || COALESCE(NEW.last_name, '');
    RETURN NEW;
END;
$$
LANGUAGE plpgsql;

CREATE TRIGGER set_client_name BEFORE INSERT OR UPDATE ON clients
FOR EACH ROW EXECUTE PROCEDURE set_client_name();
