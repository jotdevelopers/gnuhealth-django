from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, "health_dashboard/index.html")

def coming_soon(request):
	return render(request, "health_dashboard/coming-soon.html")

#Dashboard

def visitHistory(request):
    return render(request, 'health_dashboard/visitHistory.html'  )

def patientVisits(request):
    return render(request, 'health_dashboard/patientVisits.html'  )

def patientHistory(request):
    return render(request, 'health_dashboard/patientHistory.html'  )

def patientTests(request):
    return render(request, 'health_dashboard/patientTests.html'  )

def nationOne(request):
    return render(request, 'health_dashboard/Nation_Eg_1/index.html', {'selected': 'Procedure Success'})

def d1(request):
	return render(request, 'health_dashboard/Nation_Eg_1/d3.v3.min.js')

def n1(request):
	return render(request, 'health_dashboard/Nation_Eg_1/nations.json')

def c1(request):
	return render(request, 'health_dashboard/Nation_Eg_1/style.css')

def nationTwo(request):
    return render(request, 'health_dashboard/Nation_Eg_2/index.html', {'selected': 'Drugs Usage'})

def d2(request):
	return render(request, 'health_dashboard/Nation_Eg_2/d3.v3.min.js')

def n2(request):
	return render(request, 'health_dashboard/Nation_Eg_2/nations.json')

def c2(request):
	return render(request, 'health_dashboard/Nation_Eg_2/style.css')

def nationThree(request):
    return render(request, 'health_dashboard/Nation_Eg_3/index.html', {'selected': 'Diseases Data'})

def d3(request):
	return render(request, 'health_dashboard/Nation_Eg_3/d3.v3.min.js')

def n3(request):
	return render(request, 'health_dashboard/Nation_Eg_3/nations.json')

def c3(request):
	return render(request, 'health_dashboard/Nation_Eg_3/style.css')

def nationFour(request):
    return render(request, 'health_dashboard/Nation_Eg_4/index.html', {'selected': 'Procedures & Usage'})

def d4(request):
	return render(request, 'health_dashboard/Nation_Eg_4/d3.v3.min.js')

def n4(request):
	return render(request, 'health_dashboard/Nation_Eg_4/nations.json')

def c4(request):
	return render(request, 'health_dashboard/Nation_Eg_4/style.css')

def sunOne(request):
	return render(request, 'health_dashboard/Sunburst_Eg_1/index.html', {'selected': 'Diseases Percentage'})

def sd1(request):
	return render(request, 'health_dashboard/Sunburst_Eg_1/sequences.css')

def sc1(request):
	return render(request, 'health_dashboard/Sunburst_Eg_1/sequences.js')

def sj1(request):
	return render(request, 'health_dashboard/Sunburst_Eg_1/visit-sequences.csv')

def sunTwo(request):
	return render(request, 'health_dashboard/Sunburst_Eg_2/index.html', {'selected': 'Hospital Infrastructure'})

def sd2(request):
	return render(request, 'health_dashboard/Sunburst_Eg_2/sequences.css')

def sc2(request):
	return render(request, 'health_dashboard/Sunburst_Eg_2/sequences.js')

def sj2(request):
	return render(request, 'health_dashboard/Sunburst_Eg_2/visit-sequences.csv')

def treeOne(request):
	return render(request, 'health_dashboard/Tree_Eg_1/index.html', {'selected': 'Diseases & Symptoms'})

def td1(request):
	return render(request, 'health_dashboard/Tree_Eg_1/dndTree.js')

def tc1(request):
	return render(request, 'health_dashboard/Tree_Eg_1/flare.json')

def treeTwo(request):
	return render(request, 'health_dashboard/Tree_Eg_2/index.html', {'selected': 'Patient Age Groups'})

def td2(request):
	return render(request, 'health_dashboard/Tree_Eg_2/dndTree.js')

def tc2(request):
	return render(request, 'health_dashboard/Tree_Eg_2/flare.json')

def treeThree(request):
	return render(request, 'health_dashboard/Tree_Eg_3/index.html', {'selected': 'Departments Data'})

def td3(request):
	return render(request, 'health_dashboard/Tree_Eg_3/dndTree.js')

def tc3(request):
	return render(request, 'health_dashboard/Tree_Eg_3/flare.json')

def treeFour(request):
	return render(request, 'health_dashboard/Tree_Eg_4/index.html', {'selected': 'Related Diseases'})

def td4(request):
	return render(request, 'health_dashboard/Tree_Eg_4/dndTree.js')

def tc4(request):
	return render(request, 'health_dashboard/Tree_Eg_4/flare.json')
