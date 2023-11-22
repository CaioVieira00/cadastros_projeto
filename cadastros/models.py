from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.EmailField()
    endereco = models.CharField(max_length=200)
    curso = models.CharField(max_length=100)
    matricula = models.CharField(max_length=50)

class Carro(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()
    cor = models.CharField(max_length=20)
    placa = models.CharField(max_length=10)
    proprietario = models.CharField(max_length=100)

class Imovel(models.Model):
    endereco = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    quartos = models.IntegerField()
    banheiros = models.IntegerField()
    proprietario = models.CharField(max_length=100)

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20)
    carga_horaria = models.IntegerField()
    professor = models.CharField(max_length=100)
    curso_relacionado = models.CharField(max_length=100)

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    ano_publicacao = models.IntegerField()
    editora = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)

class Evento(models.Model):
    nome = models.CharField(max_length=200)
    data = models.DateField()
    local = models.CharField(max_length=200)
    descricao = models.TextField()
    organizador = models.CharField(max_length=100)
