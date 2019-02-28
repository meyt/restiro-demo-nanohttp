# untitled

## `POST` `/note`


## Parameters

### Form parameters

Name | Type | Required | Default | Example | enum | Pattern | MinLength | MaxLength | Minimum | Maximum | Repeat | Description
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
content | String | `True` |  |  |  |  |  |  |  |  | `False` |  
title | String | `False` |  |  |  |  |  |  |  |  | `False` | 

## Examples

### #0

#### Request: 

```
POST /note HTTP/1.0
Content-Length: 27
Content-Type: application/json
Host: localhost:80
```
```json
{"content": "Hello world!"}
```

#### Response: 

```
Content-Type: application/json; charset=utf-8
Content-Length: 19
```
```json
"\"None Hello world!\""
```

---
