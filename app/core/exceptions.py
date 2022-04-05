import logging


class NotFound(Exception):
    """Exception when a database object is not found"""

    def __init__(self, model_class, obj_id):
        msg = f"{model_class.__name__} {obj_id} is not found"
        logging.exception(f"Exception {self.__class__.__name__}: {msg}")
        super().__init__(msg)
