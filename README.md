
1. Clone this repo

2. Install virtualenv and activate

```
    $ virtualenv venv
    $ source venv/bin/activate
```

3. Install the dependencies

```
$ pip install -r requirements.txt
```

4. Setup env variables
    - $ export FLASK_APP=run.py
    - $ export FLASK_DEBUG=1
    - $ export FLASK_ENV=development
    - $ export SECRET_KEY=`<SECRET KEY>`
    - $ export DATABASE_URL=`<URI>`
    - $ export DATABASE_TEST_URL=`<URI>`

    ```
        export DATABASE_URL="postgres://username:password@localhost/flasky"
        export DATABASE_TEST_URL="postgres://username:password@localhost/flasky_test"

    ```

6. Run the basic tests
```
    pytest
```

7. Inspiration

    [creating-user-database-and-adding-access-on-postgresql](https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e)

    [how-to-list-databases-and-tables-in-postgresql](https://chartio.com/resources/tutorials/how-to-list-databases-and-tables-in-postgresql-using-psql/)

    [create-a-web-application-with-python-flask-postgresql-and-deploy-on-heroku](https://medium.com/@dushan14/create-a-web-application-with-python-flask-postgresql-and-deploy-on-heroku-243d548335cc)
    
    [show-data-in-a-table-by-using-psql-command-line-interface](https://stackoverflow.com/questions/26040493/how-to-show-data-in-a-table-by-using-psql-command-line-interface)
