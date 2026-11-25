"""Confere os cálculos do CMA (Sprint 1) a partir de dados/dados_simulados_CMA.csv.

Recalcula A, T, IH, classe, C, PF, IP e prioridade com as regras do README
e compara com os valores registrados no CSV. Uso:

    python scripts/calcular_indices.py
"""
import csv
from pathlib import Path

CSV = Path(__file__).resolve().parent.parent / "dados" / "dados_simulados_CMA.csv"
PESOS = {"D": 0.30, "P": 0.25, "A": 0.20, "T": 0.15, "M": 0.10}


def score_alarmes(baixa, media, alta):
    return max(0, 100 - 10 * baixa - 20 * media - 40 * alta)


def score_tendencia(queda_p_30d):
    return max(0, 100 - 10 * max(0, queda_p_30d))


def indice_saude(d, p, a, t, m):
    return round(PESOS["D"] * d + PESOS["P"] * p + PESOS["A"] * a
                 + PESOS["T"] * t + PESOS["M"] * m, 2)


def classificar(ih):
    if ih >= 80:
        return "Normal"
    if ih >= 60:
        return "Atenção"
    return "Crítico"


def classe_criticidade(s, o, r):
    valor = round(0.50 * s + 0.30 * o + 0.20 * r, 2)
    for limite, classe in ((1.80, 1), (2.60, 2), (3.40, 3), (4.20, 4)):
        if valor <= limite:
            return valor, classe
    return valor, 5


def probabilidade_falha(ih):
    if ih >= 90:
        return 1
    if ih >= 80:
        return 2
    if ih >= 70:
        return 3
    if ih >= 60:
        return 4
    return 5


def nivel_prioridade(ip):
    if ip <= 4:
        return "Baixa"
    if ip <= 9:
        return "Média"
    if ip <= 16:
        return "Alta"
    return "Crítica"


def main():
    with CSV.open(encoding="utf-8") as arquivo:
        ativos = list(csv.DictReader(arquivo))

    resultados, erros = [], 0
    for r in ativos:
        n = lambda campo: float(r[campo])
        a = score_alarmes(n("alarmes_baixa"), n("alarmes_medias"), n("alarmes_altas"))
        t = score_tendencia(n("queda_P_30d"))
        ih = indice_saude(n("disponibilidade_D"), n("desempenho_P"), a, t, n("score_M"))
        score_c, c = classe_criticidade(n("seguranca_S"), n("operacao_O"), n("sem_redundancia_R"))
        pf = probabilidade_falha(ih)
        ip = pf * c
        calculado = {"score_A": a, "score_T": t, "indice_saude": ih, "classe_ih": classificar(ih),
                     "score_criticidade": score_c, "C": c, "probabilidade_PF": pf,
                     "indice_prioridade": ip, "prioridade": nivel_prioridade(ip)}
        for campo, valor in calculado.items():
            esperado = r[campo]
            ok = (abs(float(esperado) - float(valor)) < 0.01) if isinstance(valor, (int, float)) else esperado == valor
            if not ok:
                erros += 1
                print(f"DIVERGÊNCIA {r['ativo_id']} {campo}: CSV={esperado} calculado={valor}")
        resultados.append((r["ativo_id"], ih, calculado["classe_ih"], c, pf, ip, calculado["prioridade"]))

    print("Fila de atendimento (IP decrescente; desempate pelo menor IH):")
    for pos, (ativo, ih, classe, c, pf, ip, prio) in enumerate(
            sorted(resultados, key=lambda x: (-x[5], x[1])), start=1):
        print(f"{pos}. {ativo:9} IH={ih:6.2f} ({classe:8}) C{c} PF={pf} IP={ip:2} -> {prio}")
    print("Todos os cálculos conferem com o CSV." if erros == 0 else f"{erros} divergência(s) encontrada(s).")
    return 1 if erros else 0


if __name__ == "__main__":
    raise SystemExit(main())
