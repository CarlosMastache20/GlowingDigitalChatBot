import random
import re 

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
        
        message_certainty = 0
        has_required_words = True

        for word in user_message:
            if word in recognized_words:
                message_certainty +=1

        percentage = float(message_certainty) / float(len(recognized_words))

        for word in required_word:
            if word not in user_message:
                has_required_words = False
                break
        if has_required_words or single_response:
            return int(percentage*100)
        else:
            return 0



def check_all_messages(message):
      
            highest_prob = {}

            def response(bot_response, list_of_words, single_response=False, required_words = [] ):
                nonlocal highest_prob
                highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

            response('Hola, Buen día. Escribe tu pregunta o duda y tratare de responderte lo mas rapido posible.' ,['hola', 'hoa' 'saludos', 'saludos', 'buenas', 'buen', 'dia', 'buenos' , 'dias' , 'días' ,  'tal',  'noches', 'tardes', 'Hola', 'Buenos dias' , 'Buenas' , 'Dias' , 'Tardes'], single_response=True)

            response('¿Cómo deseas recibir información? 💡  <br> <br> 	<button class="btn btn-primary"  onclick="getUserResponse3()" value="Por escrito" id="Send3" style="font-size: 14px;" >Por escrito <i class="fa-solid fa-file-lines"></i> </button>  	<button class="btn btn-success" style="font-size: 14px;" onclick="getUserResponse4()" value="Un video" id="Send4" > Un video <i class="fa-sharp fa-solid fa-circle-play"></i>   </button>',['uno'], single_response=True)
            
            response('Muy bien, me podrías ayudar rellenando el formulario del siguiente link <a href="/blog/contacto" class="nav-link">Click aqui</a> para contactarnos contigo mas tarde',['dos'], single_response=True)
            
            response('Te comento que nosotros somos una empresa dedicada a medición de la interacción de distintos temas como son autos, moda, viajes, maquillaje, etc. Trabajando de la mano del área publicitaria de Facebook logramos estas mediciones. En conclusión nosotros usaremos tu perfil para crear una pagina en la cual se publicara contenido de los temas antes mencionados para ver la reacción de la gente. Nos encanta aclarar que tu perfil es totalmente respetado así como jamas usamos tus datos personales para otros fines. <br> <button class="btn btn-primary" style="font-size: 12px;" onclick="getUserResponse5()" id="Send5" value="continuar leyendo"> Continuar leyendo  </button> <button class="btn btn-success" style="font-size: 12px;" onclick="getUserResponse4()" value="Ver video" id="Send4" > Un video <i class="fa-sharp fa-solid fa-circle-play"></i>   </button>' ,['tres'], single_response=True)

            

            response('¿Qué tal te pareció el video? ¿Deseas iniciar? <br> <a class="btn btn-primary"  href="https://wa.me/qr/7DKX6GUPVUWSF1"" target="_blank" style="font-size: 14px;" >Si <i class="fa fa-check" aria-hidden="true"></i> </a>  	<a class="btn btn-warning" style="font-size: 14px;"  href="https://wa.me/qr/RFADP5HZ7RLND1"" target="_blank" >Tengo dudas <i class="fa-solid fa-question"></i>  </a>',['cuatro'], single_response=True)

            response('Los requerimientos que pedimos para que tu puedas comenzar a tener un ingreso extra constante con nosotros son muy pocos: <br> º Contar con un perfil de Facebook real (nombre real) y que sea activo. <br>º Tener al menos 6 meses de antigüedad con tu perfil. <br> º Que la cuenta por ingresar no esté o haya colaborado con otra empresa en una colaboración similar. <br>Te recordamos que al colaborar con nosotros no tienes que invertir un solo peso. <br> <button class="btn btn-primary" style="font-size: 12px;" onclick="getUserResponse8()" id="Send8" value="continuar leyendo"> Continuar leyendo  </button>  <button class="btn btn-success" style="font-size: 12px;" onclick="getUserResponse4()" value="Ver video" id="Send4" > Un video <i class="fa-sharp fa-solid fa-circle-play"></i>   </button>' ,['cinco'], single_response=True)

            response('El colaborar con nosotros es super fácil. Ya que para generar tus primeros $2000 pesos solo tenemos que esperar a que Facebook nos apruebe tu pagina y tu perfil. Como nos regimos sobre las reglas y políticas de Facebook todo lo trabajamos a través del business manager. Que es la parte publicitaria de Facebook. Esto para que tu puedas seguir teniendo un uso normal de tu cuenta es super importante que tu cuenta tengas tus datos actualizados como numero y correo y tenga un nombre real.<br> <button class="btn btn-primary" style="font-size: 12px;" onclick="getUserResponse9()" id="Send9" value="continuar leyendo"> Continuar leyendo  </button>  <button class="btn btn-success" style="font-size: 12px;" onclick="getUserResponse4()" value="Ver video" id="Send4" > Un video <i class="fa-sharp fa-solid fa-circle-play"></i>   </button>',['ocho'], single_response=True)

            response('Le daremos seguimiento a todo tu proceso a través de un grupo de WhatsApp en el cual nos vas a compartir igual el método de pago en el cual deseas que te depositemos. <br> Tu única tarea para apoyarnos será compartir tu pagina entre amigos y familiares para que así la verificación sea mas sencilla <br> <p style="font-weight: bold;"> ¿Que tal te parecio la información? ¿Deseas iniciar? </p> <a class="btn btn-primary"  href="https://wa.me/qr/7DKX6GUPVUWSF1"" target="_blank"  style="font-size: 14px;" >Si <i class="fa fa-check" aria-hidden="true"></i> </a>  	<a class="btn btn-warning" style="font-size: 14px;" href="https://wa.me/qr/RFADP5HZ7RLND1"" target="_blank" > Tengo dudas  <i class="fa-solid fa-question"></i>  </a>',['nueve'], single_response=True)


            response('Muy bien, me podrías ayudar con el formulario del siguiente link <a href="/blog/contacto" class="nav-link">Click aqui</a> para contactarnos contigo y dar inicio al proceso',['seis'], single_response=True)

            response('Muy bien, me podrías ayudar con el formulario del siguiente link <a href="/blog/contacto" class="nav-link">Click aqui</a> para contactarnos contigo y resolver todas tus dudas en breve',['siete'], single_response=True)


            


            response('Tú puedes obtener una recompensa monetaria por el uso de tu cuenta . puede ser desde $2000.00 incluso más todo depende de la calidad de tu cuenta . <br> <br> Una vez que sincronicemos tu cuenta, te agregamos a un grupo de WhatsApp, donde llevarémos la información de tu proceso y el control de tus pagos correspondientes. <br> <br>  Tu pagó puede realizarse por cualquiera de estas 2 opciones: Una transferencia bancaria o una recarga telefónica. Cuando te agregamos a tu grupo de WhatsApp te pedimos los datos bancarios para tu pago <br> <br> Si quieres empezar lo mas pronto posible a ganar dinero da click aqui para que rellenes nuestro formulario con tus datos y lo siguiente que haremos es comunicarnos contigo <a href="/blog/contacto" class="nav-link">Click aqui</a>',['cuanto', 'como' , 'Como' , 'Comó' , 'gano' , 'Gano', 'dinero', 'tengo', 'dineor', 'dinerp', 'obtengo',  'depositan', 'pagan', 'cuanto', 'pagar', 'pago', 'deposito', 'dineor', 'ingresos', 'generar' , 'requisitos'], single_response=True)


            response('Para nada , tú no tienes que pagar ni invertir un solo peso , al contrarío nosotros te pagamos a ti por permitirnos trabajar en tu cuenta.', ['algo', 'canbio', 'camvio', 'acambio', 'cambio', 'cambió', 'depesitar', 'dar', 'depositar', 'depositár', 'pagar' ],  single_response=True)



            response('Hola muy buen día claro que sí , somos una empresa de marketing dedicada a realizar cuentas publicitarias en Facebook business que es la parte comercial de Facebook sobre temas cómo : Música , Mascotas , Belleza, entre otras . Por permitirnos trabajar en tu cuenta te ofrecemos un pago de $2000.00 que se te dará cuando la cuenta se verifique <br> <br> Si quieres empezar lo mas pronto posible a ganar dinero da click aqui para que rellenes nuestro formulario con tus datos y lo siguiente que haremos es comunicarnos contigo <a href="/blog/contacto" class="nav-link">Click aqui</a>', ['realizan', 'hacen', 'hacén', 'dedican', 'dedicán','acen', 'asen', 'hasen', 'deican', 'son', 'don', 'informes', 'info', 'ifno', 'unfo', 'informacio', 'información', 'infó', 'Información', 'informacion', 'infromacion' ],  single_response=True)

            response('Usted nos va apoyar en la sincronización de su cuenta ademas de compartir la pagina que crearemos con amigos y conocidos para que obtenga likes y así se verifique mas rápidamente y despues tú solo esperas por tu pago! <br><br> Para que tu cuenta pueda colaborar solo necesitas : contar con un perfil de Facebook con al menos 6 meses de creación , debe tener nombre real y al menos una foto del dueño del perfil . <br> <br> Tu nos ayudaras a sincronizar la cuenta en el primer paso , después ya que checamos que la cuenta es apta para colaborar procederemos a crear la página , cuando este lista te enviaremos el link por un grupo de whats al que te agregaremos más adelante donde te atenderémos en lo que dura la colaboración y te informaremos del pago . Tu podrás compartir la página con tus conocidos para que que le den like y se verifique ', ['tengo', 'yo', 'hacer', 'acer', 'hader', 'realizar', 'realisaer', 'relizar', 'hago',  ],  single_response=True)


            response('Todo el proceso tarda entre 1 a 2 meses en los cuales debe estar sincronizada tu cuenta .', ['cuanto', 'cuantó','tarda', 'tiempo', 'tiemop', 'van', 'tomar', 'prestada', 'cuenta', 'adentro', 'dentro'  ],  single_response=True)


        
            response('Estoy bien ¿Y tú?', ['estas', 'va', 'vas', 'sientes'], single_response=True)


            response( 'Para que te podamos contactar da click aqui para que rellenes nuestro formulario con tus datos y lo siguiente que haremos es comunicarnos contigo <a href="/blog/contacto" class="nav-link">Click aqui</a>' , ['datos', 'numero', 'contacto', 'contactar','contactenme', 'contacten', 'contactar' , 'contac' , 'mensaje', 'sms', 'llamar' , 'llamenme', 'llamen', 'empezar'], single_response=True)

            response('Claro en nuestra Empresa Tenemos Políticas de Privacidad para salvaguardar todos los datos de nuestros Colaboradores te las envío : <a href="https://performance.goldenclickads.com/privacy-policy"> https://performance.goldenclickads.com/privacy-policy  </a>', ['enserio', 'cierto', 'ciertó',  'verdadero', ], single_response=True)

            response('Para nada ,en nuestra empresa tus datos están 100% seguros ,además de que tenemos políticas de seguridad, te las envió: <a href="https://performance.goldenclickads.com/privacy-policy"> https://performance.goldenclickads.com/privacy-policy  </a>', ['quitaran', 'robaran', 'robar', 'quitarn', 'estafaran', 'seguros', 'datos', 'adtos',], single_response=True)

            response('Para dar inicio a la colaboración tenemos 2 opciones, tu eliges la que más te agrade y con el dispositivo con el que cuentes en este momento', ['opciones', 'inicio', 'iniciar', 'incio', 'opcion'], single_response=True)

            response('Nosotros realizamos colaboraciones seguras con las personas que ingresan ,te envió unas capturas de pagos que hemos realizado a las personas que colaboraron con nosotros : <br> <img src="./../../static/blog/images/$2000.jpg" alt="" style="width: 85%; height: 350px;"> <br> <br> <br> <img src="./../../static/blog/images/$2000o.jpg" alt="" style="width: 85%; height: 280px;">', ['pruebas', 'estafa', 'verdad', 'es verdad',  'es verad', 'prueba'], single_response=True)

            response('Ofrecemos un pago de $20000.00 (Pesos mexicanos) el cuál se realiza en aprox. 2 semanas desde que empezamos la colaboración, puedes obtener más solo que depende mucho de cómo se desarrolle la página que crearemos <br> <br> Si quieres empezar lo mas pronto posible a ganar dinero da click aqui para que rellenes nuestro formulario con tus datos y lo siguiente que haremos es comunicarnos contigo <a href="/blog/contacto" class="nav-link">Click aqui</a>', ['cuanto', 'cunto', 'cuanot', 'dinero', 'dineor',  'ganar', 'ganra', 'ganr'], single_response=True)


            response('Tenemos 2 opciones de ingreso ,una es con celular y otra con computadora, en la primera es necesario la contraseña ya que es por accesos es decir como ingresas normalmente a tu cuenta ,en la segunda opción no es necesario ya que realizamos  una sesión vía remoto con tu computadora y tú  puedes ver todo el proceso. Una vez que verifiquemos todo eso, se te otorgara el pago de $2000.00 pesos', ['contraseña', 'contra', 'clave', 'password', 'contraseña', 'contrasena', 'acceso',], single_response=True)

            response(' Contamos con la opción de referidos, usted puede obtener ganancias mediante la referencia de personas, por cada persona que ingrese al proceso usted recibe un pago de 300 pesos. ', ['mas', 'más','ganar mas', 'ganar más', 'obtener más', 'adicional'], single_response=True)


            response('Una vez que sincronicemos tu cuenta, te agregamos a un grupo de WhatsApp, donde llevarémos la información de tu proceso y el control de tus pagos correspondientes. Te ofrecemos un pago de $2000.00 , el cuál se realizará en cuanto la cuenta este verificada', ['sabre', 'sabré' ,'seguimiento', 'seguimientó', 'pago', 'pagó', 'segimineot', 'segumiento', 'segminto', 'saber','sabér'], single_response=True)

            response(' Por medio de su grupo de WhatsApp nos indica que ya no desea continuar con su proceso, nosotros eliminamos la pagina y le regresamos su cuenta sin problemas.', ['continuar', 'seguir', 'deseo', ], single_response=True)

            

            response('Claro! Usted puede seguir haciendo uso normal de su cuenta, nada se trabaja directamente es su perfil todo lo trabajamos en Business Facebook', ['seguir', 'seguír', 'utilizando', 'utilizandó',  'cuenta',  'cuentá', 'puedo', 'quitar',], single_response=True)

            response('Claro! Usted puede seguir haciendo uso normal de su cuenta, nada se trabaja directamente es su perfil todo lo trabajamos en Business Facebook', ['seguir', 'utilizando', 'cuenta', 'puedo', 'quitar',], single_response=True)
            response('El primer paso para que puedas iniciar es : sincronizar la cuenta , es decir vamos a ingresar a tu perfil con el que vas a colaborar , ya sincronizado se revisará que sea apto para colaborar .', ['paso', 'pasos', 'proceso', 'procedimiento', 'metodo' ], single_response=True)

            response('Es decir , vamos ingresar a tu perfil para poder crear nuestra página pero no tienes porque preocuparte ya que lo único que checamos es que tu correo y teléfono estén actualizados. <br> para sincronizar la cuenta tenemos 2 opciones que son : por teléfono o correo . Tu eliges la que más te agrade y con el dispositivo que cuentes a la mano . <br> <br> Si quieres empezar lo mas pronto posible a ganar dinero da click aqui para que rellenes nuestro formulario con tus datos y lo siguiente que haremos es comunicarnos contigo <a href="/blog/contacto" class="nav-link">Click aqui</a>', ['sincronizar', 'sincronizár' , 'refieres', 'refieres', 'significa', 'significá' ], single_response=True)


            response('Un gusto ayudarte', ['gracias', 'nos vemos', 'adios'], single_response=True)

            

        
            response('Un gusto ayudarte', ['gracias', 'nos vemos', 'adios'], single_response=True)


            best_match= max(highest_prob, key=highest_prob.get)

        
            return unknown() if highest_prob[best_match] < 1 else best_match



def unknown():
    response = ['No entendi la pregunta, puedes decirlo de nuevo con otras palabras', 'No estoy seguro de lo que quieres decir', 'intenta preguntarme con otras palabras'][random.randrange(3)]
    return response


