from .constants import COUCHDB_URI, COUCHDB_DB
from .models import Number
from elasticsearch import Elasticsearch
from couchdb import Server as CouchdbServer


server = CouchdbServer(COUCHDB_URI)
if COUCHDB_DB not in server:
    server.create(COUCHDB_DB)
db = server[COUCHDB_DB]
es = Elasticsearch(["elastic"], maxsize=25)

def get_number_and_assign_to_request(request, doc):
    number = Number(doc)
    request.number = number


# обгортка-декоратор для вюшки, дозволяє виконати дію перед вюшкою
def retrieve_number(wrapped):
    def wrapper(context, request):
        db = request.registry.db
        number_id = request.matchdict['number_id']
        doc = db.get(number_id)
        if doc is not None and doc.get('doc_type') == 'Number':
            get_number_and_assign_to_request(request, doc)
        elif doc is None or doc.get('doc_type') != 'Number':
            request.number = None

        response = wrapped(context, request)
        return response
    return wrapper
