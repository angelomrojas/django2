from django.shortcuts import render
from .forms import ContatoForm, ProdutoModelForm
from django.contrib import messages
from django.shortcuts import redirect
from .models import Produto

def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)

def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':

        if form.is_valid():
            form.send_mail()

            messages.success(request, 'Enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

def produto(request):
    
    if str(request.user) != 'AnonymousUser':

        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Enviado com sucesso!')
                form = ProdutoModelForm()
            else:
                messages.error(request, 'Produto não salvo')
        else:
            form = ProdutoModelForm()

        
        context = {
            'form': form
        }
        
        return render(request,'produto.html', context)
    
    else:
        return redirect('index')