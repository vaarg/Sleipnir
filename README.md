## Sleipnir
Sleipnir is an encrypted Python messenger with multi-threading.

Sleipnir can be launched either in server mode (with "-s" flag) or in client mode.
Users who launch as server can still message other users as though they are a client.

Sleipnir utilises multi-threading and thus supports multiple simultaneous users.

When Sleipnir is launched as a server, the host chooses the password that allows clients to connect.
Obviously, passwords are not sent in plaintext and instead the server attempts to decrypt the client pass hash on the assumption that both server and client have the same password. If decryption is successful then the client connects, otherwise the client is disconnected. Furthermore, matchings passwords render messages as mutually legible via en/decryption.


## Usage: 
To launch as Client ("q!" to quit):
    
    Sleipnir.py -t [IP]
    
    Sleipnir.py -t [IP] -p [PORT]

To launch as Server:
    
    Sleipnir.py -t [IP] -s
    
    Sleipnir.py -t [IP] -p [PORT] -s

## Dependencies:
Python Cryptodome library: 
    
    pip install pycryptodomex

## Why is this program named "Sleipnir"?

In Germanic mythology Sleipnir is the steed of Odin and a child of Loki. In addition to his other attributes, Odin is a god of knowledge and secrets. He is the god who gave runes (written language) to mankind and yet he is also a psychopomp; one who leads the dead to the afterlife, while riding Sleipnir - whether to Hel or Valholl.

Naming this program Sleipnir felt apt. The program itself is 'secretive' in its use of encryption (and Sleipnir's links to Loki and secretism work well too) and sometimes the non-sense of staring at hashes too long feels like looking at runes. Communication is information, and information is knowledge which I felt suited the Odinic theme well. I also feel like Sleipnir worked with the chthonic theme of 'underground' (encrypted/private) communication.
