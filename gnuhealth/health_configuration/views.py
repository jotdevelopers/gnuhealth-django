from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from health.models import gnuhealth_pathology
from health_configuration.models import *
from health_party.models import *
from health_demographics.forms import *
from health_configuration.forms import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")

# Create Conditions Views
def condition(request):
    conditions = gnuhealth_pathology.objects.order_by('id')[:500]
    # conditions = gnuhealth_pathology.objects.all()
    return render(request, 'health_configuration/conditions/conditions.html', {'conditions': conditions, 'selected': 'Conditions'})


def ethnicity(request):
    type = "grid"
    ethnicities = gnuhealth_ethnicity.objects.all()
    return render(request, 'health_configuration/patients/ethnicities.html'
                  , {'ethnicities': ethnicities
                      , 'type': type})


def addEthnicity(request):
    if request.method == "POST":
        form = ethnicityForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                msg = "1"
                latest = gnuhealth_ethnicity.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                ethnicities = gnuhealth_ethnicity.objects.all()
                messages.success(request, f'Success, Record Saved Successfully')
                return render(request, 'health_configuration/patients/ethnicities.html'
                              , {'type': type, 'msg': msg, 'ethnicities': ethnicities})
            except:
                pass
        else:
            messages.warning(request, f'Sorry, Record Save Error - Invalid Fields')
            return redirect(addEthnicity)
    else:
        form = ethnicityForm()
        latest = gnuhealth_ethnicity.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = True
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'health_configuration/patients/ethnicities.html', {'type': type, 'form': form})


def editEthnicity(request, id):
    type = "edit"
    editForm = gnuhealth_ethnicity.objects.get(id=id)
    return render(request, 'health_configuration/patients/ethnicities.html', {'form': editForm, 'type': type})


def updateEthnicity(request, id):
    type = "grid"
    eth = gnuhealth_ethnicity.objects.get(id=id)
    name = request.POST['name']
    notes = request.POST['notes']
    code = request.POST['code']
    eth_id = eth.id
    create_date = eth.create_date
    write_date = eth.write_date
    create_uid = eth.create_uid
    write_uid = eth.write_uid
    eth = gnuhealth_ethnicity(id=eth_id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid, name=name, notes=notes, code=code)
    eth.save()
    msg = "3"
    ethnicities = gnuhealth_ethnicity.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return render(request, 'health_configuration/patients/ethnicities.html'
                  , {'type': type, 'msg': msg, 'ethnicities': ethnicities})


def deleteEthnicity(request, id):
    ethnicity = gnuhealth_ethnicity.objects.get(id=id)
    ethnicity.delete()
    type = "grid"
    msg = "2"
    ethnicities = gnuhealth_ethnicity.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health_configuration/patients/ethnicities.html'
                  , {'type': type, 'msg': msg, 'ethnicities': ethnicities})


def citizenship(request):
    type = "grid"
    countries = country_country.objects.all()
    return render(request, 'health_configuration/patients/citizenships.html'
                  , {'countries': countries
                      , 'type': type})


def add_citizenship(request):
    return render(request, 'health_configuration/patients/add_citizenship.html')


def occupation(request):
    type = "grid"
    occupations = gnuhealth_occupation.objects.all()
    return render(request, 'health_configuration/patients/occupations.html'
                  , {'occupations': occupations
                      , 'type': type})


def addOccupation(request):
    if request.method == "POST":
        form = occupationForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                msg = "1"
                form.save()
                occupations = gnuhealth_occupation.objects.all()
                return render(request, 'health_configuration/patients/occupations.html'
                              , {'type': type, 'msg': msg, 'occupations': occupations})
            except:
                pass
        else:
            return HttpResponse("Invalid Form.")
    else:
        form = occupationForm()
        latest = gnuhealth_occupation.objects.latest('id')

        form.fields["id"].initial = latest.id + 1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = True
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'health_configuration/patients/occupations.html', {'type': type, 'form': form})


def editOccupation(request, id):
    type = "edit"
    form = gnuhealth_occupation.objects.get(id=id)
    # return HttpResponse(form.code)
    return render(request, 'health_configuration/patients/occupations.html', {'form': form, 'type': type})


def updateOccupation(request, id):
    type = "grid"
    occ = gnuhealth_occupation.objects.get(id=id)
    name = request.POST['name']
    code = request.POST['code']
    occ_id = occ.id
    create_date = occ.create_date
    write_date = occ.write_date
    create_uid = occ.create_uid
    write_uid = occ.write_uid
    occ = gnuhealth_occupation(id=occ_id, create_date=create_date, write_date=write_date, create_uid=create_uid
                               , write_uid=write_uid, name=name, code=code)
    occ.save()
    msg = "3"
    occupations = gnuhealth_occupation.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return render(request, 'health_configuration/patients/occupations.html'
                  , {'type': type, 'msg': msg, 'occupations': occupations})


def deleteOccupation(request, id):
    occupation = gnuhealth_occupation.objects.get(id=id)
    occupation.delete()
    type = "grid"
    msg = "2"
    occupations = gnuhealth_occupation.objects.all()
    return render(request, 'health_configuration/patients/occupations.html'
                  , {'type': type, 'msg': msg, 'occupations': occupations})


def residence(request):
    type = "grid"
    countries = country_country.objects.all()
    return render(request, 'health_configuration/patients/residence.html'
                  , {'countries': countries
                      , 'type': type})


def add_residence(request):
    return render(request, 'health_configuration/patients/add_residence.html')


def genes(request):
    type = "grid"
    genes = gnuhealth_disease_gene.objects.order_by('id')[:200]
    return render(request, 'health_configuration/genetics/genes.html', {'type': type, 'genes': genes, 'selected': 'Disease Genes'})


def editGenes(request, id):
    type = "edit"
    editForm = gnuhealth_disease_gene.objects.get(id=id)
    return render(request, 'health_configuration/genetics/genes.html', {'form': editForm, 'type': type, 'selected': 'Disease Genes'})


def updateGenes(request, id):
    type = "grid"
    gene = gnuhealth_disease_gene.objects.get(id=id)
    gene.name = request.POST['name']
    gene.long_name = request.POST['long_name']
    gene.protein_name = request.POST['protein_name']
    gene.chromosome = request.POST['chromosome']
    gene.location = request.POST['location']
    gene.gene_id = request.POST['gene_id']

    gene.gene_id = gene.id
    gene.create_date = gene.create_date
    gene.write_date = gene.write_date
    gene.create_uid = gene.create_uid
    gene.write_uid = gene.write_uid

    gene.save()
    genes = gnuhealth_disease_gene.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect('genes')


def deleteGenes(request, id):
    gene = gnuhealth_disease_gene.objects.get(id=id)
    gene.delete()
    type = "grid"
    genes = gnuhealth_disease_gene.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect('genes')


def addGenes(request):
    if request.method == "POST":
        form = genesForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                msg = "1"
                latest = gnuhealth_disease_gene.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                genes = gnuhealth_disease_gene.objects.all()
                messages.success(request, f'Success, Record Saved Successfully')
                return redirect('genes')
            except:
                pass
        else:
            messages.warning(request, f'Sorry, Record Save Error - Invalid Fields')
            return redirect(addGenes)
    else:
        form = genesForm()
        latest = gnuhealth_disease_gene.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = False
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'health_configuration/genetics/genes.html', {'type': type, 'form': form, 'selected': 'Disease Genes'})

def phenotypes(request):
    type = "grid"
    phenotypes = gnuhealth_gene_variant_phenotype.objects.order_by('-id')[:200]
    return render(request, 'health_configuration/genetics/phenotype.html'
                  , {'phenotypes': phenotypes
                      , 'type': type, 'selected': 'Variant Phenotype'})


def addPhenotype(request):
    if request.method == "POST":
        form = phenotypeForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                msg = "1"
                latest = gnuhealth_gene_variant_phenotype.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                phenotypes = gnuhealth_gene_variant_phenotype.objects.all()
                messages.success(request, f'Success, Record Saved Successfully')
                return render(request, 'health_configuration/genetics/phenotype.html'
                              , {'type': type, 'msg': msg, 'phenotypes': phenotypes, 'selected': 'Variant Phenotype'})
            except:
                pass
        else:
            messages.warning(request, f'Sorry, Record Save Error - Invalid Fields')
            return redirect(addPhenotype)
    else:
        form = phenotypeForm()
        latest = gnuhealth_gene_variant_phenotype.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = True
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'health_configuration/genetics/phenotype.html', {'type': type, 'form': form, 'selected': 'Variant Phenotype'})


def editPhenotype(request, id):
    type = "edit"
    editForm = gnuhealth_gene_variant_phenotype.objects.get(id=id)
    return render(request, 'health_configuration/genetics/phenotype.html', {'form': editForm, 'type': type, 'selected': 'Variant Phenotype'})


def updatePhenotype(request, id):
    type = "grid"
    eth = gnuhealth_gene_variant_phenotype.objects.get(id=id)
    name = request.POST['name']
    variant = request.POST['variant']
    phenotype = request.POST['phenotype']
    eth_id = eth.id
    create_date = eth.create_date
    write_date = eth.write_date
    create_uid = eth.create_uid
    write_uid = eth.write_uid
    eth = gnuhealth_gene_variant_phenotype(id=eth_id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid, name=name, variant=variant, phenotype=phenotype)
    eth.save()
    msg = "3"
    phenotypes = gnuhealth_gene_variant_phenotype.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return render(request, 'health_configuration/genetics/phenotype.html'
                  , {'type': type, 'msg': msg, 'phenotypes': phenotypes, 'selected': 'Variant Phenotype'})


def deletePhenotype(request, id):
    phenotype = gnuhealth_gene_variant_phenotype.objects.get(id=id)
    phenotype.delete()
    type = "grid"
    msg = "2"
    phenotypes = gnuhealth_gene_variant_phenotype.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health_configuration/genetics/phenotype.html'
                  , {'type': type, 'msg': msg, 'phenotypes': phenotypes, 'selected': 'Variant Phenotype'})

def proteins(request):
    type = "grid"
    proteins = gnuhealth_protein_disease.objects.order_by('-id')[:200]
    return render(request, 'health_configuration/genetics/proteins.html'
                  , {'proteins': proteins
                      , 'type': type, 'selected': 'Protein Related Diseases'})


def addProtein(request):
    if request.method == "POST":
        form = proteinForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                msg = "1"
                latest = gnuhealth_protein_disease.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                proteins = gnuhealth_protein_disease.objects.all()
                messages.success(request, f'Success, Record Saved Successfully')
                return render(request, 'health_configuration/genetics/proteins.html'
                              , {'type': type, 'msg': msg, 'proteins': proteins, 'selected': 'Protein Related Diseases'})
            except:
                pass
        else:
            messages.warning(request, f'Sorry, Record Save Error - Invalid Fields')
            return redirect(addProtein)
    else:
        form = proteinForm()
        latest = gnuhealth_protein_disease.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = True
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'health_configuration/genetics/proteins.html', {'type': type, 'form': form, 'selected': 'Protein Related Diseases'})


def editProtein(request, id):
    type = "edit"
    editForm = gnuhealth_protein_disease.objects.get(id=id)
    return render(request, 'health_configuration/genetics/proteins.html', {'form': editForm, 'type': type, 'selected': 'Protein Related Diseases'})


def updateProtein(request, id):
    type = "grid"
    eth = gnuhealth_protein_disease.objects.get(id=id)
    name = request.POST['name']
    disease_name = request.POST['disease_name']
    acronym = request.POST['acronym']
    description = request.POST['description']
    dominance = request.POST['dominance']
    mim_reference = request.POST['mim_reference']
    eth_id = eth.id
    create_date = eth.create_date
    write_date = eth.write_date
    create_uid = eth.create_uid
    write_uid = eth.write_uid
    eth = gnuhealth_protein_disease(id=eth_id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid, name=name, disease_name=disease_name, acronym=acronym, description=description, dominance=dominance, mim_reference=mim_reference)
    eth.save()
    msg = "3"
    proteins = gnuhealth_protein_disease.objects.order_by('-id')[:200]

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return render(request, 'health_configuration/genetics/proteins.html'
                  , {'type': type, 'msg': msg, 'proteins': proteins, 'selected': 'Protein Related Diseases'})


def deleteProtein(request, id):
    protein = gnuhealth_protein_disease.objects.get(id=id)
    protein.delete()
    type = "grid"
    msg = "2"
    proteins = gnuhealth_protein_disease.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health_configuration/genetics/proteins.html'
                  , {'type': type, 'msg': msg, 'proteins': proteins, 'selected': 'Protein Related Diseases'})

def searchVarient(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''

    varients = gnuhealth_gene_variant.objects.filter(name__startswith=search_text.capitalize())

    if len(varients) == 0:
        varients = gnuhealth_gene_variant.objects.filter(id=search_text)

    return render_to_response('health_configuration/js/ajax-search.html', {'varients': varients})

def searchPhenotype(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''

    phenotypes = gnuhealth_gene_variant_phenotype.objects.filter(name__startswith=search_text.capitalize())

    if len(phenotypes) == 0:
        phenotypes = gnuhealth_gene_variant_phenotype.objects.filter(id=search_text)

    return render_to_response('health_configuration/js/ajax-search.html', {'phenotypes': phenotypes})


def varients(request):
    type = "grid"
    varients = gnuhealth_gene_variant.objects.order_by('-id')[:200]
    return render(request, 'health_configuration/genetics/varient.html', {'type': type, 'varients': varients, 'selected': 'Natural Variants'})


def editVarient(request, id):
    type = "edit"
    editForm = gnuhealth_gene_variant.objects.get(id=id)
    return render(request, 'health_configuration/genetics/varient.html', {'form': editForm, 'type': type, 'selected': 'Natural Variants'})


def updateVarient(request, id):
    type = "grid"
    varient = gnuhealth_gene_variant.objects.get(id=id)
    varient.name = request.POST['name']
    varient.aa_change = request.POST['aa_change']
    varient.protein_name = request.POST['varient']

    varient.id = id
    varient.create_date = varient.create_date
    varient.write_date = varient.write_date
    varient.create_uid = varient.create_uid
    varient.write_uid = varient.write_uid

    varient.save()
    varients = gnuhealth_gene_variant.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect('genes')


def deleteVarient(request, id):
    varient = gnuhealth_gene_variant.objects.get(id=id)
    varient.delete()
    type = "grid"
    varients = gnuhealth_gene_variant.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect('varients')


def addVarient(request):
    if request.method == "POST":
        form = varientForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                msg = "1"
                latest = gnuhealth_gene_variant.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                genes = gnuhealth_gene_variant.objects.all()
                messages.success(request, f'Success, Record Saved Successfully')
                return redirect('genes')
            except:
                pass
        else:
            messages.warning(request, f'Sorry, Record Save Error - Invalid Fields')
            return redirect(addVarient)
    else:
        form = varientForm()
        latest = gnuhealth_gene_variant.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = False
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'health_configuration/genetics/varient.html', {'type': type, 'form': form, 'selected': 'Natural Variants'})


def pathologyGroups(request):
    type = "grid"
    tempPathologyGroups = gnuhealth_pathology_group.objects.all()
    return render(request, 'health_configuration/conditions/pathology_groups.html',
                  {'type': type, 'tempPathologyGroups': tempPathologyGroups, 'selected': 'Pathology Groups'})


def addPathologyGroups(request):
    if request.method == "POST":
        form = pathologyGroupsForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                latest = gnuhealth_pathology_group.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                messages.success(request, f'Success, Record Saved Successfully')
                return redirect('pathologyGroups')
            except:
                pass
        else:
            messages.warning(request, f'Sorry, Record Save Error - Invalid Fields')
            return redirect(addPathologyGroups)
    else:
        form = pathologyGroupsForm()
        latest = gnuhealth_pathology_group.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = False
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'health_configuration/conditions/pathology_groups.html', {'type': type, 'form': form, 'selected': 'Pathology Groups'})


def editPathologyGroups(request, id):
    type = "edit"
    editForm = gnuhealth_pathology_group.objects.get(id=id)
    return render(request, 'health_configuration/conditions/pathology_groups.html', {'form': editForm, 'type': type, 'selected': 'Pathology Groups'})


def updatePathologyGroups(request, id):
    temp = gnuhealth_pathology_group.objects.get(id=id)
    temp.code = request.POST['code']
    temp.desc = request.POST['desc']
    temp.info = request.POST['info']
    temp.name = request.POST['name']

    temp.id = id
    temp.create_date = temp.create_date
    temp.write_date = temp.write_date
    temp.create_uid = temp.create_uid
    temp.write_uid = temp.write_uid

    temp.save()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect('pathologyGroups')


def deletePathologyGroups(request, id):
    temp = gnuhealth_pathology_group.objects.get(id=id)
    temp.delete()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect('pathologyGroups')


def categories(request):
    type = "grid"
    tempCategories = gnuhealth_pathology_category.objects.all()
    return render(request, 'health_configuration/conditions/categories.html',
                  {'type': type, 'tempCategories': tempCategories, 'selected': 'Categories'})


def addCategories(request):
    if request.method == "POST":
        form = categoriesForm(request.POST)
        if form.is_valid():
            try:
                latest = gnuhealth_pathology_category.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                messages.success(request, f'Success, Record Saved Successfully')
                return redirect('categories')
            except:
                pass
        else:
            messages.warning(request, f'Sorry, Record Save Error - Invalid Fields')
            return redirect(addCategories)
    else:
        form = categoriesForm()
        latest = gnuhealth_pathology_category.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = False
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'health_configuration/conditions/categories.html', {'type': type, 'form': form, 'selected': 'Categories'})


def editCategories(request, id):
    type = "edit"
    editForm = gnuhealth_pathology_category.objects.get(id=id)
    return render(request, 'health_configuration/conditions/categories.html', {'form': editForm, 'type': type, 'selected': 'Categories'})


def updateCategories(request, id):
    temp = gnuhealth_pathology_category.objects.get(id=id)
    temp.name = request.POST['name']

    temp.id = id
    temp.create_date = temp.create_date
    temp.write_date = temp.write_date
    temp.create_uid = temp.create_uid
    temp.write_uid = temp.write_uid

    temp.save()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect('categories')


def deleteCategories(request, id):
    temp = gnuhealth_pathology_category.objects.get(id=id)
    temp.delete()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect('categories')


def bodyFunctions(request):
    type = "grid"
    tempBodyFunctions = gnuhealth_body_function.objects.all()
    return render(request, 'health_configuration/functionality_disability/body_functions.html',
                  {'type': type, 'tempBodyFunctions': tempBodyFunctions, 'selected': 'Body Functions'})


def addBodyFunctions(request):
    if request.method == "POST":
        form = bodyFunctionsForm(request.POST)
        if form.is_valid():
            try:
                latest = gnuhealth_body_function.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                messages.success(request, f'Success, Record Saved Successfully')
                return redirect('bodyFunctions')
            except:
                pass
        else:
            messages.warning(request, f'Sorry, Record Save Error - Invalid Fields')
            return redirect(addBodyFunctions)
    else:
        form = bodyFunctionsForm()
        latest = gnuhealth_body_function.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = False
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'health_configuration/functionality_disability/body_functions.html',
                      {'type': type, 'form': form, 'selected': 'Body Functions'})


def editBodyFunctions(request, id):
    type = "edit"
    editForm = gnuhealth_body_function.objects.get(id=id)
    return render(request, 'health_configuration/functionality_disability/body_functions.html',
                  {'form': editForm, 'type': type, 'selected': 'Body Functions'})


def updateBodyFunctions(request, id):
    temp = gnuhealth_body_function.objects.get(id=id)
    temp.name = request.POST['name']
    temp.code = request.POST['code']

    temp.id = id
    temp.create_date = temp.create_date
    temp.write_date = temp.write_date
    temp.create_uid = temp.create_uid
    temp.write_uid = temp.write_uid

    temp.save()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect('bodyFunctions')


def deleteBodyFunctions(request, id):
    temp = gnuhealth_body_function.objects.get(id=id)
    temp.delete()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect('bodyFunctions')


def bodyStructures(request):
    type = "grid"
    tempBodyStructures = gnuhealth_body_structure.objects.all()
    return render(request, 'health_configuration/functionality_disability/body_structures.html',
                  {'type': type, 'tempBodyStructures': tempBodyStructures, 'selected': 'Body Structures'})


def addBodyStructures(request):
    if request.method == "POST":
        form = bodyStructuresForm(request.POST)
        if form.is_valid():
            try:
                latest = gnuhealth_body_structure.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                messages.success(request, f'Success, Record Saved Successfully')
                return redirect('bodyStructures')
            except:
                pass
        else:
            messages.warning(request, f'Sorry, Record Save Error - Invalid Fields')
            return redirect('bodyStructures')
    else:
        form = bodyStructuresForm()
        latest = gnuhealth_body_structure.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = False
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'health_configuration/functionality_disability/body_structures.html',
                      {'type': type, 'form': form, 'selected': 'Body Structures'})


def editBodyStructures(request, id):
    type = "edit"
    editForm = gnuhealth_body_structure.objects.get(id=id)
    return render(request, 'health_configuration/functionality_disability/body_structures.html',
                  {'form': editForm, 'type': type, 'selected': 'Body Structures'})


def updateBodyStructures(request, id):
    temp = gnuhealth_body_structure.objects.get(id=id)
    temp.name = request.POST['name']
    temp.code = request.POST['code']

    temp.id = id
    temp.create_date = temp.create_date
    temp.write_date = temp.write_date
    temp.create_uid = temp.create_uid
    temp.write_uid = temp.write_uid

    temp.save()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect('bodyStructures')


def deleteBodyStructures(request, id):
    temp = gnuhealth_body_structure.objects.get(id=id)
    temp.delete()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect('bodyStructures')


def activityParticipation(request):
    type = "grid"
    tempActivityParticipation = gnuhealth_activity_and_participation.objects.all()
    return render(request, 'health_configuration/functionality_disability/activity_patricipation.html',
                  {'type': type, 'tempActivityParticipation': tempActivityParticipation, 'selected': 'Activities and Participtions'})


def addActivityParticipation(request):
    if request.method == "POST":
        form = activityParticipationForm(request.POST)
        if form.is_valid():
            try:
                latest = gnuhealth_activity_and_participation.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                messages.success(request, f'Success, Record Saved Successfully')
                return redirect(addActivityParticipation)
            except:
                pass
        else:
            messages.warning(request, f'Sorry, Record Save Error - Invalid Fields')
            return redirect('activityParticipation')
    else:
        form = activityParticipationForm()
        latest = gnuhealth_activity_and_participation.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = False
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'health_configuration/functionality_disability/activity_patricipation.html',
                      {'type': type, 'form': form, 'selected': 'Activities and Participtions'})


def editActivityParticipation(request, id):
    type = "edit"
    editForm = gnuhealth_activity_and_participation.objects.get(id=id)
    return render(request, 'health_configuration/functionality_disability/activity_patricipation.html',
                  {'form': editForm, 'type': type, 'selected': 'Activities and Participtions'})


def updateActivityParticipation(request, id):
    temp = gnuhealth_activity_and_participation.objects.get(id=id)
    temp.name = request.POST['name']
    temp.code = request.POST['code']

    temp.id = id
    temp.create_date = temp.create_date
    temp.write_date = temp.write_date
    temp.create_uid = temp.create_uid
    temp.write_uid = temp.write_uid

    temp.save()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect('activityParticipation')


def deleteActivityParticipation(request, id):
    temp = gnuhealth_activity_and_participation.objects.get(id=id)
    temp.delete()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect('activityParticipation')


def environmentalFactor(request):
    type = "grid"
    tempEnvironmentalFactor = gnuhealth_environmental_factor.objects.all()
    return render(request, 'health_configuration/functionality_disability/environmental_factor.html',
                  {'type': type, 'tempEnvironmentalFactor': tempEnvironmentalFactor, 'selected': 'Environmental Factors'})


def addEnvironmentalFactor(request):
    if request.method == "POST":
        form = environmentalFactorForm(request.POST)
        if form.is_valid():
            try:
                latest = gnuhealth_environmental_factor.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                messages.success(request, f'Success, Record Saved Successfully')
                return redirect(addEnvironmentalFactor)
            except:
                pass
        else:
            messages.warning(request, f'Sorry, Record Save Error - Invalid Fields')
            return redirect('environmentalFactor')
    else:
        form = environmentalFactorForm()
        latest = gnuhealth_environmental_factor.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = False
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'health_configuration/functionality_disability/environmental_factor.html',
                      {'type': type, 'form': form, 'selected': 'Environmental Factors'})


def editEnvironmentalFactor(request, id):
    type = "edit"
    editForm = gnuhealth_environmental_factor.objects.get(id=id)
    return render(request, 'health_configuration/functionality_disability/environmental_factor.html',
                  {'form': editForm, 'type': type, 'selected': 'Environmental Factors'})


def updateEnvironmentalFactor(request, id):
    temp = gnuhealth_environmental_factor.objects.get(id=id)
    temp.name = request.POST['name']
    temp.code = request.POST['code']

    temp.id = id
    temp.create_date = temp.create_date
    temp.write_date = temp.write_date
    temp.create_uid = temp.create_uid
    temp.write_uid = temp.write_uid

    temp.save()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect('environmentalFactor')


def deleteEnvironmentalFactor(request, id):
    temp = gnuhealth_environmental_factor.objects.get(id=id)
    temp.delete()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect('environmentalFactor')


def dietBelief(request):
    type = "grid"
    tempDietBelief = gnuhealth_diet_belief.objects.all()
    return render(request, 'health_configuration/misc/diet_belief.html',
                  {'type': type, 'tempDietBelief': tempDietBelief, 'selected': 'Diet Beliefs'})


def addDietBelief(request):
    if request.method == "POST":
        form = dietBeliefForm(request.POST)
        if form.is_valid():
            try:
                latest = gnuhealth_diet_belief.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                messages.success(request, f'Success, Record Saved Successfully')
                return redirect(dietBelief)
            except:
                pass
        else:
            messages.warning(request, f'Sorry, Record Save Error - Invalid Fields')
            return redirect(addDietBelief)
    else:
        form = dietBeliefForm()
        latest = gnuhealth_diet_belief.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = False
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'health_configuration/misc/diet_belief.html', {'type': type, 'form': form, 'selected': 'Diet Beliefs'})


def editDietBelief(request, id):
    type = "edit"
    editForm = gnuhealth_diet_belief.objects.get(id=id)
    return render(request, 'health_configuration/misc/diet_belief.html', {'form': editForm, 'type': type, 'selected': 'Diet Beliefs'})


def updateDietBelief(request, id):
    temp = gnuhealth_diet_belief.objects.get(id=id)
    temp.name = request.POST['name']
    temp.code = request.POST['code']
    temp.description = request.POST['description']

    temp.id = id
    temp.create_date = temp.create_date
    temp.write_date = temp.write_date
    temp.create_uid = temp.create_uid
    temp.write_uid = temp.write_uid

    temp.save()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect('dietBelief')


def deleteDietBelief(request, id):
    temp = gnuhealth_diet_belief.objects.get(id=id)
    temp.delete()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect('dietBelief')


def dietTherapeutic(request):
    type = "grid"
    tempDietTherapeutic = gnuhealth_diet_therapeutic.objects.all()
    return render(request, 'health_configuration/misc/diet_therapeutic.html',
                  {'type': type, 'tempDietTherapeutic': tempDietTherapeutic, 'selected': 'Therapeutic Diets'})


def addDietTherapeutic(request):
    if request.method == "POST":
        form = dietTherapeuticForm(request.POST)
        if form.is_valid():
            try:
                latest = gnuhealth_diet_therapeutic.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                messages.success(request, f'Success, Record Saved Successfully')
                return redirect(dietTherapeutic)
            except:
                pass
        else:
            messages.warning(request, f'Sorry, Record Save Error - Invalid Fields')
            return redirect(addDietTherapeutic)
    else:
        form = dietTherapeuticForm()
        latest = gnuhealth_diet_therapeutic.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = False
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'health_configuration/misc/diet_therapeutic.html', {'type': type, 'form': form, 'selected': 'Therapeutic Diets'})


def editDietTherapeutic(request, id):
    type = "edit"
    editForm = gnuhealth_diet_therapeutic.objects.get(id=id)
    return render(request, 'health_configuration/misc/diet_therapeutic.html', {'form': editForm, 'type': type, 'selected': 'Therapeutic Diets'})


def updateDietTherapeutic(request, id):
    temp = gnuhealth_diet_therapeutic.objects.get(id=id)
    temp.name = request.POST['name']
    temp.code = request.POST['code']
    temp.description = request.POST['description']

    temp.id = id
    temp.create_date = temp.create_date
    temp.write_date = temp.write_date
    temp.create_uid = temp.create_uid
    temp.write_uid = temp.write_uid

    temp.save()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect('dietTherapeutic')


def deleteDietTherapeutic(request, id):
    temp = gnuhealth_diet_therapeutic.objects.get(id=id)
    temp.delete()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect('dietTherapeutic')


def pediatricsGrowthChart(request):
    type = "grid"
    tempPediatricsGrowthChart = gnuhealth_pediatrics_growth_charts_who.objects.all()
    return render(request, 'health_configuration/misc/pediatrics_growth_chart.html',
                  {'type': type, 'tempPediatricsGrowthChart': tempPediatricsGrowthChart})


def addPediatricsGrowthChart(request):
    if request.method == "POST":
        form = pediatricGrowthChartForm(request.POST)
        if form.is_valid():
            try:
                latest = gnuhealth_pediatrics_growth_charts_who.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                messages.success(request, f'Success, Record Saved Successfully')
                return redirect('pediatricsGrowthChart')
            except:
                pass
        else:
            messages.warning(request, f'Sorry, Record Save Error - Invalid Fields')
            return redirect(addPediatricsGrowthChart)
    else:
        form = pediatricGrowthChartForm()
        latest = gnuhealth_pediatrics_growth_charts_who.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = False
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'health_configuration/misc/pediatrics_growth_chart.html', {'type': type, 'form': form})


def editPediatricsGrowthChart(request, id):
    type = "edit"
    editForm = gnuhealth_pediatrics_growth_charts_who.objects.get(id=id)
    return render(request, 'health_configuration/misc/pediatrics_growth_chart.html', {'form': editForm, 'type': type})


def updatePediatricsGrowthChart(request, id):
    temp = gnuhealth_pediatrics_growth_charts_who.objects.get(id=id)
    temp.indicator = request.POST['indicator']
    temp.measure = request.POST['measure']
    temp.sex = request.POST['sex']
    temp.month = request.POST['month']
    temp.type = request.POST['type']
    temp.value = request.POST['value']

    temp.id = id
    temp.create_date = temp.create_date
    temp.write_date = temp.write_date
    temp.create_uid = temp.create_uid
    temp.write_uid = temp.write_uid

    temp.save()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect('pediatricsGrowthChart')


def deletePediatricsGrowthChart(request, id):
    temp = gnuhealth_pediatrics_growth_charts_who.objects.get(id=id)
    temp.delete()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect('pediatricsGrowthChart')


def procedures(request):
    type = "grid"
    procedures = gnuhealth_procedure.objects.all()
    return render(request, 'health_configuration/procedure/procedures.html'
                  , {'procedures': procedures
                      , 'type': type})


def addProcedure(request):
    if request.method == "POST":
        form = procedureForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                msg = "1"
                latest = gnuhealth_procedure.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                procedures = gnuhealth_procedure.objects.all()
                messages.success(request, f'Success, Record Saved Successfully')
                return render(request, 'health_configuration/procedure/procedures.html'
                              , {'type': type, 'msg': msg, 'procedures': procedures})
            except:
                pass
        else:
            messages.warning(request, f'Sorry, Record Save Error - Invalid Fields')
            return redirect(addProcedure)
    else:
        form = procedureForm()
        latest = gnuhealth_procedure.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = True
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'health_configuration/procedure/procedures.html', {'type': type, 'form': form})


# def editProcedure(request, id):
#   type = "edit"
#  editForm = gnuhealth_procedure.objects.get(id=id)
# return render(request, 'health_configuration/procedure/procedures.html', {'form': editForm, 'type': type})


# def updateProcedure(request, id):
#   type = "grid"
#   procedure = gnuhealth_procedure.objects.get(id=id)
#   name = request.POST['name']
#  description = request.POST['description']
# pro_id = procedure.id
# create_date = procedure.create_date
# write_date = procedure.write_date
# create_uid = procedure.create_uid
# write_uid = procedure.write_uid
# procedure = gnuhealth_operational_area(id=pro_id, create_date=create_date, write_date=write_date, create_uid=create_uid
#                          , write_uid=write_uid, name=name, description=description)
# procedure.save()
# msg = "3"
# procedures = gnuhealth_procedure.objects.all()

# if True:
#    messages.success(request, f'Success, Record Updated Successfully')
# elif False:
#   messages.error(request, f'Sorry, Record Update Error')


# return render(request, 'health_configuration/procedure/procedures.html'
#                  , {'type': type, 'msg': msg, 'procedures': procedures})


def deleteProcedure(request, id):
    procedure = gnuhealth_procedure.objects.get(id=id)
    procedure.delete()
    type = "grid"
    msg = "2"
    procedures = gnuhealth_procedure.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health_configuration/procedure/procedures.html'
                  , {'type': type, 'msg': msg, 'procedures': procedures})


def imagingTestTypes(request):
    type = "grid"
    types = gnuhealth_imaging_test_type.objects.all()
    return render(request, 'health_configuration/imaging/imaging_test_types.html'
                  , {'types': types
                      , 'type': type})


def addImagingTestType(request):
    if request.method == "POST":
        form = imagingTestTypeForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                msg = "1"
                latest = gnuhealth_imaging_test_type.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                types = gnuhealth_imaging_test_type.objects.all()
                messages.success(request, f'Success, Record Saved Successfully')
                return render(request, 'health_configuration/imaging/imaging_test_types.html'
                              , {'type': type, 'msg': msg, 'types': types})
            except:
                pass
        else:
            messages.warning(request, f'Sorry, Record Save Error - Invalid Fields')
            return redirect(addImagingTestType)
    else:
        form = imagingTestTypeForm()
        latest = gnuhealth_imaging_test_type.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = True
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'health_configuration/imaging/imaging_test_types.html', {'type': type, 'form': form})


def editImagingTestType(request, id):
    type = "edit"
    editForm = gnuhealth_imaging_test_type.objects.get(id=id)
    return render(request, 'health_configuration/imaging/imaging_test_types.html', {'form': editForm, 'type': type})


def updateImagingTestType(request, id):
    type = "grid"
    eth = gnuhealth_imaging_test_type.objects.get(id=id)
    name = request.POST['name']
    code = request.POST['code']
    eth_id = eth.id
    create_date = eth.create_date
    write_date = eth.write_date
    create_uid = eth.create_uid
    write_uid = eth.write_uid
    eth = gnuhealth_imaging_test_type(id=eth_id, create_date=create_date, write_date=write_date, create_uid=create_uid
                                      , write_uid=write_uid, name=name, code=code)
    eth.save()
    msg = "3"
    types = gnuhealth_imaging_test_type.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return render(request, 'health_configuration/imaging/imaging_test_types.html'
                  , {'type': type, 'msg': msg, 'types': types})


def deleteImagingTestType(request, id):
    test = gnuhealth_imaging_test_type.objects.get(id=id)
    test.delete()
    type = "grid"
    msg = "2"
    types = gnuhealth_imaging_test_type.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health_configuration/imaging/imaging_test_types.html'
                  , {'type': type, 'msg': msg, 'types': types})


def specialities(request):
    type = "grid"
    specialities = gnuhealth_specialty.objects.all()
    return render(request, 'health_configuration/work_schedule/specialities.html'
                  , {'specialities': specialities
                      , 'type': type})


def addSpeciality(request):
    if request.method == "POST":
        form = specialityForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                msg = "1"
                latest = gnuhealth_specialty.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                specialities = gnuhealth_specialty.objects.all()
                messages.success(request, f'Success, Record Saved Successfully')
                return render(request, 'health_configuration/work_schedule/specialities.html'
                              , {'type': type, 'msg': msg, 'specialities': specialities})
            except:
                pass
        else:
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = specialityForm()
        latest = gnuhealth_specialty.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = True
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'health_configuration/work_schedule/specialities.html', {'type': type, 'form': form})


def editSpeciality(request, id):
    type = "edit"
    editForm = gnuhealth_specialty.objects.get(id=id)
    return render(request, 'health_configuration/work_schedule/specialities.html', {'form': editForm, 'type': type})


def updateSpeciality(request, id):
    type = "grid"
    eth = gnuhealth_specialty.objects.get(id=id)
    name = request.POST['name']
    notes = request.POST['notes']
    code = request.POST['code']
    eth_id = eth.id
    create_date = eth.create_date
    write_date = eth.write_date
    create_uid = eth.create_uid
    write_uid = eth.write_uid
    eth = gnuhealth_specialty(id=eth_id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid, name=name, code=code)
    eth.save()
    msg = "3"
    specialities = gnuhealth_specialty.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return render(request, 'health_configuration/work_schedule/specialities.html'
                  , {'type': type, 'msg': msg, 'specialities': specialities})


def deleteSpeciality(request, id):
    speciality = gnuhealth_specialty.objects.get(id=id)
    speciality.delete()
    type = "grid"
    msg = "2"
    specialities = gnuhealth_specialty.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health_configuration/work_schedule/specialities.html'
                  , {'type': type, 'msg': msg, 'specialities': specialities})


def buildings(request):
    type = "grid"
    buildings = gnuhealth_hospital_building.objects.all()
    return render(request, 'health_configuration/work_schedule/buildings.html'
                  , {'buildings': buildings
                      , 'type': type})


def addBuilding(request):
    if request.method == "POST":
        form = specialityForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                msg = "1"
                latest = gnuhealth_hospital_building.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                specialities = gnuhealth_hospital_building.objects.all()
                messages.success(request, f'Success, Record Saved Successfully')
                return render(request, 'health_configuration/work_schedule/specialities.html'
                              , {'type': type, 'msg': msg, 'specialities': specialities})
            except:
                pass
        else:
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = specialityForm()
        latest = gnuhealth_hospital_building.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = True
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'health_configuration/work_schedule/specialities.html', {'type': type, 'form': form})


def editBuilding(request, id):
    type = "edit"
    editForm = gnuhealth_hospital_building.objects.get(id=id)
    return render(request, 'health_configuration/work_schedule/specialities.html', {'form': editForm, 'type': type})


def updateBuilding(request, id):
    type = "grid"
    eth = gnuhealth_hospital_building.objects.get(id=id)
    name = request.POST['name']
    code = request.POST['code']
    eth_id = eth.id
    create_date = eth.create_date
    write_date = eth.write_date
    create_uid = eth.create_uid
    write_uid = eth.write_uid
    eth = gnuhealth_hospital_building(id=eth_id, create_date=create_date, write_date=write_date, create_uid=create_uid
                                      , write_uid=write_uid, name=name, code=code)
    eth.save()
    msg = "3"
    buildings = gnuhealth_hospital_building.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return render(request, 'health_configuration/institutions/buildings.html'
                  , {'type': type, 'msg': msg, 'buildings': buildings})


def deleteBuilding(request, id):
    building = gnuhealth_hospital_building.objects.get(id=id)
    building.delete()
    type = "grid"
    msg = "2"
    buildings = gnuhealth_hospital_building.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health_configuration/institutions/bulidings.html'
                  , {'type': type, 'msg': msg, 'buildings': buildings})


def country(request):
    type = "grid"
    countries = country_country.objects.all()
    return render(request, 'health_configuration/demographics/countries.html'
                  , {'countries': countries
                      , 'type': type})


def addCountry(request):
    if request.method == "POST":
        form = countryForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                msg = "1"
                latest = country_country.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                countries = country_country.objects.all()
                messages.success(request, f'Success, Record Saved Successfully')
                return render(request, 'health_configuration/demographics/countries.html'
                              , {'type': type, 'msg': msg, 'countries': countries})
            except:
                pass
        else:
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = countryForm()
        latest = country_country.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = True
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'health_configuration/demographics/countries.html', {'type': type, 'form': form})


def editCountry(request, id):
    type = "edit"
    editForm = country_country.objects.get(id=id)
    return render(request, 'health_configuration/demographics/countries.html', {'form': editForm, 'type': type})


def updateCountry(request, id):
    type = "grid"
    eth = country_country.objects.get(id=id)
    name = request.POST['name']
    code3 = eth.code3
    code = request.POST['code']
    code_numeric = eth.code_numeric
    eth_id = eth.id
    create_date = eth.create_date
    write_date = eth.write_date
    create_uid = eth.create_uid
    write_uid = eth.write_uid
    eth = country_country(id=eth_id, create_date=create_date, write_date=write_date, create_uid=create_uid
                          , write_uid=write_uid, name=name, code3=code3, code=code, code_numeric=code_numeric)
    eth.save()
    msg = "3"
    countries = country_country.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return render(request, 'health_configuration/demographics/countries.html'
                  , {'type': type, 'msg': msg, 'countries': countries})


def deleteCountry(request, id):
    country = country_country.objects.get(id=id)
    country.delete()
    type = "grid"
    msg = "2"
    countries = country_country.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health_configuration/demographics/countries.html'
                  , {'type': type, 'msg': msg, 'countries': countries})


def subdivisions(request):
    type = "grid"
    divisions = country_subdivision.objects.all()
    return render(request, 'health_configuration/demographics/sub_divisions.html'
                  , {'divisions': divisions
                      , 'type': type})


def addSubdivision(request):
    if request.method == "POST":
        form = subdivisionForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                msg = "1"
                latest = country_subdivision.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                divisions = country_subdivision.objects.all()
                messages.success(request, f'Success, Record Saved Successfully')
                return render(request, 'health_configuration/demographics/sub_divisions.html'
                              , {'type': type, 'msg': msg, 'divisions': divisions})
            except:
                pass
        else:
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = subdivisionForm()
        latest = country_subdivision.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = True
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'health_configuration/demographics/sub_divisions.html'
                      , {'type': type, 'form': form})


def editSubdivision(request, id):
    type = "edit"
    editForm = country_subdivision.objects.get(id=id)
    return render_to_response('health_configuration/demographics/sub_divisions.html', {'form': editForm, 'type': type})


@csrf_exempt
def updateSubdivision(request, id):
    type = "grid"
    eth = country_subdivision.objects.get(id=id)
    name = request.POST['name']
    type = request.POST['type']
    code = request.POST['code']
    parent = request.POST['parent']
    country = request.POST['country']
    eth_id = eth.id
    create_date = eth.create_date
    write_date = eth.write_date
    create_uid = eth.create_uid
    write_uid = eth.write_uid
    eth = country_subdivision(id=eth_id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid, name=name, code=code, country=country, type=type, parent=parent)
    eth.save()
    msg = "3"
    divisions = country_subdivision.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return render_to_response(request, 'health_configuration/demographics/sub_divisions.html'
                  , {'type': type, 'msg': msg, 'divisions': divisions})


def deleteSubdivision(request, id):
    division = country_subdivision.objects.get(id=id)
    division.delete()
    type = "grid"
    msg = "2"
    divisions = country_subdivision.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health_configuration/demographics/sub_divisions.html'
                  , {'type': type, 'msg': msg, 'divisions': divisions})


def searchCountry(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''

    countries = country_country.objects.filter(name__startswith=search_text.capitalize())

    if len(countries) == 0:
        countries = country_country.objects.filter(id=search_text)

    return render_to_response('health_configuration/js/ajax-search.html', {'countries': countries})
