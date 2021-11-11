# Server Usage

The server is a Flask application hosted on Heroku (a PaaS) using gunicorn and nginx. The client CLI performs GET requests to certain URL paths on this server to execute commands and operate on the global trie. There are two files in charge of the server's functionality.

### `trie.py`
- Maintains the data structures representing the global trie
- Hosts the functions that manipulate the global trie and communicate information about it

### `server.py`
- Uses Flask to map URL routes to functions performed on the global trie in `trie.py`

#### `display`

### Procfile
- Specifies information about the WSGI (Web Service Gateway Interface) to host the Flask app on Heroku
- Gunicorn and NGINX are used in pair to handle requests directed to the Flask app
