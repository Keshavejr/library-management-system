# lims_portal/routers.py

class ReaderRouter:
    def db_for_read(self, model, **hints):
        # Direct read operations for the Reader model to the second_db
        if model.__name__ == 'Reader':
            return 'second_db'
        return None

    def db_for_write(self, model, **hints):
        # Direct write operations for the Reader model to the second_db
        if model.__name__ == 'Reader':
            return 'second_db'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Allow migrations for the Reader model to the second_db
        if app_label == 'lims_app':  # Ensure this matches your app name
            return db == 'second_db'
        return None
