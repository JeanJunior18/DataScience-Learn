import pymongo as pm

# Conecta > Cria a Base de Dados > Cria a Collection
conn = pm.MongoClient()
db = conn.Banco
acessos = db.acessos

# Cria o conjunto chave valor que vai ser inserido na Base de Dados
acesso = {
    'ip':'localhost',
    'port':'8888',
    'OS':'Windows'
}

# insere o o arquivo de chave e valor na collection e cria automaticamente um id
# db.acessos.insert_one(acesso)

# Mostra todos os arquivos na collection, ou com os requistos chave valor entre parenteses
for rec in db.acessos.find({'port': '8888', 'OS':'Windows'}):
    print(rec)

print(conn.list_database_names())
print(db.list_collection_names())
print(acessos.estimated_document_count())