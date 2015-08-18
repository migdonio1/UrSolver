from django.shortcuts import get_object_or_404, render,loader,RequestContext,render_to_response

# Create your views here.
from django.http import HttpResponse,Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Solvers,Skill
from .forms import UsuarioForm


def index(request):
    latest_solvers_list = Solvers.objects.order_by('-fechaRegistro')[:5]
    context = {'latest_solvers_list' : latest_solvers_list}
    return render(request,'polls/index.html',context)

def detail(request, solver_id):
    try:
        solver = Solvers.objects.get(pk=solver_id)
    except Solvers.DoesNotExist:
        raise Http404("Solver does not exist")
    return render (request, 'polls/detail.html',{'solver':solver})

def results(request,solver_id):
    solver = get_object_or_404(Solvers,pk=solver_id)
    return render(request,'polls/results.html', {'solver': solver})

def registrar(request):
    if request.method =='POST':
        formSolver = UsuarioForm(request.POST)
        if formSolver.is_valid():
            formSolver.save()
            return HttpResponseRedirect('registrar.html')
    else:
        formSolver = Usuarioform()
    return render_to_response('polls/registrar.html',{'formSolver':formSolver},context_instance=RequestContext(request))  