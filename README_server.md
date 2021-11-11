# Server Usage

The server is a Flask application hosted on Heroku (a PaaS) at https://triemaker.herokuapp.com using gunicorn and nginx. The client CLI performs GET requests to certain URL paths on this server to execute commands and operate on the global trie. There are two files in charge of the server's functionality.

### `trie.py`
- Maintains the data structures representing the global trie
- Hosts the functions that manipulate the global trie and communicate information about it

#### Functions
- `add(keyword)`: This function will add a keyword to the trie. If the keyword already exists, there will be no change to the trie.
- `remove(keyword)`: This function will remove a keyword from the trie. If the keyword doesn't exist, there will be no change to the trie and the user will be notified.
- `check(keyword)`: This function will check whether a keyword is in the trie, returning "True" or "False" accordingly
- `suggest(prefix)`: This function will provide autocomplete suggestions. If there are no suggestions, nothing is returned
- `display()`: This function will return a top-down display of the tree on the CLI.  

For further details, check `README_client.md`.

### `server.py`
- Uses Flask to map URL routes to functions performed on the global trie in `trie.py`

#### URL Paths
- `/add/<keyword>`: The CLI will send a GET request to this URL path if the user wants to add a keyword in the trie

- `/remove/<keyword>`: The CLI will send a GET request to this URL path if the user wants to remove a keyword if it exists in the trie

- `/check/<keyword>`: The CLI will send a GET request to this URL path if the user wants to check whether a keyword exists

- `/suggest/<prefix>`: The CLI will send a GET request to this URL path if the user wants to obtain autocomplete suggestions for the prefix

- `/display`

### Procfile
- Specifies information about the WSGI (Web Service Gateway Interface) to host the Flask app on Heroku
- Gunicorn and NGINX are used in pair to handle requests directed to the Flask app
