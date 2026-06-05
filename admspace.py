# Convert spaceinvaders.scode to raw 2KB binary
# Base: $E000 (ROM A plugin slot)
scode = open('admspace.scode').read()
out = bytearray(b'\xFF' * 2048)
for line in scode.strip().split('\n'):
    line = line.strip()
    if line.startswith('S1'):
        count  = int(line[2:4], 16)
        addr   = int(line[4:8], 16)
        nbytes = count - 3
        payload = bytes.fromhex(line[8:8+nbytes*2])
        for i, b in enumerate(payload):
            off = addr - 0xE000 + i
            if 0 <= off < 2048:
                out[off] = b
open('admspace.bin', 'wb').write(bytes(out))
print(f'{len(out)} bytes written to admspace.bin')


