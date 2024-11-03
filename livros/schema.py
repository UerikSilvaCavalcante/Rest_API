from ninja import ModelSchema, Schema
from .models import Categoria, Livro

class LivrosSchema(ModelSchema):
    class Meta:
        model = Livro
        fields = ['nome', 'streaming','categorias']

class AvaliacaoSchema(ModelSchema):
    class Meta:
        model = Livro
        fields = ['nota', 'comentarios']

class FiltrosSortear(Schema):
    nota_minima:int = None
    categorias:int = None
    reler:bool = False