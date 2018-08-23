# coding=utf-8
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, analyzer, tokenizer, Index, token_filter
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from emails.models import EMailPost

HOST = '127.0.0.1'
PORT = '9200'
stopwords = "а,без,более,бы,был,была,были,было,быть,в,вам,вас,весь,во,вот,все,всего,всех,вы,где,да,даже,для,до,его,ее,если,есть,еще,же,за,здесь,и,из,или,им,их,к,как,ко,когда,кто,ли,либо,мне,может,мы,на,надо,наш,не,него,нее,нет,ни,них,но,ну,о,об,однако,он,она,они,оно,от,очень,по,под,при,с,со,так,также,такой,там,те,тем,то,того,тоже,той,только,том,ты,у,уже,хотя,чего,чей,чем,что,чтобы,чье,чья,эта,эти,это,я,a,an,and,are,as,at,be,but,by,for,if,in,into,is,it,no,not,of,on,or,such,that,the,their,then,there,thesethey,this,to,was,will,with"

connections.create_connection()
simple_analyzer = analyzer(
    'my_analyzer',
    type='custom',
    tokenizer=tokenizer('standard'),
    filter=["lowercase", "russian_morphology", "english_morphology", token_filter('my_stop', 'stop', stopwords=stopwords)]
)

class EmailIndex(DocType):
    description = Text(analyzer=simple_analyzer)
    created = Date()
    text = Text(analyzer=simple_analyzer)
    sender = Text()

    class Index:
        name = 'email'

def bulk_indexing():
    EmailIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in EMailPost.objects.all().iterator()))



