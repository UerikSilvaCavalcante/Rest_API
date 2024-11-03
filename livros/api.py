from ninja import Router, Query
from .schema import LivrosSchema, AvaliacaoSchema, FiltrosSortear
from .models import Livro, Categoria

livros_router = Router()

@livros_router.post('/')
def create_livro(request, livro_schema:LivrosSchema):
    nome = livro_schema.dict()['nome']
    streaming = livro_schema.dict()['streaming']
    categorias = livro_schema.dict()['categorias']
    if streaming not in ['AK', 'F', 'AU']:
        return 401,{'error': 'Invalid streaming'}
    livro = Livro(
        nome= nome,
        streaming= streaming,
    )
    livro.save()
    for categoria in categorias:
        categoria_temp = Categoria.objects.get(id=categoria)
        livro.categorias.add(categoria_temp)
    livro.save()

    return {'reponse': livro_schema.dict()}

@livros_router.get('/{livro_id}')
def get_livro(request, livro_id:int):
    livros = Livro.objects.get(id=livro_id)
    return 200, {'response': [livros.nome, livros.streaming, [categoria.nome for categoria in livros.categorias.all()]]}

@livros_router.put('/{livro_id}')
def avaliar_livro(request, livro_id:int, avaliacao_schema:AvaliacaoSchema):
    livro = Livro.objects.get(id=livro_id)
    nota  = avaliacao_schema.dict()['nota']
    comentarios = avaliacao_schema.dict()['comentarios']
    if nota < 0 or nota > 10:
        return 400, {'status': 'Nota invalida'}
    try:
        livro.nota = nota
        livro.comentarios = comentarios
        livro.save()
        return 200, {'response': {'message': 'Avaliação realizada com sucesso', 'content': [livro.nome, livro.nota, livro.comentarios]}}
    except Exception as e:
        return 500, {'error': str(e)}

@livros_router.delete('/{livro_id}')
def deletar_livro(request, livro_id:int):
    try:
        livro = Livro.objects.get(id=livro_id)
        livro.delete()
        return 200, {'response': f'Livro: {livro.nome} deletado com sucesso',}
    except Exception as e:
        return 404, {'error': str(e)}

@livros_router.get('/sortear/', response={200:LivrosSchema, 404:dict})
def sortear_livro(request, filtros:Query[FiltrosSortear]):
    # print(filtros.dict())
    categorias = filtros.dict()['categorias']
    nota_minima = filtros.dict()['nota_minima']
    reler = filtros.dict()['reler']

    livros = Livro.objects.all()
    if not reler:
        livros = livros.filter(nota=None)
    if nota_minima:
        livros = livros.filter(nota__gte=nota_minima)
    if categorias:
        livros = livros.filter(categorias__id=categorias)

    livro = livros.order_by('?').first()

    if livros.count() > 0:
        return 200, livro
    else:
        return 404, {'status': 'Nenhum livro encontrado'}
    
