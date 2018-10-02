[![Wisdomic Panda](https://github.com/robagwe/wisdomic-panda/blob/master/imgs/panda.png)](http://www.rohanbagwe.com/)  **Wisdomic Panda**
> *Hold the Vision, Trust the Process.*

# SQLAlchemy ORM guide for EOD Framework Class mapping for Celery-Batch Processing! 
*... basic example for SQLAlchemy Object Relational Mapper to associate user-defined Python classes with database tables.*

###### Why ORM?

ORMs provide a high-level abstraction upon a relational database that allows a developer to write Python code instead of SQL to create, read, update and delete data and schemas in their database.

         # Oracle SQL
         SELECT * FROM USERS WHERE dept_code='DEVOPS';
         
         # Obtain everyone in the department code DEVOPS and assign to users variable.
         users = Users.objects.filter(zip_code=94107)


> There are numerous ORM implementations written in Python, which includes:
    
 -  SQLAlchemy
 -  Peewee
 -  The Django ORM
 -  PonyORM
 -  SQLObject

**(Similarly, we have Hibernate, Eclipselink, Enterprise JavaBeans Entity Beans, Castor in java.)**

#### :construction: Setting up local environment:

> *pip install sqlalchemy*

        import sqlalchemy
        sqlalchemy.__version__
        1.2.7 

> *pip install flask*

#### :construction: Run [seed.sql](https://github.com/robagwe/rough-book-flask-sqlalchemy-sqlite3/blob/master/seed.sql) for table creation in Database:

> *sqlite3 test_users.db < seed.sql*

###### Verify
         
         #test_users.db will be created in your directory!
         
         sqlite3 test_users.db
         SQLite version 3.23.1 2018-04-10 17:39:29
         Enter ".help" for usage hints.
         
         sqlite> 

#### :construction: Get hands on: [Kick-off](https://github.com/robagwe/rough-book-flask-sqlalchemy-sqlite3/blob/master/user_model.py)

> *python -m DIRECTORY.Main.py*

### :coffee: Ingredients:

- sqlalchemy
- flask
- sqlite3
- Ubuntu 16.4 LTS

#### :heavy_exclamation_mark: I run on Mac OS/Ubuntu so you might have to slightly modify the code to make it work in your env.

:email: [Drop In!!](https://www.rohanbagwe.com) Seriously, it'd be great to discuss Technology.
