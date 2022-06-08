## Sleipnir
Sleipnir is a simple Python messenger with encryption.

Sleipnir can be launched either in server mode (with "-s" flag) or in client mode.
Users who launch as server can still message other users as though they are a client.

Sleipnir supports multi-threading and thus supports multiple simultaneous users at once.

When Sleipnir is launched as a server, the host chooses the password that will allow clients to connect.
Obviously, passwords are not sent in plaintext and instead the server attempts to decrypt the client pass hash on the assumption that both server and client have the same password. If decryption is successful then the client connects, otherwise the client is disconnected. Furthermore, matchings passwords render messages as mutually legible via en/decryption.


## Usage: 
To launch as Client ("q!" to quit):
    
    Sleipnir.py -t [IP]
    
    Sleipnir.py -t [IP] -p [PORT]

To launch as Server:
    
    Sleipnir.py -t [IP] -s
    
    Sleipnir.py -t [IP] -p [PORT] -s

## Dependencies:

    Python Crytodome library ["pip install pycryptodomex"]
