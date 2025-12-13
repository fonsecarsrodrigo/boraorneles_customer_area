from pydantic import BaseModel


class ErrorSchema(BaseModel):
    """ Define how an error is represented
    """
    message: str
