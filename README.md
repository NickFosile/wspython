# wspython
a python mini-server that can handle websocket connections

The idea is to create a python tcp server that can handle websockets connections. This software is intended to be used in a small-scale multiplayer browser games, mostly.

For me, it is a chance to experiment with the python asynchronous API and how I can use it combined with threading in order to support (why not) more network intensive web games (or any other type of application).

Any suggestions, comments or submits are very welcome.


FIRST STEP
 For now, I am creating a basic server socket that accepts connections, passing them to a threaded connection handler that verifies the client and then maintains packet exchange with that client (or disconnect), while the main thread is ready to accept another client. For starts, I will add some code to the connection handler to explore more the websocket protocol.
