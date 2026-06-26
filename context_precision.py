import os
import sys
from pathlib import Path
import asyncio

# este log deve ter sido colocado pq alguma coisa não tinha funcionado
import logging
# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.INFO)

from openai import AsyncOpenAI
from ragas.llms import llm_factory
# alterado apos pesquisar que nao eh ragas.metrics.collections mas soh ragas.metrics
# from ragas.metrics import ContextPrecision
from ragas.metrics.collections import ContextPrecision

# Setup LLM
client = AsyncOpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY")
)

llm = llm_factory("gpt-4o-mini", client=client)
# llm = llm_factory("gpt-4.1-mini", client=client)
# llm = llm_factory("z-ai/glm-5.1", client=client)
## llm = llm_factory("openrouter/elephant-alpha", client=client)
##
### Create metric
scorer = ContextPrecision(llm=llm)
##
print ("___ Scorer___")
print (scorer)
print ("___ Scorer___")

##
### Evaluate
input = "o que é um cartão de crédito?"
reference = "é um instrumento de crédito pessoal"
retrieved = "é um instrumento de crédito pessoal"
print (" ") 
print ("input: ", input)
print ("reference: ", reference)
print ("retrieved contexts: ", retrieved)
print (" ")

result = scorer.score(
    user_input=input,
    reference= reference,
    retrieved_contexts=[ retrieved,
    ] 
)
print(f"Context Precision Score: {result.value}")

## respostas salvas
##        "It is a way to pay things."
## "The Brandenburg Gate is located in Berlin.",

## "é um plastico que usarmos para fazer compras",
##        "é um meio de pagamento",
