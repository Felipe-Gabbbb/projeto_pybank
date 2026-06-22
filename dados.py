from datetime import datetime
agora = datetime.now()
meses = (
    "Jan","Fev","Mar","Abr","Mai","Jun",
    "Jul","Ago","Set","Out","Nov","Dez"
)
rec = {
    "salario": {"valor": 3000.0, "mes": meses[agora.month - 1]},
    "freelance": {"valor": 500.90, "mes": meses[agora.month - 1]},
    "investimentos": {"valor": 200.10, "mes": meses[agora.month - 1]},
}
desp = {
    "cartões": {
        "caixa": {
            "nome": "caixa",
            "fatura": 1000.0,
            "status": "pendente",
            "mes": meses[agora.month - 1],
        },
        "bradesco": {
            "nome": "bradesco",
            "fatura": 500.0,
            "status": "pendente",
            "mes": meses[agora.month - 1],
        },
    },
    "contas": {
        "luz": {
            "nome": "luz",
            "fatura": 150.86,
            "status": "pendente",
            "mes": meses[agora.month - 1],
        },
        "agua": {
            "nome": "agua",
            "fatura": 100.95,
            "status": "pendente",
            "mes": meses[agora.month - 1],
        },
    },
    "outros": {
        "shoppe": {
            "nome": "shoppe",
            "fatura": 236.50,
            "status": "pendente",
            "mes": meses[agora.month - 1],
        },
        "amazon": {
            "nome": "amazon",
            "fatura": 120.25,
            "status": "pendente",
            "mes": meses[agora.month - 1],
        },
    },
}
metas = {
    "carro": {"nome": "carro", "total": 40000.0, "valor": 36500.50, "estado": True},
    "moto": {"nome": "moto", "total": 15000.0, "valor": 8000.66, "estado": True},
}
