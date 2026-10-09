# -*- coding: utf-8 -*-
"""Gera carousels_data_v2.json e as imagens .webp de outubro/v2/assets a partir da pasta oficial dos carrosséis.

Só entram as peças revisadas em 09/10/2026. A versão 1 (outubro/index.html e outubro/assets) não é tocada.
"""
import json, pathlib, re, sys
from PIL import Image

AQUI = pathlib.Path(__file__).parent
CARROSSEIS = pathlib.Path(r"G:/00 - CLIENTES/02_GAIA/CRIACAO - CARROSEL/Outubro Rosa 2026")
sys.path.insert(0, str(CARROSSEIS / "_assets" / "build"))
import data  # noqa: E402

REVISADOS = [16, 2, 5, 8, 11, 12, 6]
DIAS = {"seg": "Segunda-feira", "ter": "Terça-feira", "qua": "Quarta-feira", "qui": "Quinta-feira",
        "sex": "Sexta-feira", "sáb": "Sábado", "dom": "Domingo"}
PILAR = {"rosa": ("rosa", "Outubro Rosa"), "hpv": ("hpv", "Ginecologia · HPV"), "katia": ("katia", "Dicas da tia Katia"),
         "wine": ("inst", "Institucional"), "wine2": ("inst", "Cápsulas de Cuidado")}
MEDICA = {16: "andrea", 2: "andrea", 5: "andrea", 8: "andrea", 11: "andrea", 12: "equipe", 6: "katia"}
FIXA = {12}
NOTA = {
    16: "Peça de lançamento da linha Cápsulas de Cuidado. A legenda explica a pausa e o retorno das publicações.",
    2: "Texto revisado pela Dra. Andrea em 09/10. A frase \"como os estudos já mostraram várias vezes\" está no card 4 sem fonte indicada.",
    5: "Ajustes da Dra. Andrea aplicados: \"contraído\", \"elimina\" e o novo fechamento.",
    8: "Texto novo da Dra. Andrea. Dois pontos para confirmar: o card 4 diz \"milhões de mulheres\" no lugar de \"quase 215 milhões\" e o card 6 mantém \"totalmente evitável\".",
    11: "Texto sem mudança. Imagens refeitas em aquarela. Ainda sem retorno da revisão clínica.",
    12: "Texto sem mudança. Imagens refeitas com figuras de mulheres em cada fase da vida.",
    6: "Esquema do SUS reescrito a partir do guia técnico do Ministério da Saúde. Aguarda a Dra. Katia. Peça de reserva, sem data.",
}


def clean(t):
    return re.sub(r"\s+", " ", re.sub(r"<br\s*/?>", " ", t)).strip()


def titulo(c):
    s0 = c["slides"][0]
    if s0["t"] in ("cover", "fcover", "tcover"):
        return clean(" ".join(s0["title"]))
    if s0["t"] == "kcover":
        return "Tia Katia: " + clean(c["slides"][1].get("title", ""))
    return clean(" ".join(s0["lines"]) + " " + s0["bold"]).capitalize()


def pasta(c):
    return f'{c["n"]:02d} - {c["data"][:5].replace("/", "-")} - {c["slug"]}'


by = {c["n"]: c for c in data.CAROUSELS}
out = []
for n in REVISADOS:
    c = by[n]
    reserva = bool(c.get("backup"))
    slug, badge = PILAR[c["theme"]]
    loc = data.TAGS_LOCAL_PED if c["theme"].startswith("katia") else data.TAGS_LOCAL
    dd, mm = c["data"][:2], c["data"][3:5]
    cid = f"{n:02d}"
    out.append(dict(
        id=cid, folder=pasta(c),
        data="Reserva (sem data)" if reserva else c["data"],
        data_ordem="2026-12-31" if reserva else f"2026-{mm}-{dd}",
        dia_mes="--" if reserva else c["data"][:5],
        dia_semana="Reserva" if reserva else DIAS[c["data"][7:10]],
        titulo=titulo(c), pilar=c["pilar"], pilar_slug=slug, pilar_badge=badge,
        subpilar=c["pilar"].split("·")[-1].strip(), medica=c["medica"], medica_tag=MEDICA[n],
        origem=c["origem"], num_slides=len(c["slides"]), nota=NOTA[n],
        data_fixa=(n in FIXA) and not reserva, reserva=reserva,
        legenda=c["legenda"].format(aviso=data.AVISO, local=loc),
    ))
    dest = AQUI / "outubro" / "v2" / "assets" / cid
    dest.mkdir(parents=True, exist_ok=True)
    for i in range(1, len(c["slides"]) + 1):
        Image.open(CARROSSEIS / pasta(c) / f"{i}.png").convert("RGB").save(dest / f"{i}.webp", "WEBP", quality=88, method=6)
    print(cid, len(c["slides"]), "cards", "->", dest.relative_to(AQUI))

(AQUI / "carousels_data_v2.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print("carousels_data_v2.json:", len(out), "carrosséis")
