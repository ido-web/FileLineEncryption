import hashlib

def sha256(text):
    '''
    SHA256加密

    :param text: 传入需要加密手机号码
    :return: 加密后的数据
    '''
    jm_text = hashlib.sha256(text.encode('utf-8')).hexdigest()
    return jm_text

def sha1(text):
    '''
    SHA1加密

    :param text: 传入需要加密手机号码
    :return: 加密后的数据
    '''
    jm_text = hashlib.sha1(text.encode('utf-8')).hexdigest()
    return jm_text

def sha224(text):
    '''
    SHA224加密

    :param text: 传入需要加密手机号码
    :return: 加密后的数据
    '''
    jm_text = hashlib.sha224(text.encode('utf-8')).hexdigest()
    return jm_text

def sha384(text):
    '''
    sha384

    :param text: 传入需要加密手机号码
    :return: 加密后的数据
    '''
    jm_text = hashlib.sha384(text.encode('utf-8')).hexdigest()
    return jm_text

def sha512(text):
    '''
    SHA256加密

    :param text: 传入需要加密手机号码
    :return: 加密后的数据
    '''
    jm_text = hashlib.sha512(text.encode('utf-8')).hexdigest()
    return jm_text
