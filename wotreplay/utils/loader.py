from sqlalchemy.orm import sessionmaker

from wotreplay.utils.engine import create_db_engine


class DataHandler:

    @staticmethod
    def insert(model: object, data: list, db_path: str, db_name: str, db_engine="default"):
        """
        Generic method to insert a data model into sqlite.
        """

        try:
            if db_engine == 'default':
                s = sessionmaker(bind=create_db_engine(path=db_path, db_name=db_name))
            else:
                s = sessionmaker(bind=db_engine)
            session = s()
            session.bulk_insert_mappings(model, data)
            session.commit()
            session.close()

        except:
            # TODO: Create a less generic exception
            raise

    @staticmethod
    def query_file_id(model: object, filename: str, db_path: str, db_name: str, db_engine='default'):
        """
        Get object from database
        """

        if db_engine == 'default':
            s = sessionmaker(bind=create_db_engine(path=db_path, db_name=db_name))
        else:
            s = sessionmaker(bind=db_engine)
        session = s()
        response = session.query(model).filter(model.filename == filename).all()

        try:
            file_id = response[0].id
        except:
            file_id = None
        finally:
            session.commit()
            session.close()

        return file_id

    @staticmethod
    def update(model: object, row_id: int,  data: dict, db_path: str, db_name: str):
        """
        Update values in the database.
        """

        try:

            s = sessionmaker(bind=create_db_engine(path=db_path, db_name=db_name))
            session = s()
            session.query(model).filter(model.id == row_id).update(data)
            session.commit()
            session.close()

        except:
            # TODO: Create a less generic exception
            raise