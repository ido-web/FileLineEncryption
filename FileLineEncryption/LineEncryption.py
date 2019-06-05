# coding: utf-8

import os
from xml.dom.minidom import parse
from SHA import sha256,sha1,sha224,sha384,sha512



class LineEncryption(object):
    '''
    使用sha256对文件进行加密并输出
    '''
    def __init__(self):
        # 获取配置文件数据
        method,filename = self.get_config()

        print({'加密方式':method,'文件名':filename})

        if not method:
            raise Exception("请在config.xml文件里，配置所需加密方法")
        if not filename:
            raise Exception('请在config.xml文件里，配置所需加密文件名称')

        # 文件路径
        self.__filename = os.path.join('FileLineEncryption/file',filename)


        # 截取文件名和后缀名
        filename, suffix = os.path.splitext(self.__filename)
        # 拼接输出的文件名
        output_filename = filename + '_' + method + suffix

        self.out = open(output_filename, 'a', encoding='utf-8')

        if method.lower().strip() == 'sha256':
            self.__method = sha256
        elif method.lower().strip() == 'sha1':
            self.__method = sha1
        elif method.lower().strip() == 'sha224':
            self.__method = sha224
        elif method.lower().strip() == 'sha384':
            self.__method = sha384
        elif method.lower().strip() == 'sha512':
            self.__method = sha512
        else:
            raise Exception("目前还不支持您配置的加密方式")
         # TODO 追加加密方式




    # @property
    # def jm_method(self,method):
    #     jm_method = None
    #     if method.lower() == 'sha256':
    #         jm_method = sha256
    #
    #     return jm_method


    def run(self):
        try:
            with open(self.__filename, 'r',encoding='utf-8') as fp:
                while True:
                    line = fp.readline()  # 整行读取数据
                    if not line:
                        break

                    line = line.replace('\n','')
                    # 调用加密方法，获取加密后的字符串
                    jm_text = self.__method(text=line)
                    self.out.write(jm_text + '\n')
        except Exception as ret:
            print(ret)
            raise Exception('没有找到文件。请把文件放在LineEncryption目录下的file目录下，或请确认配置的文件名是否正确')
        finally:
            self.out.close()


    def get_config(self):
        '''
        获取配置文件
        :return: method,filename
        '''
        # 打开匹配文档
        DOMTree = parse('./FileLineEncryption/config.xml')
        # 获取文件元素对象
        document = DOMTree.documentElement
        # 读取配置文件中EncryptionInfo信息
        encryptionInfo_list = document.getElementsByTagName('EncryptionInfo')

        # 获取method
        method_list = encryptionInfo_list[0].getElementsByTagName('method')
        # 获取filename
        filename_list = encryptionInfo_list[0].getElementsByTagName('filename')

        # 获取值
        try:
            method = (method_list[0].childNodes[0].data).strip()
            filename = (filename_list[0].childNodes[0].data).strip()
        except IndexError:
            raise Exception('没有找到文件。请确认config.xm配置的文件名是否正确')
        return method,filename

if __name__ == '__main__':
    lineEncryption = LineEncryption()
    lineEncryption.run()







