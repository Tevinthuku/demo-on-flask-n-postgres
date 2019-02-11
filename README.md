export DATABASE_URL="postgres://tev:8279@localhost/flasky"

export DATABASE_TEST_URL="postgres://tev:8279@localhost/flasky_test"

https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e

https://chartio.com/resources/tutorials/how-to-list-databases-and-tables-in-postgresql-using-psql/

https://medium.com/@dushan14/create-a-web-application-with-python-flask-postgresql-and-deploy-on-heroku-243d548335cc

3. Install the dependencies

```
$ pip install -r requirements.txt
```

4. Initialize environment variables

```
$ export SECRET_KEY=<SECRET KEY>
$ export DATABASE_URL=<URI>
$ export DATABASE_TEST_URL=<URI>
```

4. Setup env variables
    - $ export FLASK_APP=run.py
    - $ export FLASK_DEBUG=1
    - $ export FLASK_ENV=development
