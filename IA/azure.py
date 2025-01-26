"""
Eres un agente especializado en sistemas operativos de windows, 
tu objetivo es responder preguntas sobre soporte del sistema operativo, 
quiero que me respondas a la siguiente pregunta " Como puedo cambiar el fondo de escritorio" 
y quiero que la respuesta no supere los 30 palabras y si la pregunta no tiene nada que ver sobre 
sistemas operativos de windows responde que no tienes la capacidad para responder a este pregunta.
"""

import platform
from langchain_openai import AzureChatOpenAI

class AzureChatOpenAI:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(AzureChatOpenAI, cls).__new__(cls)
        return cls._instance

    def __init__(self, temperature, deployment_name, model_name, api_key, api_version, azure_endpoint):
        if not hasattr(self, 'initialized'):
            self.llm = AzureChatOpenAI(
                temperature=temperature,
                deployment_name=deployment_name,
                model_name=model_name,
                api_key=api_key,
                api_version=api_version,
                azure_endpoint=azure_endpoint
            )
            self.initialized = True

    def invoke(self, question):
        question= f"Eres un agente especializado en sistemas operativos de {platform.system()}, tu objetivo es responder preguntas sobre soporte del sistema operativo, quiero que me respondas a la siguiente pregunta '{question}' y quiero que la respuesta no supere los 30 palabras y si la pregunta no tiene nada que ver sobre el sistema operativo responde que no tienes la capacidad para responder a este pregunta."
        return self.llm.invoke(question)
