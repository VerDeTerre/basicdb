# basicdb #

## About ##

basicdb provides a wrapper around a SQLAlchemy database connection.

## Usage ##

The constructor for the `Database` object accepts any parameters used by a SQLAlchemy `URL`. The following examples show how basicdb may be used:

    from basicdb import Database

    # Create and query an in-memory sqlite database
    sqlite_db = Database(drivername='sqlite', echo=True)
    sqlite_db.execute('select 12345')

    # Create a Postgresql database and perform queries using a session (see
    # SQLALchemy documentation for details)
    pg_db = Database(
        drivername='postgresql',
        host='localhost',
        database='mydb',
    )
    with pg_db.scoped_session() as session:
        session.execute('create table mytable (id integer)')
        session.execute("""
            insert into mytable values
            (1),
            (2),
            (3)
        """)
        results = session.execute('select * from mytable where')
        for result in results:
            print(result)
        session.commit()

## License ##

This software is released under the MIT license. See [LICENSE](LICENSE) for terms.
