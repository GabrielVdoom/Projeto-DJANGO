from django.db import models

class CadastroForm (models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome_completo = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    usuario = models.CharField(max_length=100)
    senha = models.CharField(max_length=32)
    email = models.EmailField()
    telefone = models.CharField(max_length=14)
    genero = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    data_nascimento = models.DateField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'usuarios'