import socket

# Zad13

datagram = "ed740b550024effd70726f6772616d6d696e6720696e20707974686f6e2069732066756e"

src_port_hex = datagram[0:4]
dst_port_hex = datagram[4:8]
data_hex = datagram[16:]

src_port = int(src_port_hex, 16)
dst_port = int(dst_port_hex, 16)
data = int((len(data_hex)*4)/8)

output = f"zad14odp;src;{src_port};dst;{dst_port};data;{data}"



print(output)

# ===============================================================

# Zad14