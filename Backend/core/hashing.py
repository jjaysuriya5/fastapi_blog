from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'],deprecated='auto')


class Hasher:
    @staticmethod
    def verify_password(plain_pwd,hash_pwd):
        return pwd_context.verify(plain_pwd,hash_pwd)

    @staticmethod
    def set_pwd_hash(plain_pwd):
        return pwd_context.hash(plain_pwd)