"""
user.py
~~~~~~~~~~~~~
The class User stores the list of tweets and the screen name of a particular user.
It generates responses to the question "Qué debería hacer con mi vida" based on the
list of tweets of the user.
"""

import tweepy

DESIRES = ["quiero", "necesito", "deseo", "anhelo", "aspiro", "ansio", "gustaría"]

VERBS = ["abandonar", "abordar", "abortar", "abrazar", "abrir", "aburrir", "aburrirme", "abusar", "acabar", "acampar", "aceptar", "acercar", "acercarme", "acompañar", "aconsejar", "acontecer", "acordar", "acordarme", "acortar", "acostar", "acostarme", "acostumbrar", "acostumbrarme", "actuar", "adivinar", "admirar", "admitir", "adorar", "adornar", "advertir", "afeitar", "afeitarme", "afirmar", "afligir", "agorar", "agradar", "agradecer", "aguantar", "ahorcar", "ahorrar", "alcanzar", "alegrar", "alegrarme", "alentar", "aliviar", "almorzar", "alquilar", "amanecer", "amar", "amenazar", "andar", "anhelar", "anunciar", "añadir", "apagar", "aparecer", "aplaudir", "aplicar", "apostar", "apoyar", "apreciar", "aprender", "apretar", "aprobar", "argüir", "arreglar", "arrepentirme", "arrojar", "asistir", "asociar", "aspirar", "asustar", "asustarme", "atacar", "atender", "atraer", "atravesar", "atreverme", "aumentar", "avanzar", "averiguar", "avisar", "ayudar", "bailar", "bajar", "bañar", "bañarme", "barrer", "batir", "bautizar", "beber", "bendecir", "besar", "bordar", "borrar", "brillar", "brindar", "broncearme", "bucear", "burlar", "burlarme", "buscar", "caber", "caer", "calcular", "calentar", "calentarme", "callar", "callarme", "calmar", "calmarme", "cambiar", "caminar", "cancelar", "cansar", "cansarme", "cantar", "caracterizar", "cargar", "casar", "casarme", "castigar", "causar", "cazar", "celebrar", "cenar", "censurar", "cepillar", "cerrar", "cesar", "charlar", "chismear", "chocar", "civilizar", "clarificar", "clasificar", "cobrar", "cocinar", "coger", "colgar", "colocar", "colonizar", "combatir", "comenzar", "comer", "competir", "componer", "comprar", "comprender", "comunicar", "comunicarme", "condenar", "conducir", "confesar", "confiar", "confirmar", "compartir", "confiscar", "conjugar", "conocer", "conquistar", "conseguir", "consentir", "conservar", "consistir", "constituir", "construir", "consumir", "contaminar", "contar", "contener", "contestar", "continuar", "contribuir", "controlar", "convencer", "convenir", "conversar", "convertir", "convidar", "copiar", "corregir", "correr", "cortar", "coser", "costar", "crear", "crecer", "creer", "criar", "criarme", "criticar", "crucificar", "cruzar", "cubrir", "cuidar", "culpar", "cultivar", "cumplir", "curar", "dar", "deber", "decidir", "decidirme", "decir", "declarar", "decorar", "dedicar", "dedicarme", "defender", "dejar", "demostrar", "depender", "depositar", "deprimir", "derretir", "desagradar", "desagradecer", "desaparecer", "desayunar", "descansar", "descender", "describir", "descubrir", "desarrollar", "desarrollarme", "desear", "deshacer", "despedir", "despertar", "despertarme", "destruir", "detener", "detenerme", "detestar", "devolver", "devorar", "dibujar", "dirigir", "discutir", "diseñar", "disfrutar", "disgustar", "disminuir", "distinguir", "distribuir", "divertir", "divertirme", "divorciar", "divorciarme", "doblar", "doler", "dormir", "dormirme", "duchar", "ducharme", "dudar", "durar", "echar", "echarme", "educar", "efectuar", "ejercer", "elegir", "eliminar", "emborrachar", "emborracharme", "emigrar", "empezar", "emplear", "enamorar", "enamorarme", "encantar", "encender", "encontrar", "enfadar", "enfadarme", "enfermar", "enfermarme", "enflaquecer", "enflaquecerme", "engañar", "enojar", "enojarme", "enriquecer", "enriquecerme", "enseñar", "ensuciar", "entender", "enterarme", "entrar", "entregar", "entretener", "entrevistar", "entusiasmar", "entusiasmarme", "envejecer", "envejecerme", "enviar", "equivocar", "equivocarme", "errar", "escoger", "esconder", "esconderme", "escribir", "escuchar", "esperar", "esquiar", "establecer", "estar", "estimar", "estudiar", "evacuar", "evitar", "exhibir", "exigir", "explicar", "explorar", "explotar", "exponer", "exportar", "expresar", "extender", "extinguir", "fabricar", "faltar", "fascinar", "felicitar", "fijar", "fingir", "firmar", "florecer", "formar", "fortalecer", "fregar", "freír", "fumar", "funcionar", "ganar", "gastar", "generalizar", "glorificar", "gobernar", "graduar", "graduarme", "gritar", "gruñir", "guardar", "guiar", "gustar", "haber (verbo impersonal)", "haber (verbo auxiliar)", "hablar", "hacer", "hallar", "hallarme", "helar", "heredar", "herir", "hervir", "huir", "hundir", "hundirme", "ilustrar", "importar", "imprimir", "incluir", "indicar", "inducir", "influir", "informar", "iniciar", "inmigrar", "insistir", "instalar", "insultar", "intentar", "interesar", "interpretar", "introducir", "invadir", "inventar", "invertir", "investigar", "invitar", "invocar", "ir", "irme", "jugar", "juntar", "jurar", "ladrar", "lamentar", "lanzar", "lastimar", "lavar", "lavarme", "leer", "legalizar", "levantar", "levantarme", "limpiar", "llamar", "llamarme", "llegar", "llenar", "llevar", "llorar", "llover", "lograr", "luchar", "madurar", "mandar", "manejar", "mantener", "maquillar", "maquillarme", "marcar", "masticar", "matar", "matricular", "matricularme", "medir", "mentir", "merecer", "merendar", "meter", "mezclar", "mirar", "modificar", "molestar", "montar", "morir", "mostrar", "mover", "moverme", "mudar", "mudarme", "nacer", "nadar", "navegar", "necesitar", "negar", "negarme", "negociar", "nevar", "notar", "obedecer", "obligar", "obtener", "ocurrir", "odiar", "ofender", "ofrecer", "oír", "oler", "olvidar", "olvidarme", "oponer", "oponerme", "organizar", "padecer", "pagar", "parar", "parecer", "participar", "partir", "pasar", "patinar", "pedir", "pegar", "peinar", "peinarme", "pelear", "pensar", "perder", "perdonar", "permanecer", "permitir", "perseguir", "pertenecer", "pesar", "pescar", "picar", "pintar", "platicar", "planchar", "plantar", "poder", "poner", "ponerme", "practicar", "predecir", "preferir", "preguntar", "preguntarme", "preparar", "prepararme", "presentar", "presentir", "preservar", "prever", "probar", "producir", "prohibir", "prometer", "proponer", "proseguir", "proteger", "protestar", "provocar", "publicar", "purificar", "quebrar", "quebrarme", "quedar", "quedarme", "quejarme", "quemar", "quemarme", "querer", "quitar", "realizar", "rechazar", "recibir", "reciclar", "recoger", "recomendar", "reconocer", "recordar", "redargüir", "reducir", "regalar", "regar", "regatear", "regir", "registrar", "registrarme", "regresar", "regular", "rehusar", "rehusarme", "reinar", "reír", "renacer", "renovar", "renunciar", "reñir", "reparar", "repasar", "repetir", "replicar", "reportar", "requerir", "reservar", "resolver", "respetar", "respirar", "responder", "resultar", "revelar", "rezar", "robar", "rogar", "romper", "saber", "sacar", "sacrificar", "sacudir", "salir", "saltar", "saludar", "salvar", "satisfacer", "satirizar", "secar", "secarme", "seguir", "sentar", "sentarme", "sentir", "sentirme", "señalar", "ser", "servir", "significar", "simbolizar", "situar", "sobrevivir", "soler", "sonar", "soñar", "sonreír", "soportar", "sorprender", "subir", "suceder", "sufrir", "sugerir", "suponer", "surgir", "suspirar", "sustituir", "tañer", "tapar", "tardar", "temer", "tener", "teñir", "terminar", "tirar", "tocar", "tomar", "torcer", "toser", "trabajar", "traducir", "traer", "tragar", "tratar", "triunfar", "tropezar", "ubicar", "unir", "untar", "usar", "utilizar", "vaciar", "valer", "variar", "vencer", "vender", "venir", "ver", "verificar", "vestir", "vestirme", "viajar", "visitar", "vivir", "volar", "volver", "vomitar", "votar", "yacer", "zambullirme"]


class User:
    def __init__(self, screen_name):
        self.screen_name = screen_name
        self.tweets_list = []
        self.responses_list = []

    """
    Handy script from https://gist.github.com/yanofsky/5436496 by yanofsky
    "A script to download all of a user's tweets into a csv"
    """
    def fetch_tweets(self, api):
        # Initialize a list to hold all the tweepy Tweets
        all_tweets = []

        # Make initial request for most recent 200 Tweets
        new_tweets = api.api.user_timeline(screen_name=self.screen_name, count=200)

        # Save the most recent Tweets
        all_tweets.extend(new_tweets)

        # Save the id of the oldest Tweet less one
        oldest = all_tweets[-1].id - 1

        # Keep grabbing Tweets until there are no Tweets left to grab

        while len(new_tweets) > 0:
            print ("Downloading {} Tweets before {}".format(self.screen_name, oldest))

            # All subsequent requests use the max_id param to prevent duplicates
            new_tweets = api.api.user_timeline(screen_name=self.screen_name, count=200, max_id=oldest)
            all_tweets.extend(new_tweets)
            oldest = all_tweets[-1].id - 1
            print ("   ...{} Tweets downloaded so far".format(len(all_tweets)))

        # Keep only the text part from each tweet if it is longer than 4
        self.tweets_list = [tweet.text.lower() for tweet in all_tweets if len(tweet.text) > 4]
        self.parse_tweets()

    def parse_tweets(self):
        # TODO: Replace with efficient algorithm
        # Find those tweets that include a string from DESIRES
        for tweet in self.tweets_list:
            for desire in DESIRES:
                if desire in tweet:
                    try:
                        # Get the index of the desire in the tweet as a list
                        tweet_as_list = tweet.split()
                        desire_idx = tweet_as_list.index(desire)

                        # TODO: Also replace with efficient algorithm
                        # The desire is positive if the previous word is not a "no"
                        is_positive = True
                        if desire_idx - 1 >= 0:
                            is_positive =  tweet_as_list[desire_idx - 1] != "no"

                        # The desire is actually a desire if there is not a "que" before the desire word
                        is_need = True
                        if desire_idx - 2 >= 0:
                            is_need = tweet_as_list[desire_idx - 2] != "que"
                            is_need = is_need and tweet_as_list[desire_idx - 2] != "qué"

                        if desire_idx + 2 < len(tweet_as_list):
                            is_need = is_need and tweet_as_list[desire_idx + 2] != "con"
                            is_need = is_need and tweet_as_list[desire_idx + 2] != "para"

                        # Generate a response if the next word is a verb and it is a positive desire
                        verb_idx = desire_idx + 1
                        if is_positive and is_need and verb_idx < len(tweet_as_list) and tweet_as_list[desire_idx + 1] in VERBS:
                            response = self.generate_response(tweet_as_list[verb_idx:])
                            self.responses_list.append(response)

                    except Exception as e:
                        print("¯\_(ツ)_/¯")
                        print(e)


    def generate_response(self, tweet_as_list):
        # Check if the verb is not in infinitive (when the last letter is "r")
        if tweet_as_list[0][-1] != "r":
            # Delete the last 2 letters of the verb to make it infinitive
            tweet_as_list[0] = tweet_as_list[0][:-2:]

        # Attempt to chance the direct object of the sentence. Not working atm
        for word in tweet_as_list:
            if word == "mi":
                word = "tu"
        return " ".join(tweet_as_list)
