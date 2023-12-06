import crc32c
import random

checksum = crc32c.crc32c("hola mundo".encode())
checksum_2 = crc32c.crc32c("hola mundo".encode())

def add_crc(data):
    checksum = crc32c.crc32c(data.encode())
    return f"{data}|{checksum}"

def verify_crc(data_with_crc):
    parts = data_with_crc.split('|')
    data = parts[0]
    if random.random() <= 0.25:
        x = len(data)
        data =  data[:x] + "X" + data[x:]

    print(f"Data: {data}")
    received_checksum = int(parts[1])
    calculated_checksum = crc32c.crc32c(data.encode())
    print(bin(calculated_checksum))
    return data, received_checksum == calculated_checksum

data = "Hola, como estas?"

data_crc = add_crc(data)
print(data_crc)

verified_data = verify_crc(data_crc)
print(verified_data)


# modified_data = data[:5] + "X" + data[6:]
# print(modified_data)
# verified_modified = verify_crc(add_crc(modified_data))
# print(verified_modified)