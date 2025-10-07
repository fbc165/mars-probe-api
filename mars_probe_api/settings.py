import os

from dotenv import load_dotenv

load_dotenv()

# URI do banco de dados
SQLALCHEMY_DATABASE_URI = os.getenv(
    "SQLALCHEMY_DATABASE_URI", "mysql+pymysql://root:iqui1234@localhost:3306/mars_probe"
)  # hardcode pra facilitar o teste local (mas não é o ideal visto que tem dado sensível)
