## Sleipnir
Sleipnir is a simple Python messenger with encryption.

Sleipnir can be launched either in server mode (with "-s" flag) or in client mode.
Users who launch as server can still message other users as though they are a client.

When Sleipnir is launched as a server, the host chooses the password that will allow clients to connect.
Obviously, passwords are not sent in plaintext and instead the client/server pass hashes are compared to determine a match.
Matchings passwords renders messages as mutually legible via en/decryption.


## Usage: 
To launch as Client ("q!" to quit):
    
    Sleipnir.py -t [IP]
    
    Sleipnir.py -t [IP] -p [PORT]

To launch as Server:
    
    Sleipnir.py -t [IP] -s
    
    Sleipnir.py -t [IP] -p [PORT] -s

## Dependencies:

    Python Crytodome library ["pip install pycryptodomex"]
