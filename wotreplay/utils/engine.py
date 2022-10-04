from sqlalchemy import create_engine


def create_db_engine(path: str, db_name: str):
    """
    Creates a sqlite database to be populated by the ORM
    """
    engine = create_engine('sqlite:///{}/{}.db'.format(path, db_name))

    return engine
