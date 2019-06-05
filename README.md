# FileLineEncryption
文件按行加密工具

## 使用方式
 - 首先在FileLineEncryption/file目录下放置文件
比如telephone.txt

 - 然后在config.xml文件里配置你的加密信息

    如下配置 使用**sha512**的方式按行加密**telephone.txt**的内容
    ```xml
        <config>
            <EncryptionInfo>
                <!--  加密方式，目前支持 sha256 sha1 sha224 sha384 sha512  -->
                <method>sha512</method>
                <!--  需要加密的文件名称telephone.txt  -->
                <filename>telephone.txt</filename>
            </EncryptionInfo>
        </config>
    ```
然后运行LineEncryption.py即可
```
 python LineEncryption.py
```

