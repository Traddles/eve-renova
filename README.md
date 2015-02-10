# eve-renova
Eve and falsk at the same time. `TRIAL`

## Get started
Add some data to play with:

### Add data to 'unit'
`curl -d '[{"name": "symb2", "state": "on"}]' -H 'Content-Type: application/json'  http://127.0.0.1:5000/unit`

"Right now only state on and off is allowed."

### Look at data
`curl http://127.0.0.1:5000/all/on | jsonify`

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
