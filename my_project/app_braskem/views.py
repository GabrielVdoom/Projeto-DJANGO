from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CadastroForm

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()  # Salva os dados do formulário no banco de dados
            messages.success(request, 'Cadastro realizado com sucesso! Você pode fazer login agora.')
            return redirect('success')  # Redireciona para a página de sucesso ou outra view
        else:
            messages.error(request, 'Erro no cadastro. Verifique os dados e tente novamente.')
    else:
        form = CadastroForm()

    return render(request, 'index.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['usuario-login']
        password = request.POST['senha-login']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            return redirect('home')  # Redireciona para a página inicial ou outra página
        else:
            messages.error(request, "Usuário ou senha incorretos.")
    return render(request, 'login.html')

def success(request):
    return render(request, 'success.html')