# Get notes

## `GET` `/note`


## Parameters

### Query-string parameters

Name | Type | Required | Default | Example | enum | Pattern | MinLength | MaxLength | Minimum | Maximum | Repeat | Description
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
sort | None | `False` |  |  |  |  |  |  |  |  | `False` |  

## Examples

### #0

#### Request: 

```
GET /note HTTP/1.0
Host: localhost:80
```
```

```

#### Response: 

```
Content-Type: application/json; charset=utf-8
Content-Length: 22
```
```json
"[\n    \"Welcome Note\"\n]"
```

---
