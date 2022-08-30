from django.db import models

# Create your models here.
'''
class Categoria(Model):

    nombre = CharField(max_length=50)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre

class Publicacion(Model):
    imagen = ImageField(upload_to='blog', null=True, blank=True)
    titulo = CharField(max_length=50)
    # contenido = CharField(max_length=80)
    autor = ForeignKey(User, on_delete=CASCADE)
    categorias = ManyToManyField(Categoria)

    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'publicacion'
        verbose_name_plural = 'publicaciones'

    def __str__(self):
        return self.titulo

'''