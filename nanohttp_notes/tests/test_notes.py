

def test_notes(app):
    app.doc = True
    app.get('/note')

    app.doc = True
    app.get('/note/0')

    app.doc = True
    app.post_json('/note', params={
        'content': 'Hello world!'
    })
