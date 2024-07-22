
# Envío de mails
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages



# Create your views here.


def index(request):
    return render(request, 'index.html')
# Filtro de los mensajes que se enviarán.
# Extracción Aquí debo traer mis datos de mi excel
def contact(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
# Transformación
        template = render_to_string('email-template.html', {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        })
# Carga
        emailSender = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            # ACA VA EL CORREO O LA LISTA DE CORREOS A LOS QUE QUIERO ENVIAR ESTE EMAIL. PUEDE SER UNO O TANTOS COMO LOS QUE DESEE
            # SI ES UNO SOLO, COLOCO EL CORREO UNICO ENTRE COMILLAS SIMPLES Y NADA MAS. SI AGREGO MÁS TENGO QUE SEPARARLOS CON UNA COMA ','
            ['edwvazmor@gmail.com'] # aqui deben estar mis mails a enviar. Además noto que también envía un mail al mail del campo "email", o sea que tiene dos formas de enviar, una es poniendo mails dentro de estos corchetes y ademas envía al mail del "email". Yo probablemente deba usar lo de poner en los corchetes
        )
        emailSender.content_subtype = 'html'
        emailSender.fail_silently = False
        emailSender.send()

        messages.success(request, 'El correo electrónico se envió correctamente')
        return redirect('index')
    

# Pruebas o tareas a ir haciendo o cosas a agregar
# Traer datos en un dataframe: fijarse en como se hizo en WORD & PDF AUTOMATE se hizo esa eso parte.
# Ver si hay una forma de filtrarlos antes de extraerlos para que no procese datos innecesarios.
#
#
#
#
#
#
