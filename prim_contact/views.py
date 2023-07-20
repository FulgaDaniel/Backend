from django.shortcuts import render
from django.http import HttpResponse

pagina_contacte="""
<h1> Acesta este un contact FICTIV</h1>
<p>Nume:Ion</p>
<p>Prenume:Ion</p>
<p>telefon:077777</p>
<p>adresa:Strada Gheorghe Pop de Basesti 19</p>
""".replace ("\n","").replace("  ", "")

    return HttpResponse(request, pagina_html)

