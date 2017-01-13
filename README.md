# eve-renova
Eve and falsk at the same time. `TRIAL`

## Database
Runs on *MongoDb* db-name **eve**. 

## Docs
[Flask 0.1](http://flask.pocoo.org/docs/0.10/api/)
[Eve config](http://python-eve.org/config.html)

## Get started
Run the following python apps simultaniously. E.g. in a split console screen: [Screen to split terminal](http://unix.stackexchange.com/questions/7453/how-to-split-the-terminal-into-more-than-one-view)

Console 1: `python eveapp.py`

Console 2: `python flasker.py`

### Add data to 'unit'
Add some data to play with:
`curl -d '[{"name": "tvättmaskin", "state": "off"}]' -H 'Content-Type: application/json'  http://0.0.0.0:5111/unit`

"Right now only state on and off is allowed."

### Look at data
`curl http://127.0.0.1:5000/all/on | jsonify`

### Look at unit data
`curl -H 'Content-Type: application/json'  http://127.0.0.1:5111/unit/obama | jsonify`
```python
{
    "_created": "Mon, 09 Feb 2015 13:21:16 GMT",
    "_etag": "8b11ff59a484bdc74827a7c5cc7c7a33322f602c",
    "_id": "54d8b44c9f19a36cc98cbdcf",
    "_links": {
        "collection": {
            "href": "/unit",
            "title": "unit"
        },
        "parent": {
            "href": "",
            "title": "home"
        },
        "self": {
            "href": "/unit/54d8b44c9f19a36cc98cbdcf",
            "title": "unit"
        }
    },
    "_updated": "Thu, 12 Feb 2015 12:00:09 GMT",
    "name": "obama",
    "state": "on"
}
```

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

### Data schema
Check settings.py out and see the configuration of the rules for the fields in the schema definition.

## Future additions to functionality
* Todo-list for different areas (cabin e.g.) [How to](http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)


### Comment
"Cross-Origin Request Blocked: The Same Origin Policy disallows reading the remote resource at http://localhost:5111/all/on. This can be fixed by moving the resource to the same domain or enabling CORS."
[Unleash ajax with CORS](http://dev.housetrip.com/2014/04/17/unleash-your-ajax-requests-with-cors/)
