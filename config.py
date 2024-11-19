class Config:
    user = "" # User
    password = "" # User password
    host = "" # XAMPP HOST
    port = 0000 # XAMPP PORT
    database = "SistemaDeEmpleados"

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
