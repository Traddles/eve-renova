# eve-renova
Eve and falsk at the same time. `TRIAL`

## Docs
[Flask 0.1](http://flask.pocoo.org/docs/0.10/api/)
[Eve config](http://python-eve.org/config.html)

## Get started

### Add data to 'unit'
Add some data to play with:
`curl -d '[{"name": "symb2", "state": "on"}]' -H 'Content-Type: application/json'  http://127.0.0.1:5000/unit`

"Right now only state on and off is allowed."

### Look at data
`curl http://127.0.0.1:5000/all/on | jsonify`

### Patch data
To patch an item (with etag-check "If-Match"-thing)
`curl -H "Content-Type: application/json" -H "If-Match: df43b5315ceebb5b45ac6825cd48caeb154d787c" -X PATCH -i http://0.0.0.0:5111/unit/54d8b2639f19a36c2c337a99 -d '{"state": "nigh"}'`

#### Etags
[Etags-uninitiated](https://ibuildings.nl/blog/2013/07/etags-uninitiated)

#### jsonify alias in linux
jsonify is aliased to `python -m json.tool`

## Data structure
```python
{
    "_id" : ObjectId("54d8b44c9f19a36cc98cbdcf"),
    "_updated" : ISODate("2015-02-09T13:21:16.000Z"),
    "_created" : ISODate("2015-02-09T13:21:16.000Z"),
    "_allowed_fields" : {
        "state" : {
            "0" : "off",
            "1" : "on"
        }
    },
    "name" : "obama",
    "state" : "off"
}
```

## Future additions to functionality
* Todo-list for different areas (cabin e.g.) [How to](http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)


### Comment
"Cross-Origin Request Blocked: The Same Origin Policy disallows reading the remote resource at http://localhost:5111/all/on. This can be fixed by moving the resource to the same domain or enabling CORS."
[Unleash ajax with CORS](http://dev.housetrip.com/2014/04/17/unleash-your-ajax-requests-with-cors/)
