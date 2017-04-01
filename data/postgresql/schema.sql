/* demo-app-mf-1 */

DROP TABLE IF EXISTS medications;
DROP SEQUENCE IF EXISTS medications_id_seq;

DROP TABLE IF EXISTS locations;
DROP SEQUENCE IF EXISTS locations_id_seq;

DROP TABLE IF EXISTS services;
DROP SEQUENCE IF EXISTS services_id_seq;

DROP TABLE IF EXISTS horses;
DROP SEQUENCE IF EXISTS horses_id_seq;

DROP TABLE IF EXISTS clients;
DROP SEQUENCE IF EXISTS clients_id_seq;

CREATE SEQUENCE clients_id_seq;
CREATE TABLE clients (
    id INTEGER PRIMARY KEY DEFAULT NEXTVAL('clients_id_seq'),
    name VARCHAR(255) DEFAULT '',
    first_name VARCHAR(255) DEFAULT '',
    last_name VARCHAR(255) DEFAULT '',
    city VARCHAR(64) DEFAULT '',
    zipcode VARCHAR(32) DEFAULT '',
    street VARCHAR(255) DEFAULT '',
    additional_address_data VARCHAR(255) DEFAULT '',
    phone VARCHAR(64) DEFAULT '',
    mobphone VARCHAR(64) DEFAULT '',
    fax VARCHAR(64) DEFAULT '',
    email VARCHAR(128) DEFAULT '',
    account_type_1 VARCHAR(64) DEFAULT '',
    owner_1 VARCHAR(255) DEFAULT '',
    account_number_1 VARCHAR(255) DEFAULT '',
    banking_code_1 VARCHAR(255) DEFAULT '',
    account_type_2 VARCHAR(64) DEFAULT '',
    owner_2 VARCHAR(255) DEFAULT '',
    account_number_2 VARCHAR(255) DEFAULT '',
    banking_code_2 VARCHAR(255) DEFAULT '',
    open_stall SMALLINT DEFAULT 0,
    stall SMALLINT DEFAULT 0,
    coupler SMALLINT DEFAULT 0,
    additional_info TEXT,
    vet VARCHAR(255) DEFAULT '',
    smith VARCHAR(255) DEFAULT ''
);

DROP TYPE IF EXISTS sex;
CREATE TYPE sex AS ENUM ('m', 'f');
CREATE SEQUENCE horses_id_seq;
CREATE TABLE horses (
    id INTEGER PRIMARY KEY DEFAULT NEXTVAL('horses_id_seq'),
    client_id INTEGER DEFAULT 0,
    name VARCHAR(255) DEFAULT '',
    online_number VARCHAR(64) DEFAULT '',
    birth_date DATE DEFAULT CURRENT_DATE,
    sex sex DEFAULT 'm',
    color VARCHAR(32) DEFAULT '',
    arrival_date DATE DEFAULT CURRENT_DATE,
    departure_date DATE DEFAULT CURRENT_DATE,
    active SMALLINT DEFAULT 1,
    CONSTRAINT clients_fk FOREIGN KEY (client_id) REFERENCES clients(id) MATCH SIMPLE ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE SEQUENCE medications_id_seq;
CREATE TABLE medications (
    id INTEGER PRIMARY KEY DEFAULT NEXTVAL('medications_id_seq'),
    horse_id INTEGER DEFAULT 0,
    medicament VARCHAR(255) DEFAULT '',
    date DATE DEFAULT CURRENT_DATE,
    note TEXT,
    CONSTRAINT horses_fk FOREIGN KEY (horse_id) REFERENCES horses (id) MATCH SIMPLE ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE SEQUENCE locations_id_seq;
CREATE TABLE locations (
    id INTEGER PRIMARY KEY DEFAULT NEXTVAL('locations_id_seq'),
    horse_id INTEGER DEFAULT 0,
    box_name VARCHAR(255) DEFAULT '',
    box_number VARCHAR(255) DEFAULT '',
    price DECIMAL(8,2) DEFAULT 0.00,
    account_type VARCHAR(64) DEFAULT '',
    contract_number VARCHAR(255) DEFAULT '',
    CONSTRAINT horses_fk FOREIGN KEY (horse_id) REFERENCES horses (id) MATCH SIMPLE ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE SEQUENCE services_id_seq;
CREATE TABLE IF NOT EXISTS services (
    id INTEGER PRIMARY KEY DEFAULT NEXTVAL('services_id_seq'),
    horse_id INTEGER DEFAULT 0,
    active SMALLINT DEFAULT 1,
    service_name VARCHAR(255) DEFAULT '',
    performed_by VARCHAR(255) DEFAULT '',
    start_date DATE DEFAULT CURRENT_DATE,
    end_date DATE DEFAULT CURRENT_DATE,
    price DECIMAL(8,2) DEFAULT 0.00,
    account_type VARCHAR(64) DEFAULT '',
    contract_number VARCHAR(255) DEFAULT '',
    CONSTRAINT horses_fk FOREIGN KEY (horse_id) REFERENCES horses (id) MATCH SIMPLE ON DELETE CASCADE ON UPDATE CASCADE
);
