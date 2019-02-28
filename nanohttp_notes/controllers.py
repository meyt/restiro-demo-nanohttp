from nanohttp import Controller, RestController, json, context

notes = ['Welcome Note']


class NoteController(RestController):

    @json
    def get(self, note_id: int=None):
        """
        @api {get} /note Get notes
        @apiGroup Note
        @apiVersion 1
        @apiPermission none

        @apiQueryParam [sort]
        """
        """
        @api {get} /note/:noteId Get one note 
        @apiGroup Note
        @apiVersion 1
        @apiPermission none
        
        @apiUrlParam noteId
        """
        if note_id:
            return notes[int(note_id)]

        return notes

    @json
    def post(self):
        """
        @api {post} /note
        @apiGroup Note
        @apiVersion 1
        @apiPermission none

        @apiParam {String} [title]
        @apiParam {String} content
        """
        note = '%s %s' % (
            context.form.get('title'),
            context.form.get('content')
        )
        notes.append(note)
        return note


class RootController(Controller):
    note = NoteController()
