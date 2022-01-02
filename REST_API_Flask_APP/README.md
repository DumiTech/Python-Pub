=========================================================================
**Install all packages**
```
pip install -r requierments.txt
```

Make sure to activate the virtual environment!

=========================================================================

**To set up Flask, run the following:**

```
python -m pip install flask
```

Once flask is installed, save the code in a file called app.py. To run this Flask application, you first need to set an environment variable called FLASK_APP to app.py. This tells Flask which file contains your application.

**For macOS or Linux use shell:**
```
export FLASK_APP=app.py
```

You can set FLASK_ENV to development, which puts Flask in debug mode:
```
export FLASK_ENV=development
```

**For windows use cmd/windows terminal:**
```
C:\> set FLASK_APP=app.py
C:\> set FLASK_ENV=development
```

To start the Flask development server:
```
flask run
```

**Send HTTP requests from the command line using curl. Adding a new country to the list of countries:**
```
curl -i http://127.0.0.1:5000/countries \
-X POST \
-H 'Content-Type: application/json' \
-d '{"name":"Germany", "capital": "Berlin", "area": 357022}'
```

**Curl to send a GET request to /countries**
```
curl -i http://127.0.0.1:5000/countries
```