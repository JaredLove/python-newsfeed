# import the getenv function from the os module
from os import getenv
# import the declarative_base function from the sqlalchemy module
from sqlalchemy.orm.decl_api import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
load_dotenv()

# connect to database using env variable
# The engine variable manages the overall connection to the database.
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
# The Session variable generates temporary connections for performing create, read, update, and delete (CRUD) operations.
Session = sessionmaker(bind=engine)
# The Base class variable helps us map the models to real MySQL tables.
Base = declarative_base()