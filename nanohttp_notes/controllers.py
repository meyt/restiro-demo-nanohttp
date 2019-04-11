from nanohttp import (
    Controller,
    RestController,
    json,
    context,
    HTTPBadRequest,
    HTTPNoContent
)

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
        
        @apiDescription # Ferri lustravit hasta memorabile morientis suos
        
        ## Facem mei aris
        
        Lorem markdownum **nec** poenas, in tuus at arida. I dixere bulla *solo est*,
        enim passim parvus, et **amat milite manu** sui referens, et regna. Oris
        quoniam! Quoque hoc nec missa **servare premuntur** Agamemnona vis obruor
        doliturus.
        
        1. Pollice lumina discedunt semine
        2. Aeneadae neu adopertam
        3. Certe memorique decolor distinctus corpora
        
        ## Meliore in mea mihi
        
        Antiqua adesse petisti. A servat imagine quae!
        
        Sanguinis me quid: tinxit conviciaque [vult cumque bene](http://etadducor.org/)
        tamen? Talia hoc centum inveniunt antiquus acuta inpulsu: suis imoque posses,
        vult non *lanianda* ferentes. In tibi quae vel **calido volat secretaque**
        vertit sit dixit, libera ipse valvis duos.
        
        ## Et auctorem habitandae mutua vix
        
        Ut et Riphea vastum et aliter tantum quod Telamon cornu ab addita, nunc. Illa
        non. Quaerit rigescere arcere multis sine. Fuga huic Osiris. Illi arma habebit:
        quoque abit dederat salutem genu, Alcyone.
        
        ## Ac ope ratus cum patebat spemque
        
        Pars per excusare portare actum conantemque carne, arma cum cum vultus quondam
        Salmacis altera reponere cacumen sacra. Roboris adit illa et luserit dederint
        rem. Poteras contigerant meosque nubila saucius in reverentia alte dubites, sed
        aut conantesque simul: dare **indignantia duris non** fletque. Pulsa verborum
        invenies venias terrigenasque cuspide lactantiaque magis tenebat **Troades
        frustra**, at corpora fortis. Suspiria repetebam peto reducunt circa cum in
        **voce** nullo exterrita facta.
        
        ## Enim utque prodere
        
        [Suis redeuntis](http://quamratem.net/tua) seque **et** qui saepe pietate illa
        tuo incaluitque cumque parte miratur rigidi et. **Bono et** semel trementi
        [quid](http://deus.org/ibiamuli.aspx). Gratissime viderunt geminatis dicentum
        arbor, faucibus quamvis denique teli at, mihi. Ornum tolle dilata Telamon, in
        est Phrygiae aevi aras terras porrigit. Matrum Ino laedunt inspiciunt et sanguis
        Thebis potest; laboras constitit amari in quies Naupliades.
        
        Placent serpentem pectus occupat superinposita [Midae
        repetitque](http://nisirupibus.org/) et murmure traxit. Iungere protinus
        confinia famulae, de saxum trepidat citius, relevare poenaeque hunc dederant,
        est. Et perque oblitus vestibus hederis. **Et Pallas ut** distuleratque tuum
        lacrimisque **nostris**?
        
        Et nec quaecumque in arguit, Aonides terga, calamis praecordia *veluti* reponit
        **ratae** tamen mora unda [vocis reverti Aethionque](http://hoc.net/). Damnare
        posse naturaeque movet Minervam temperat vim.
        
        @apiUrlParam noteId
        
        """
        if note_id:
            return notes[int(note_id)]

        return notes

    @json
    def post(self):
        """
        @api {post} /note Create new note
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

    @json
    def delete(self, id_: int):
        """
        @api {delete} /note/:id Delete a note
        @apiGroup Note
        @apiVersion 1
        @apiPermission none
        """
        if int(id_) > 999:
            raise HTTPBadRequest('Invalid ID')

        raise HTTPNoContent


class RootController(Controller):
    note = NoteController()
