from django.http import HttpResponse
from health_genetics.models import *
from health_genetics.forms import *
from datetime import datetime
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from health.models import gnuhealth_pathology
from health_configuration.models import *
from health_party.models import *
from health_demographics.forms import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

def index(request):
    genetics = gnuhealth_patient_genetic_risk.objects.all()
    return render(request, 'health_genetics/index.html' , {'genetics':genetics})

def genetics(request):
    type = "grid"
    genetics = gnuhealth_patient_genetic_risk.objects.all()
    return render(request, 'health_genetics/genetics.html'
                  , {'genetics': genetics
                      , 'type': type})


def addGenetic(request):
    if request.method == "POST":
        form = geneticForm(request.POST)
       # if form.is_valid():
        #    try:
        type = "grid"
        msg = "1"
        latest = gnuhealth_patient_genetic_risk.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        #form.fields["id"].initial = 1
        id = request.POST['id']
        create_date = request.POST['create_date']
        create_uid = request.POST['create_uid']
        disease_gene = 2
        healthprof = request.POST['healthprof']
        institution = None
        natural_variant = request.POST['natural_variant']
        notes = request.POST['notes']
        onset = request.POST['onset']
        patient = request.POST['patient']
        variant_phenotype = request.POST['variant_phenotype']
        write_date = request.POST['write_date']
        write_uid = request.POST['write_uid']
        genet = gnuhealth_patient_genetic_risk(id=id, write_date=write_date, write_uid=write_uid,create_date=create_date,
        create_uid=create_uid,
        disease_gene = disease_gene,
        healthprof = healthprof,
        institution = institution,
        natural_variant = natural_variant,
        notes = notes,
        onset = onset,
        patient = patient,
        variant_phenotype = variant_phenotype,
         )
        genet.save()
        genetics = gnuhealth_patient_genetic_risk.objects.all()
        messages.success(request, f'Success, Record Saved Successfully')
        return render(request, 'health_genetics/genetics.html'
                              , {'type': type, 'msg': msg, 'genetics': genetics})
          #  except:
           #     pass
        #else:
         #   messages.error(request, f'Sorry, Record Save Error')
          #  return HttpResponse("Invalid Form.")
    else:
        form = geneticForm()
        latest = gnuhealth_patient_genetic_risk.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        #form.fields["id"].initial = 1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = True
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'health_genetics/genetics.html', {'type': type, 'form': form})


def editGenetic(request, id):
    type = "edit"
    editForm = gnuhealth_patient_genetic_risk.objects.get(id=id)
    return render(request, 'health_genetics/genetics.html', {'form': editForm, 'type': type})


def updateGenetic(request, id):
    type = "grid"
    genet = gnuhealth_patient_genetic_risk.objects.get(id=id)
    id = request.POST['id']
    create_date = request.POST['create_date']
    create_uid = request.POST['create_uid']
    disease_gene = 2
    healthprof = request.POST['healthprof']
    institution = None
    natural_variant = request.POST['natural_variant']
    notes = request.POST['notes']
    onset = request.POST['onset']
    patient = request.POST['patient']
    variant_phenotype = request.POST['variant_phenotype']
    write_date = request.POST['write_date']
    write_uid = request.POST['write_uid']
    genet = gnuhealth_patient_genetic_risk(id=id, write_date=write_date, write_uid=write_uid,create_date=create_date,
        create_uid=create_uid,
        disease_gene = disease_gene,
        healthprof = healthprof,
        institution = institution,
        natural_variant = natural_variant,
        notes = notes,
        onset = onset,
        patient = patient,
        variant_phenotype = variant_phenotype,
         )
    genet.save()
    msg = "3"
    genetics = gnuhealth_patient_genetic_risk.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return render(request, 'health_genetics/genetics.html'
                  , {'type': type, 'msg': msg, 'genetics': genetics})


def deleteGenetic(request, id):
    genetic = gnuhealth_patient_genetic_risk.objects.get(id=id)
    genetic.delete()
    type = "grid"
    msg = "2"
    genetics = gnuhealth_patient_genetic_risk.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health_genetics/genetics.html'
                  , {'type': type, 'msg': msg, 'genetics': genetics})


def searchVarient(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''

    varients = gnuhealth_gene_variant.objects.filter(name__startswith=search_text.capitalize())

    if len(varients) == 0:
        varients = gnuhealth_gene_variant.objects.filter(id=search_text)

    return render_to_response('health_genetics/js/ajax-search.html', {'varients': varients})

def searchPhenotype(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''

    phenotypes = gnuhealth_gene_variant_phenotype.objects.filter(name__startswith=search_text.capitalize())

    if len(phenotypes) == 0:
        phenotypes = gnuhealth_gene_variant_phenotype.objects.filter(id=search_text)

    return render_to_response('health_genetics/js/ajax-search.html', {'phenotypes': phenotypes})

def searchGene(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''

    genes = gnuhealth_disease_gene.objects.filter(name__startswith=search_text.capitalize())

    if len(genes) == 0:
        genes = gnuhealth_disease_gene.objects.filter(id=search_text)

    return render_to_response('health_genetics/js/ajax-search.html', {'genes': genes})

def addgenetics(request):
    if request.method == "POST":  
        form = HealthGeneticsForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return HttpResponse("Data Saved.")  
            except:  
                pass
        else:
            return HttpResponse("Invalid Form.")        
    else:  
        form = HealthGeneticsForm()  
    return render(request,'health_genetics/add-person-genetic-info.html'  ,{'form':form})




# Genetics module functions start
def disease_genes(request):
    return render(request, "health_genetics_boys/genetics-disease-genes.html")

def natural_variants(request):
    return render(request, "health_genetics_boys/genetics-natural-variants.html")

def protein_related_diseases(request):
    return render(request, "health_genetics_boys/genetics-protein-related-diseases.html")

def variants_phenotype(request):
    return render(request, "health_genetics_boys/genetics-variants-phenotype.html")
# Genetics module functions end