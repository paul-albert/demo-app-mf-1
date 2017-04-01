# demo-app-mf-1

## Prepare steps:

_(environment: Linux / Nginx / PostgreSQL 9.x / Python 3.4+ / Flask / AngularJS 1.6+)_

### Database (PostgreSQL)

* Create:

`sudo -u postgres psql`

`CREATE ROLE "demo-app-mf-1" WITH PASSWORD 'demo-app-mf-1' LOGIN;`

`CREATE DATABASE "demo-app-mf-1" OWNER "demo-app-mf-1";`

`psql -h localhost -U demo-app-mf-1 demo-app-mf-1` (for check of access only)

* _(Optional step - for VBox/VMWare only)_

`sudo nano /etc/postgresql/9.4/main/pg_hba.conf`

and add:

`host    demo-app-mf-1   demo-app-mf-1   10.0.2.2/0              md5`

* Import schema and data to database:

`psql -h localhost -U demo-app-mf-1 demo-app-mf-1 < ~/projects/demo-app-mf-1/data/postgresql/schema.sql`

`psql -h localhost -U demo-app-mf-1 demo-app-mf-1 < ~/projects/demo-app-mf-1/data/postgresql/triggers.sql`

`psql -h localhost -U demo-app-mf-1 demo-app-mf-1 < ~/projects/demo-app-mf-1/data/postgresql/data.sql`

or:

`~/projects/demo-app-mf-1/data/initdb.sh`

### Back-end's part (Python/Flask)

* `cd ~/projects/demo-app-mf-1/backend/`

* Check version of Python:

`python3 -V` _(outputs like as Python 3.4.2)_

* Check version of Python:

`virtualenv --version` _(outputs like as 15.1.0)_

* Create new virtual environment:

`virtualenv -p python3 env`

* Activate the created virtual environment:

`source env/bin/activate`

* Check again version of Python:

`python -V` _(outputs like as Python 3.4.2)_

* Install all dependencies:

`pip install -r requirements.txt`

* Check and edit [configuration file](backend/app/config.py) if needing

* Run our new RESTful web-service:

`python ./app/main.py` (here you can use "http://127.0.0.1:5001/"; CTRL+C - for break the service)

* `deactivate` _(optional step, for virtual environment's turn off only)_

### Web-server (Nginx)

* Nginx's configuration sample - see in `configuration/nginx.conf`

### Front-end's part (HTML/CSS/Bootstrap 3.x/AngularJS 1.6+)

_(This part is not yet implemented completely...)_

## Running:

* Open in browser link "http://demo-app-mf-1.dev"
