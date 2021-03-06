import hashlib

from thirdparty.blake import blake
from thirdparty.md2 import md2_hash
from passlib.hash import bcrypt
from passlib.hash import oracle11
from passlib.hash import scrypt

from thirdparty.tiger import tiger


def mysql_hash(string, salt=None, front=False, back=False):
    """
      Create a hash identical to the one that MySQL uses

      > :param string: string to turn into MySQL hash
      > :param salt: for all occurrences, given salt to be provided
      > :param front: for all occurrences, salt goes on the front if True
      > :param back: for all occurrences, salt goes on the back if True
      > :return: a MySQL hash

      Example:
        >>> mysql_hash("test")
        *94BDCEBE19083CE2A1F959FD02F964C7AF4CFC29
    """
    if salt is not None and front is True and not back:
        obj1 = hashlib.sha1(salt + string).digest()
        obj2 = hashlib.sha1(obj1).hexdigest()
    elif salt is not None and back is True and not front:
        obj1 = hashlib.sha1(string + salt).digest()
        obj2 = hashlib.sha1(obj1).hexdigest()
    else:
        obj1 = hashlib.sha1(string).digest()
        obj2 = hashlib.sha1(obj1).hexdigest()
    return "*{}".format(obj2.upper())


def oracle_hash(string, salt=None, front=False, back=False):
    raise NotImplementedError("Oracle hashes are not implemented yet")
    if salt is not None and front is True and not back:
        obj = oracle11.hash(salt + string)
    elif salt is not None and back is True and not front:
        obj = oracle11.hash(string + salt)
    else:
        obj = oracle11.hash(string)
    return obj


def blowfish_hash(string, salt=None, front=False, back=False):
    """
      Create a Blowfish hash using passlib

      > :param string: string to generate a Blowfish hash from
      > :return: Blowfish hash

      Example:
        >>> blowfish_hash("test")
        $2b$12$9.uNMtjZD./9xGMD3QLHpen6WBSs8TmjmYSl5EGs4OS/zsUwmJivq
    """
    if salt is not None and front is True and not back:
        return bcrypt.hash(salt + string)
    elif salt is not None and back is True and not front:
        return bcrypt.hash(string + salt)
    else:
        return bcrypt.hash(string)


def scrypt_hash(string, salt=None, front=False, back=False):
    raise NotImplementedError("Scrypt hashes are not implemented yet")
    if salt is not None and front is True and not back:
        obj = scrypt.hash(string)


def ripemd160(string, salt=None, front=False, back=False):
    """
      Create a RipeMD160 hash from a given string

      > :param string: string to be hashed
      > :return: a hashed string with or without salt

      Example:
        >>> ripemd160("test")
        5e52fee47e6b070565f74372468cdc699de89107
    """
    obj = hashlib.new("ripemd160")
    if salt is not None and front is True and not back:
        obj.update(salt + string)
    elif salt is not None and back is True and not front:
        obj.update(string + salt)
    else:
        obj.update(string)
    return obj.hexdigest()


def blake224(string, salt=None, front=False, back=False):
    """
      Create a Blake224 hash from given string

      > :param string: string to be hashed
      > :return: a blake224 hash

      Example:
        >>> blake224("test")
        e9543bfe985642bc30d41903161b2252a014deca64a9af27fc0c111f
    """
    obj = blake.BLAKE(224)
    if salt is not None and front is True and not back:
        digest = obj.hexdigest(salt + string)
    elif salt is not None and back is True and not front:
        digest = obj.hexdigest(string + salt)
    else:
        digest = obj.hexdigest(string)
    return digest


def blake256(string, salt=None, front=False, back=False):
    """
      Create a Blake256 hash from a given string

      > :param string: string to be hashed
      > :return: a blake256 hash

      Example:
        >>> blake256("test")
        dc1ef7d25c8658590f3498d15baa87834f39a6208ddcb28fdfb7cc3179b8bf8f
    """
    obj = blake.BLAKE(256)
    if salt is not None and front is True and not back:
        digest = obj.hexdigest(salt + string)
    elif salt is not None and back is True and not front:
        digest = obj.hexdigest(string + salt)
    else:
        digest = obj.hexdigest(string)
    return digest


def blake384(string, salt=None, front=False, back=False):
    """
      Create a bBlake384 hash from a given string

      > :param string: string to be hashed
      > :return: a blake384 hash

      Example:
        >>> blake384("test")
        97c456fb92567f27324497d1d41a8427eed77a1f3a1161faf49e40ebae44a7d1e2f9e8bdf7bc193ae9e37bebf50ece76
    """
    obj = blake.BLAKE(384)
    if salt is not None and front is True and not back:
        digest = obj.hexdigest(salt + string)
    elif salt is not None and back is True and not front:
        digest = obj.hexdigest(string + salt)
    else:
        digest = obj.hexdigest(string)
    return digest


def blake512(string, salt=None, front=False, back=False):
    """
      Create a Blake512 hash from a given string

      > :param string: string to ne hashed
      > :return: a blake512 hash

      Example:
        >>> blake512("test")
        042d11c84ee88718f4451b05beb21c0751e243ed15491a927fef891ba0ba17bbe0d2f5286639cebabe86d876e4064821cd9d5764faba5bbd3d63d02275c0593e
    """
    obj = blake.BLAKE(512)
    if salt is not None and front is True and not back:
        digest = obj.hexdigest(salt + string)
    elif salt is not None and back is True and not front:
        digest = obj.hexdigest(string + salt)
    else:
        digest = obj.hexdigest(string)
    return digest


def md2(string, salt=None, front=False, back=False):
    """
      Create an MD2 hash from a given string

      > :param string: string to be hashed
      > :return: an MD2 hash

      Example:
        >>> md2("test")
        dd34716876364a02d0195e2fb9ae2d1b
    """
    if salt is not None and front is True and not back:
        obj = md2_hash.md2h(salt + string)
    elif salt is not None and back is True and not front:
        obj = md2_hash.md2h(string + salt)
    else:
        obj = md2_hash.md2h(string)
    return obj


def md4(string, salt=None, front=False, back=False):
    """
    Create an MD4 hash from a given string

      > :param string: string to hash
      > :return: a MD4 hash

      Example:
        >>> md4("test")
        db346d691d7acc4dc2625db19f9e3f52
    """
    obj = hashlib.new("md4")
    if salt is not None and front is True and not back:
        obj.update(salt + string)
    elif salt is not None and back is True and not front:
        obj.update(string + salt)
    else:
        obj.update(string)
    return obj.hexdigest()


def md5(string, salt=None, front=False, back=False):
    """
      Create an MD5 hash from a given string

      > :param string: string to be hashed
      > :return: a MD5 hash

      Example:
        >>> md5("test")
        098f6bcd4621d373cade4e832627b4f6
    """
    obj = hashlib.md5()
    if salt is not None and front is True and not back:
        obj.update(salt + string)
    elif salt is not None and back is True and not front:
        obj.update(string + salt)
    else:
        obj.update(string)
    return obj.hexdigest()


def sha1(string, salt=None, front=False, back=False):
    """
      Create an SHA1 hash from a given string

      > :param string: string to be hashed
      > :return: a SHA1 hashed string

      Example:
        >>> sha1("test")
        a94a8fe5ccb19ba61c4c0873d391e987982fbbd3
    """
    obj = hashlib.sha1()
    if salt is not None and front is True and not back:
        obj.update(salt + string)
    elif salt is not None and back is True and not front:
        obj.update(string + salt)
    else:
        obj.update(string)
    return obj.hexdigest()


def sha2(string, salt=None, front=False, back=False):
    obj = None


def sha224(string, salt=None, front=False, back=False):
    """
       Create a SHA224 hash from a given string

      > :param string: string to be hashed
      > :return: an SHA224 hash

      Example:
        >>> sha224("test")
        90a3ed9e32b2aaf4c61c410eb925426119e1a9dc53d4286ade99a809
    """
    obj = hashlib.sha224()
    if salt is not None and front is True and not back:
        obj.update(salt + string)
    elif salt is not None and back is True and not front:
        obj.update(string + salt)
    else:
        obj.update(string)
    return obj.hexdigest()


def sha256(string, salt=None, front=False, back=False):
    """
      Create an SHA256 hash from a given string

      > :param string: string to be hashed
      > :return: a SHA256 hash

      Example:
        >>> sha256("test")
        9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08
    """
    obj = hashlib.sha256()
    if salt is not None and front is True and not back:
        obj.update(salt + string)
    elif salt is not None and back is True and not front:
        obj.update(string + salt)
    else:
        obj.update(string)
    return obj.hexdigest()


def sha384(string, salt=None, front=False, back=False):
    """
      Create an SHA384 hash from a given string

      > :param string:
      > :return:

      Example:
        >>> sha384("test")
        768412320f7b0aa5812fce428dc4706b3cae50e02a64caa16a782249bfe8efc4b7ef1ccb126255d196047dfedf17a0a9
    """
    obj = hashlib.sha384()
    if salt is not None and front is True and not back:
        obj.update(salt + string)
    elif salt is not None and back is True and not front:
        obj.update(string + salt)
    else:
        obj.update(string)
    return obj.hexdigest()


def sha512(string, salt=None, front=False, back=False):
    """
      Create an SHA512 hash from a given string

      > :param string: string to be hashed
      > :return: an SHA512 hash

      Example:
        >>> sha512("test")
        ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db27ac185f8a0e1d5f84f88bc887fd67b143732c304cc5fa9ad8e6f57f50028a8ff
    """
    obj = hashlib.sha512()
    if salt is not None and front is True and not back:
        obj.update(salt + string)
    elif salt is not None and back is True and not front:
        obj.update(string + salt)
    else:
        obj.update(string)
    return obj.hexdigest()


def whirlpool(string, salt=None, front=False, back=False):
    """
      Create a WHIRLPOOL hash from a given string

      > :param string: string to be hashed
      > :return: a WHIRLPOOL hash

      Example:
        >>> whirlpool("test")
        b913d5bbb8e461c2c5961cbe0edcdadfd29f068225ceb37da6defcf89849368f8c6c2eb6a4c4ac75775d032a0ecfdfe8550573062b653fe92fc7b8fb3b7be8d6
    """
    obj = hashlib.new("whirlpool")
    if salt is not None and front is True and not back:
        obj.update(salt + string)
    elif salt is not None and back is True and not front:
        obj.update(string + salt)
    else:
        obj.update(string)
    return obj.hexdigest()


def dsa(string, salt=None, front=False, back=False):
    """
      Create a DSA hash from a given string

      > :param string: string to be hashed
      > :return: a DSA hash

      Example:
        >>> dsa("test")
        a94a8fe5ccb19ba61c4c0873d391e987982fbbd3
    """
    obj = hashlib.new("DSA")
    if salt is not None and front is True and not back:
        obj.update(salt + string)
    elif salt is not None and back is True and not front:
        obj.update(string + salt)
    else:
        obj.update(string)
    return obj.hexdigest()


def tiger192(string, salt=None, front=False, back=False):
    """
      Hash a password using Tiger192

      > :param string: string to be hashed into Tiger192
      > :return: a Tiger192 hash

      Example:
        >>> tiger192("test")
        8d1fd829fc83b37af1e5ba697ce8680d1d8bc430d76682f1
    """
    if salt is not None and front is True and not back:
        obj = tiger.hash(salt + string)
    elif salt is not None and back is True and not front:
        obj = tiger.hash(string + salt)
    else:
        obj = tiger.hash(string)
    return obj.lower()

