# -*- coding: utf-8 -*-
"""Gera carousels_data_novembro.json e as imagens .webp de novembro/assets a partir da pasta oficial dos carrosséis.

A legenda vem do legenda.txt de cada carrossel (o mesmo texto que vai para o Instagram). Outubro não é tocado.
"""
import json, pathlib, sys
from PIL import Image

AQUI = pathlib.Path(__file__).parent
CARROSSEIS = pathlib.Path(r"G:/00 - CLIENTES/02_GAIA/CRIACAO - CARROSEL/Novembro 2026")
sys.path.insert(0, str(CARROSSEIS / "_assets" / "build"))
import data  # noqa: E402

DIAS = {"seg": "Segunda-feira", "ter": "Terça-feira", "qua": "Quarta-feira", "qui": "Quinta-feira",
        "sex": "Sexta-feira", "sáb": "Sábado", "dom": "Domingo"}
PILAR = {"news": ("noticias", "Notícias"), "katiap": ("katia", "Dicas da tia Katia"), "hpv": ("inst", "Cápsulas de Cuidado")}
TITULO = {
    1: "O implante agora vale por cinco anos",
    2: "Apgar, a primeira nota da vida",
    3: "Por que esperar para clampear o cordão",
    4: "Anticorpo contra o VSR para bebês prematuros",
    5: "A alta da UTI não encerra o cuidado",
    6: "O teste de DNA-HPV chega a 26 estados",
    7: "O puerpério de quem sai da maternidade sem o bebê",
    8: "O toque no prematuro",
    9: "Terapia hormonal da menopausa em avaliação para o SUS",
    10: "Pressão alta na gestação ganhou um plano mundial",
    11: "Implantes hormonais manipulados em xeque",
}
MEDICA = {1: "andrea", 2: "katia", 3: "katia", 4: "katia", 5: "katia", 6: "andrea", 7: "nathalia",
          8: "katia", 9: "andrea", 10: "andrea", 11: "andrea"}
FIXA = {5, 6}  # 15/11 Dia Mundial da Prematuridade · 17/11 Dia de Eliminação do Câncer do Colo do Útero
FECHO = "A frase de fecho foi escrita por nós; o texto da médica prevalece."
NOTA = {
    1: "Cita o comunicado da Anvisa e a nota da Febrasgo. A RE 4.184/2026 e a bula ainda não foram abertas. " + FECHO,
    2: "Leitura da Dra. Katia. O carrossel fala só do limite populacional que a SBP descreve, sem prever o futuro de uma criança específica.",
    3: "Leitura da Dra. Katia. A regra de 60 segundos citada é a do documento da SBP para bebês com 34 semanas ou mais.",
    4: "\"Proteção que já vem pronta\" é a nossa explicação de anticorpo monoclonal. O card da vacina da gestante usa a Instrução Normativa lida na cópia da Prefeitura de Porto Alegre, ainda não conferida no gov.br. " + FECHO,
    5: "Data fixa: 15/11, Dia Mundial da Prematuridade.",
    6: "Data fixa: 17/11. A frase \"chances de cura de 100%\" do comunicado do Ministério ficou de fora por soar absoluta. A capa traz um útero floral, e a Dra. Andrea havia deixado a linha fisiológica em outubro: vale olhar a capa. " + FECHO,
    7: "\"O pensamento ficou na UTI\" é linha nossa. O card de saúde mental leva o CVV 188. Os números da metanálise não entraram. " + FECHO,
    8: "É a peça de 15 de outubro sem mudança de texto. Falta a validação da Dra. Katia para a comparação com o carinho que desliza.",
    9: "A Febrasgo fala em consulta pública até 23/10; a Conitec fala em chamada pública da Perspectiva do Paciente, com inscrições até 28/10. O card segue a Conitec. " + FECHO,
    10: "Números mundiais da OMS. A nota não traz conduta, por isso o carrossel não orienta a gestante. " + FECHO,
    11: "A carta é um pedido, não uma proibição. Os nomes das entidades signatárias não entraram. " + FECHO,
}


def pasta(c):
    return f'{c["n"]:02d} - {c["data"][:5].replace("/", "-")} - {c["slug"]}'


out = []
for c in data.CAROUSELS:
    n = c["n"]
    src = CARROSSEIS / pasta(c)
    slug, badge = PILAR[c["theme"]]
    dd, mm = c["data"][:2], c["data"][3:5]
    cid = f"{n:02d}"
    num = len(c["slides"])
    out.append(dict(
        id=cid, folder=pasta(c), data=c["data"], data_ordem=f"2026-{mm}-{dd}",
        dia_mes=c["data"][:5], dia_semana=DIAS[c["data"][7:10]],
        titulo=TITULO[n], pilar=c["pilar"], pilar_slug=slug, pilar_badge=badge,
        subpilar=c["pilar"].split("·")[-1].strip(), medica=c["medica"], medica_tag=MEDICA[n],
        origem=c["origem"], num_slides=num, nota=NOTA[n], data_fixa=n in FIXA, reserva=False,
        legenda=(src / "legenda.txt").read_text(encoding="utf-8").strip(),
    ))
    dest = AQUI / "novembro" / "assets" / cid
    dest.mkdir(parents=True, exist_ok=True)
    for i in range(1, num + 1):
        Image.open(src / f"{i}.png").convert("RGB").save(dest / f"{i}.webp", "WEBP", quality=88, method=6)
    print(cid, num, "cards", "->", dest.relative_to(AQUI))

(AQUI / "carousels_data_novembro.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print("carousels_data_novembro.json:", len(out), "carrosséis")
