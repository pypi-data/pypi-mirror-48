# flask-api-spec

[![PyPI version](https://badge.fury.io/py/flask-api-spec.svg)](https://badge.fury.io/py/flask-api-spec)

flask API toolset

```
pip install flask-api-spec
```

## started with a simple idea

Let's

- write validation codes for **requests**
- write validation and serialization codes for **responses**
- write API body
- integrate **authorizations** then protect the APIs
- **swaggerize** all of them automatically
- _with Flask_

## usage

### installation

```python
import flask_api_spec

app = Flask(__name__)
flask_api_spec.init_app(app)
```

### examples

```python
from flask_api_spec import Value


@app.route('/hello', apispec=dict(
    query=dict(  # constraints for request.args
        id=Value(int, error='There is not id or id is not int.')
    )
))
def hello_id():
    return dict(result='The id is %s' % request.args['id'])
```

Focus on what begins with `apispec=`. We've got a robust feature for the API using the extended app.route with the apispec keyword argument.

```python
from flask_api_spec import Value


@app.route('/hello/<string:name>', apispec=dict(
    param=dict(  # constraints for parameters
        name=Value(str, lambda x: len(x) > 3, error='name is no string or the length is not greater than 3')
    )
))
def hello_name(name):
    return dict(result='Hello %s!' % name)
```

A param keyword in `apispec=` indicates in-path parameters. We can state some more detailed rules about them explicitly. In the case above, size of `<string:name>` should exceed 3.

## todo

- [ ] support more mashmallow functionalities
- [ ] support more schema functionalities
- [ ] integrate authorization
- [ ] generate full swagger yaml
- [ ] support flask class view
