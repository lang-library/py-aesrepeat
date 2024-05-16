from aesrepeat import *

text = "Pythonの暗号化ライブラリとそれらの概要を表にまとめました。非常にたくさんのライブラリがあることがわかりました。それぞれのライブラリが得手不得手を持っているためユースケースに応じて適切なライブラリを使用する必要があります。"
bytes = text.encode()

ar = AES128(["aa", "bb"])

print("")
encoded = ar.encode_text(text)
print(encoded)
decoded = ar.decode_text(encoded)
print(decoded)

print("")
encoded = ar.encode_bytes(bytes)
print(encoded)
decoded = ar.decode_bytes(encoded)
print(decoded.decode())

print("")
list = [11, 22, 33]
encoded = ar.encode_pickle(list)
print(encoded)
decoded = ar.decode_pickle(encoded)
print(decoded)

ar = AES256(["aa", "bb"])

print("")
encoded = ar.encode_text(text)
print(encoded)
decoded = ar.decode_text(encoded)
print(decoded)

print("")
encoded = ar.encode_bytes(bytes)
print(encoded)
decoded = ar.decode_bytes(encoded)
print(decoded.decode())

print("")
list = [11, 22, 33]
encoded = ar.encode_pickle(list)
print(encoded)
decoded = ar.decode_pickle(encoded)
print(decoded)
