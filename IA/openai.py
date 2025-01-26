from langchain_openai import ChatOpenAI


class ChatOpenAI:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ChatOpenAI, cls).__new__(cls)
        return cls._instance

    def __init__(self, temperature, model, api_key, base_url):
        if not hasattr(self, 'initialized'):
            self.llm = ChatOpenAI(
                temperature=temperature,
                model=model,
                api_key=api_key,
                base_url=base_url
            )
            self.initialized = True

    def invoke(self, question):
        question= f"Eres un agente especializado en sistemas operativos de {platform.system()}, tu objetivo es responder preguntas sobre soporte del sistema operativo, quiero que me respondas a la siguiente pregunta '{question}' y quiero que la respuesta no supere los 30 palabras y si la pregunta no tiene nada que ver sobre el sistema operativo responde que no tienes la capacidad para responder a este pregunta."
        return self.llm.invoke(question)