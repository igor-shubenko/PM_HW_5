## Project description

**Starting services**

Clone repo to local directory and run 

```commandline
docker compose up
```

This command starts services in docker compose: 
1. database
2. crud_server
3. math_server

**Database**

Postgres database with tables: _Users, Events, Bets_.  During containers building database fills with data.
Table _Users_ fills with processed users data from previous homework. Tables _Events and Bets_, also fills some data.

**Crud_server**

Starts on _localhost:8765_

_Crud_server_ provides API for creating, reading, updating and deleting data from database

Endpoints for working with table _Users_

- ***/get/{idn}*** - HTTP method must be GET. _{idn}_ - record _id_ (integer) in table, or 'all' for getting all records from table.
- ***/add*** - HTTP method must be POST. Expect json data in request's body. Fields 'name' and 'time_created' are required.
- ***/change/{idn}*** - HTTP method must be PUT. _{idn}_ - record _id_ (integer) in table. Expect json data in request's body.
- ***/delete/{idn}*** - HTTP method must be DELETE. _{idn}_ - record _id_ (integer) in table , or 'all' for deleting all records from table.

Endpoints for working with table _Bets_

- ***/bet/get/{idn}*** - HTTP method must be GET. _{idn}_ - record _id_ (integer) in table, or 'all' for getting all records from table.
- ***/bet/add*** - HTTP method must be POST. Expect json data in request's body. Fields 'name' and 'time_created' are required.
- ***/bet/change/{idn}*** - HTTP method must be PUT. _{idn}_ - record _id_ (integer) in table. Expect json data in request's body.
- ***/bet/delete/{idn}*** - HTTP method must be DELETE. _{idn}_ - record _id_ (integer) in table , or 'all' for deleting all records from table.

Endpoints for working with table _Events_

- ***/event/get/{idn}*** - HTTP method must be GET. _{idn}_ - record _id_ (integer) in table, or 'all' for getting all records from table.
- ***/event/add*** - HTTP method must be POST. Expect json data in request's body. Fields 'name' and 'time_created' are required.
- ***/event/change/{idn}*** - HTTP method must be PUT. _{idn}_ - record _id_ (integer) in table. Expect json data in request's body.
- ***/event/delete/{idn}*** - HTTP method must be DELETE. _{idn}_ - record _id_ (integer) in table , or 'all' for deleting all records from table.

**Math_server**

Server provides API to get data from another server and make math operations on it: calculate median of users age, 
count amount of unique users names, filter users records by age range. Endpoints for this functional:
- **/median**
- **/unique_names_histogram**
- **/age_range?frm={int}&to={int}** - query parameter ***frm** - left border of age range, ***to*** right border.
