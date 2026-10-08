import os
import json
import html

# Load carousels data
json_path = os.path.join(os.path.dirname(__file__), 'carousels_data.json')
with open(json_path, 'r', encoding='utf-8') as f:
    carousels = json.load(f)

# Sort by date for chronological presentation
carousels_by_date = sorted(carousels, key=lambda x: x['data_ordem'])

# Generate the HTML
html_content = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"/>
  <title>Aprovação de Carrosséis · Outubro Rosa 2026 · Gaia Medicina Integrada</title>
  <meta name="description" content="Portal de visualização, navegação responsiva e aprovação individual dos 15 carrosséis do Instagram de Outubro 2026 da Gaia Medicina Integrada."/>
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,500;0,600;1,400;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet">

  <style>
    :root {
      --gaia-vinho: #853B50;
      --gaia-vinho-dark: #5C2233;
      --gaia-primaria: #B12A38;
      --gaia-rosa: #D95388;
      --gaia-rosa-pale: #FDF2F6;
      --gaia-hpv: #86286B;
      --gaia-adol: #2E7970;
      --gaia-katia: #C4566B;
      --gaia-fundo: #FAF5F5;
      --gaia-fundo-alt: #F4ECEC;
      --gaia-card: #FFFFFF;
      --gaia-texto: #2D2427;
      --gaia-muted: #7A696E;
      --gaia-borda: #EBDCDC;
      --gaia-whatsapp: #25D366;
      --gaia-whatsapp-dark: #128C7E;
      --gaia-alerta: #E65100;
      --sombra-card: 0 8px 30px rgba(133, 59, 80, 0.07);
      --sombra-hover: 0 14px 40px rgba(133, 59, 80, 0.14);
      --radius: 18px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }

    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background-color: var(--gaia-fundo);
      color: var(--gaia-texto);
      line-height: 1.6;
      padding-bottom: 90px;
    }

    /* ══════════════════════════════════════
       HEADER HERO
    ══════════════════════════════════════ */
    .header-hero {
      background: linear-gradient(135deg, var(--gaia-vinho-dark) 0%, var(--gaia-vinho) 55%, var(--gaia-primaria) 100%);
      color: #FFFFFF;
      padding: 42px 20px 36px;
      text-align: center;
      position: relative;
      overflow: hidden;
      box-shadow: 0 4px 20px rgba(92, 34, 51, 0.25);
    }
    .header-hero::before {
      content: '';
      position: absolute;
      top: -60px;
      right: -60px;
      width: 240px;
      height: 240px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(255,255,255,0.12) 0%, transparent 70%);
      pointer-events: none;
    }
    .header-hero::after {
      content: '';
      position: absolute;
      bottom: -80px;
      left: -40px;
      width: 220px;
      height: 220px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(217,83,136,0.2) 0%, transparent 70%);
      pointer-events: none;
    }
    .header-content {
      max-width: 820px;
      margin: 0 auto;
      position: relative;
      z-index: 2;
    }
    .brand-tag {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(255, 255, 255, 0.15);
      border: 1px solid rgba(255, 255, 255, 0.3);
      backdrop-filter: blur(8px);
      padding: 6px 16px;
      border-radius: 30px;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      margin-bottom: 14px;
    }
    .brand-tag span {
      width: 8px;
      height: 8px;
      background: #FFB5C5;
      border-radius: 50%;
      display: inline-block;
    }
    .header-hero h1 {
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: clamp(26px, 5.5vw, 40px);
      font-weight: 800;
      line-height: 1.18;
      letter-spacing: -0.02em;
      margin-bottom: 12px;
    }
    .header-hero p {
      font-family: 'Crimson Pro', Georgia, serif;
      font-style: italic;
      font-size: clamp(17px, 3.8vw, 21px);
      color: rgba(255, 255, 255, 0.92);
      max-width: 680px;
      margin: 0 auto 24px;
      line-height: 1.45;
    }
    .hero-badges {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 10px;
      margin-top: 8px;
    }
    .hero-badge {
      background: rgba(255, 255, 255, 0.14);
      border: 1px solid rgba(255, 255, 255, 0.22);
      padding: 7px 14px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .hero-badge b {
      color: #FFE6EE;
      font-weight: 800;
    }

    /* ══════════════════════════════════════
       BARRA DE NAVEGAÇÃO SUPERIOR FIXA
    ══════════════════════════════════════ */
    .sticky-nav {
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--gaia-borda);
      box-shadow: 0 2px 12px rgba(133, 59, 80, 0.05);
      padding: 10px 16px;
    }
    .sticky-nav-inner {
      max-width: 980px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
    }
    .nav-tabs {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }
    .nav-tab-btn {
      background: #F3EBEB;
      color: var(--gaia-vinho);
      border: 1px solid transparent;
      padding: 8px 16px;
      border-radius: 24px;
      font-size: 13.5px;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
      text-decoration: none;
    }
    .nav-tab-btn:hover, .nav-tab-btn.active {
      background: var(--gaia-vinho);
      color: #FFFFFF;
      box-shadow: 0 4px 12px rgba(133, 59, 80, 0.2);
    }
    .nav-quick-btn {
      background: #E8F5E9;
      color: #1B5E20;
      border: 1px solid #A5D6A7;
      padding: 8px 14px;
      border-radius: 24px;
      font-size: 12.5px;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      text-decoration: none;
      transition: all 0.2s;
    }
    .nav-quick-btn:hover {
      background: #C8E6C9;
    }

    /* ══════════════════════════════════════
       CONTAINER PRINCIPAL
    ══════════════════════════════════════ */
    .container {
      max-width: 940px;
      margin: 0 auto;
      padding: 24px 16px;
    }

    /* ══════════════════════════════════════
       SEÇÃO: CALENDÁRIO GERAL & APROVAÇÃO
    ══════════════════════════════════════ */
    .section-card {
      background: var(--gaia-card);
      border-radius: var(--radius);
      border: 1px solid var(--gaia-borda);
      box-shadow: var(--sombra-card);
      padding: 28px 24px;
      margin-bottom: 36px;
      overflow: hidden;
    }
    @media (max-width: 600px) {
      .section-card {
        padding: 20px 16px;
        border-radius: 14px;
      }
    }
    .section-header {
      margin-bottom: 22px;
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      flex-wrap: wrap;
      gap: 12px;
      border-bottom: 2px solid #F6EFEF;
      padding-bottom: 16px;
    }
    .section-header-left h2 {
      color: var(--gaia-vinho);
      font-size: clamp(20px, 4vw, 26px);
      font-weight: 800;
      letter-spacing: -0.01em;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .section-header-left p {
      color: var(--gaia-muted);
      font-size: 14px;
      margin-top: 4px;
    }

    /* Banner de Aprovação Geral do Calendário */
    .calendario-aprovacao-box {
      background: linear-gradient(135deg, #FDF7F8 0%, #FFF5F7 100%);
      border: 1.5px solid #F0CFD8;
      border-radius: 14px;
      padding: 20px;
      margin-bottom: 24px;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }
    .cal-box-header {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .cal-box-icon {
      width: 44px;
      height: 44px;
      border-radius: 12px;
      background: var(--gaia-vinho);
      color: white;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 22px;
      flex-shrink: 0;
    }
    .cal-box-title h3 {
      font-size: 17px;
      font-weight: 700;
      color: var(--gaia-vinho);
    }
    .cal-box-title p {
      font-size: 13.5px;
      color: #665;
      margin-top: 2px;
    }
    .cal-box-actions {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }
    .btn-wpp-calendario {
      flex: 1;
      min-width: 240px;
      background: var(--gaia-whatsapp);
      color: white;
      text-decoration: none;
      font-size: 14px;
      font-weight: 700;
      padding: 12px 18px;
      border-radius: 10px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      box-shadow: 0 4px 12px rgba(37, 211, 102, 0.28);
      transition: all 0.2s ease;
    }
    .btn-wpp-calendario:hover {
      background: var(--gaia-whatsapp-dark);
      transform: translateY(-1px);
    }
    .btn-wpp-ajuste {
      background: #FFFFFF;
      color: #853B50;
      border: 1.5px solid #E4C0CA;
      text-decoration: none;
      font-size: 13px;
      font-weight: 700;
      padding: 12px 16px;
      border-radius: 10px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      transition: all 0.2s;
    }
    .btn-wpp-ajuste:hover {
      background: #FDF2F5;
      border-color: var(--gaia-vinho);
    }

    /* Linha do tempo de semanas */
    .semana-group {
      margin-bottom: 24px;
    }
    .semana-title {
      font-size: 15px;
      font-weight: 700;
      color: var(--gaia-vinho);
      padding-bottom: 8px;
      border-bottom: 1.5px solid var(--gaia-borda);
      margin-bottom: 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .semana-title span {
      font-size: 12.5px;
      color: var(--gaia-muted);
      font-weight: 500;
    }
    .timeline-list {
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .timeline-item {
      display: grid;
      grid-template-columns: 58px 74px minmax(0, 1fr) auto;
      gap: 14px;
      align-items: center;
      background: #FCF9F9;
      border: 1px solid var(--gaia-borda);
      border-radius: 12px;
      padding: 10px 14px;
      transition: all 0.2s ease;
    }
    .timeline-item:hover {
      background: #FFFFFF;
      border-color: var(--gaia-rosa);
      box-shadow: 0 4px 14px rgba(133, 59, 80, 0.08);
      transform: translateY(-1px);
    }
    @media (max-width: 580px) {
      .timeline-item {
        grid-template-columns: 50px 64px minmax(0, 1fr);
        gap: 10px;
        padding: 8px 10px;
      }
      .timeline-btn-col {
        grid-column: 1 / -1;
        margin-top: 4px;
      }
    }
    .time-dia-box {
      text-align: center;
    }
    .time-dia-num {
      font-size: 24px;
      font-weight: 800;
      color: var(--gaia-vinho);
      line-height: 1;
    }
    .time-dia-sem {
      font-size: 11px;
      font-weight: 600;
      color: var(--gaia-muted);
      text-transform: uppercase;
    }
    .timeline-thumb {
      width: 74px;
      height: 92px;
      border-radius: 8px;
      object-fit: cover;
      background: #EEE;
      cursor: pointer;
      box-shadow: 0 2px 6px rgba(0,0,0,0.1);
      transition: transform 0.2s;
    }
    .timeline-thumb:hover {
      transform: scale(1.04);
    }
    @media (max-width: 580px) {
      .timeline-thumb {
        width: 64px;
        height: 80px;
      }
    }
    .timeline-info {
      min-width: 0;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }
    .timeline-info h4 {
      font-size: 15px;
      font-weight: 700;
      color: var(--gaia-texto);
      line-height: 1.3;
      margin: 0;
    }
    .timeline-meta {
      font-size: 12.5px;
      color: var(--gaia-muted);
    }
    .timeline-meta b {
      color: var(--gaia-vinho);
      font-weight: 600;
    }
    .badge-linha {
      display: inline-block;
      font-size: 11px;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 12px;
      width: fit-content;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .badge-linha.rosa {
      background: #FCE8EE;
      color: var(--gaia-rosa);
      border: 1px solid #F8B4C8;
    }
    .badge-linha.katia {
      background: #FDF0F2;
      color: var(--gaia-katia);
      border: 1px solid #F5C6CE;
    }
    .badge-linha.hpv {
      background: #F7EBF4;
      color: var(--gaia-hpv);
      border: 1px solid #E1BBD8;
    }
    .badge-linha.adol {
      background: #E8F5F3;
      color: var(--gaia-adol);
      border: 1px solid #B3DFD9;
    }
    .badge-linha.inst {
      background: #F4E8EC;
      color: var(--gaia-vinho);
      border: 1px solid #DCBAC5;
    }
    .badge-fixa {
      background: #FFF3E0;
      color: #E65100;
      border: 1px solid #FFE0B2;
      font-size: 10.5px;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: 10px;
    }

    .btn-ir-carrossel {
      background: #FFFFFF;
      color: var(--gaia-vinho);
      border: 1px solid var(--gaia-borda);
      font-size: 12.5px;
      font-weight: 700;
      padding: 8px 14px;
      border-radius: 8px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      white-space: nowrap;
      transition: all 0.2s;
    }
    .btn-ir-carrossel:hover {
      background: var(--gaia-vinho);
      color: white;
      border-color: var(--gaia-vinho);
    }

    /* ══════════════════════════════════════
       BARRA DE FILTROS E CONTROLE DE EXIBIÇÃO
    ══════════════════════════════════════ */
    .controls-wrapper {
      background: var(--gaia-card);
      border-radius: var(--radius);
      border: 1px solid var(--gaia-borda);
      padding: 20px;
      margin-bottom: 28px;
      box-shadow: var(--sombra-card);
    }
    .search-box-row {
      margin-bottom: 14px;
    }
    .search-input {
      width: 100%;
      padding: 12px 18px 12px 42px;
      border-radius: 30px;
      border: 1.5px solid var(--gaia-borda);
      background: #FCF9F9 url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='18' height='18' viewBox='0 0 24 24' fill='none' stroke='%23853B50' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='11' cy='11' r='8'%3E%3C/circle%3E%3Cline x1='21' y1='21' x2='16.65' y2='16.65'%3E%3C/line%3E%3C/svg%3E") no-repeat 16px center;
      font-family: inherit;
      font-size: 14px;
      color: var(--gaia-texto);
      outline: none;
      transition: all 0.2s;
    }
    .search-input:focus {
      border-color: var(--gaia-vinho);
      background-color: #FFFFFF;
      box-shadow: 0 0 0 3px rgba(133, 59, 80, 0.1);
    }
    .filter-chips-label {
      font-size: 11px;
      font-weight: 700;
      color: var(--gaia-muted);
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 8px;
    }
    .filter-chips-row {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 14px;
    }
    .filter-chip {
      background: #F7EFEF;
      color: var(--gaia-texto);
      border: 1px solid transparent;
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
      user-select: none;
    }
    .filter-chip:hover {
      background: #EEDCDC;
    }
    .filter-chip.active {
      background: var(--gaia-vinho);
      color: #FFFFFF;
      box-shadow: 0 2px 8px rgba(133, 59, 80, 0.2);
    }
    .controls-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
      padding-top: 10px;
      border-top: 1px solid #F4EBEB;
      font-size: 13px;
      color: var(--gaia-muted);
    }
    .sort-select {
      padding: 6px 12px;
      border-radius: 8px;
      border: 1px solid var(--gaia-borda);
      font-family: inherit;
      font-size: 13px;
      color: var(--gaia-vinho);
      font-weight: 600;
      background: #FFF;
      outline: none;
      cursor: pointer;
    }

    /* ══════════════════════════════════════
       CARD DO CARROSSEL INDIVIDUAL
    ══════════════════════════════════════ */
    .carrossel-card {
      background: var(--gaia-card);
      border-radius: var(--radius);
      border: 1px solid var(--gaia-borda);
      box-shadow: var(--sombra-card);
      margin-bottom: 40px;
      overflow: hidden;
      transition: transform 0.2s, box-shadow 0.2s;
    }
    .carrossel-card:hover {
      box-shadow: var(--sombra-hover);
    }
    .carrossel-header {
      padding: 22px 24px 16px;
      background: #FCF9F9;
      border-bottom: 1px solid var(--gaia-borda);
    }
    .carrossel-header-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 8px;
    }
    .carrossel-num-data {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 13px;
      font-weight: 700;
      color: var(--gaia-vinho);
    }
    .carrossel-num-data .num-badge {
      background: var(--gaia-vinho);
      color: white;
      padding: 2px 8px;
      border-radius: 6px;
      font-size: 12px;
    }
    .carrossel-title {
      font-size: clamp(20px, 4vw, 24px);
      font-weight: 800;
      color: var(--gaia-texto);
      line-height: 1.25;
      margin-bottom: 10px;
    }
    .carrossel-subinfo {
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
      font-size: 13.5px;
      color: var(--gaia-muted);
    }
    .carrossel-subinfo b {
      color: var(--gaia-vinho);
    }

    /* Ponto de atenção / Nota clínica */
    .nota-clinica-alert {
      background: #FFF9E6;
      border-left: 4px solid #FFB300;
      padding: 10px 14px;
      margin-top: 12px;
      border-radius: 0 8px 8px 0;
      font-size: 13px;
      color: #6D4C00;
      display: flex;
      align-items: flex-start;
      gap: 8px;
    }

    /* ══════════════════════════════════════
       VISUALIZADOR DO CARROSSEL (SLIDER)
    ══════════════════════════════════════ */
    .carrossel-body {
      padding: 24px;
    }
    @media (max-width: 600px) {
      .carrossel-body {
        padding: 16px;
      }
    }
    .slider-container {
      position: relative;
      max-width: 440px;
      margin: 0 auto 20px;
      background: #1F1619;
      border-radius: 16px;
      overflow: hidden;
      box-shadow: 0 10px 30px rgba(133, 59, 80, 0.2);
    }
    .slider-track {
      display: flex;
      transition: transform 0.35s cubic-bezier(0.25, 1, 0.5, 1);
      width: 100%;
    }
    .slider-slide {
      min-width: 100%;
      aspect-ratio: 4 / 5;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      background: #2A1D22;
    }
    .slider-slide img {
      width: 100%;
      height: 100%;
      object-fit: contain;
      display: block;
      cursor: zoom-in;
    }
    /* Controles do slider */
    .slider-btn {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      width: 42px;
      height: 42px;
      background: rgba(255, 255, 255, 0.88);
      color: var(--gaia-vinho);
      border: none;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      cursor: pointer;
      box-shadow: 0 4px 12px rgba(0,0,0,0.25);
      transition: all 0.2s;
      z-index: 10;
    }
    .slider-btn:hover {
      background: #FFFFFF;
      transform: translateY(-50%) scale(1.08);
      color: var(--gaia-primaria);
    }
    .slider-btn.prev {
      left: 10px;
    }
    .slider-btn.next {
      right: 10px;
    }
    .slider-counter-badge {
      position: absolute;
      bottom: 12px;
      right: 12px;
      background: rgba(0, 0, 0, 0.65);
      backdrop-filter: blur(4px);
      color: white;
      font-size: 12px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 12px;
      letter-spacing: 0.5px;
      z-index: 10;
    }
    .slider-zoom-badge {
      position: absolute;
      top: 12px;
      right: 12px;
      background: rgba(0, 0, 0, 0.55);
      backdrop-filter: blur(4px);
      color: white;
      font-size: 11px;
      font-weight: 600;
      padding: 5px 9px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      gap: 5px;
      cursor: pointer;
      z-index: 10;
      border: 1px solid rgba(255,255,255,0.2);
    }
    .slider-zoom-badge:hover {
      background: rgba(0, 0, 0, 0.8);
    }

    /* Miniaturas de navegação do carrossel */
    .slider-thumbs-strip {
      display: flex;
      gap: 8px;
      justify-content: center;
      overflow-x: auto;
      padding: 6px 4px 12px;
      max-width: 480px;
      margin: 0 auto 20px;
    }
    .slider-thumb-dot {
      width: 44px;
      height: 55px;
      border-radius: 6px;
      overflow: hidden;
      border: 2px solid transparent;
      cursor: pointer;
      opacity: 0.55;
      transition: all 0.2s;
      flex-shrink: 0;
    }
    .slider-thumb-dot img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .slider-thumb-dot.active {
      opacity: 1;
      border-color: var(--gaia-primaria);
      transform: scale(1.06);
      box-shadow: 0 2px 8px rgba(177, 42, 56, 0.3);
    }

    /* ══════════════════════════════════════
       BLOCO DE AÇÕES / APROVAÇÃO WHATSAPP
    ══════════════════════════════════════ */
    .action-approval-box {
      background: #FCF7F8;
      border: 1.5px solid #F0D5DD;
      border-radius: 14px;
      padding: 18px 20px;
      margin-bottom: 22px;
    }
    .action-header-text {
      font-size: 13.5px;
      font-weight: 700;
      color: var(--gaia-vinho);
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .approval-buttons-row {
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
    }
    .btn-aprovar-wpp {
      flex: 1;
      min-width: 220px;
      background: var(--gaia-whatsapp);
      color: white;
      text-decoration: none;
      font-size: 14px;
      font-weight: 700;
      padding: 12px 18px;
      border-radius: 10px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      box-shadow: 0 4px 12px rgba(37, 211, 102, 0.28);
      transition: all 0.2s;
      cursor: pointer;
      border: none;
    }
    .btn-aprovar-wpp:hover {
      background: var(--gaia-whatsapp-dark);
      transform: translateY(-1px);
    }
    .btn-ajustes-toggle {
      background: #FFFFFF;
      color: var(--gaia-alerta);
      border: 1.5px solid #FFCC80;
      font-size: 13.5px;
      font-weight: 700;
      padding: 12px 16px;
      border-radius: 10px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      cursor: pointer;
      transition: all 0.2s;
    }
    .btn-ajustes-toggle:hover {
      background: #FFF8E1;
      border-color: #FFA726;
    }

    /* Painel retrátil de Ajustes */
    .panel-ajustes {
      display: none;
      margin-top: 14px;
      padding-top: 14px;
      border-top: 1px dashed #E6C5CE;
    }
    .panel-ajustes.open {
      display: block;
      animation: fadeIn 0.25s ease;
    }
    .textarea-ajustes {
      width: 100%;
      min-height: 80px;
      border: 1.5px solid #E0B4C0;
      border-radius: 8px;
      padding: 12px;
      font-family: inherit;
      font-size: 13.5px;
      color: var(--gaia-texto);
      outline: none;
      resize: vertical;
      margin-bottom: 10px;
      box-sizing: border-box;
    }
    .textarea-ajustes:focus {
      border-color: var(--gaia-vinho);
      box-shadow: 0 0 0 2px rgba(133, 59, 80, 0.1);
    }
    .btn-enviar-ajustes-wpp {
      background: #F57C00;
      color: white;
      text-decoration: none;
      font-size: 13.5px;
      font-weight: 700;
      padding: 10px 18px;
      border-radius: 8px;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      cursor: pointer;
      border: none;
      transition: background 0.2s;
    }
    .btn-enviar-ajustes-wpp:hover {
      background: #E65100;
    }

    /* ══════════════════════════════════════
       BLOCO DE LEGENDA (COPY)
    ══════════════════════════════════════ */
    .legenda-accordion {
      background: #FCF9F9;
      border: 1px solid var(--gaia-borda);
      border-radius: 12px;
      overflow: hidden;
      margin-top: 10px;
    }
    .legenda-accordion-header {
      padding: 14px 18px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
      user-select: none;
      background: #FCF9F9;
      transition: background 0.2s;
    }
    .legenda-accordion-header:hover {
      background: #F8F0F2;
    }
    .legenda-header-title {
      font-size: 14px;
      font-weight: 700;
      color: var(--gaia-vinho);
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .legenda-header-actions {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .btn-copiar-legenda {
      background: #FFFFFF;
      color: var(--gaia-vinho);
      border: 1px solid var(--gaia-borda);
      font-size: 12px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 6px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      transition: all 0.2s;
    }
    .btn-copiar-legenda:hover {
      background: var(--gaia-vinho);
      color: white;
    }
    .legenda-chevron {
      font-size: 12px;
      color: var(--gaia-muted);
      transition: transform 0.2s;
    }
    .legenda-accordion.open .legenda-chevron {
      transform: rotate(180deg);
    }
    .legenda-content-body {
      display: none;
      padding: 18px;
      border-top: 1px solid var(--gaia-borda);
      background: #FFFFFF;
      font-size: 13.5px;
      color: #3D3336;
      white-space: pre-wrap;
      line-height: 1.65;
      font-family: inherit;
    }
    .legenda-accordion.open .legenda-content-body {
      display: block;
    }

    /* ══════════════════════════════════════
       MODAL DE ZOOM (LIGHTBOX)
    ══════════════════════════════════════ */
    .modal-zoom {
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0, 0, 0, 0.92);
      z-index: 1000;
      padding: 20px;
      align-items: center;
      justify-content: center;
      flex-direction: column;
    }
    .modal-zoom.active {
      display: flex;
    }
    .modal-zoom-img {
      max-width: 96vw;
      max-height: 84vh;
      object-fit: contain;
      border-radius: 8px;
      box-shadow: 0 10px 40px rgba(0,0,0,0.5);
    }
    .modal-close-btn {
      position: absolute;
      top: 16px;
      right: 16px;
      background: rgba(255, 255, 255, 0.2);
      color: white;
      border: none;
      width: 44px;
      height: 44px;
      border-radius: 50%;
      font-size: 24px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .modal-caption {
      color: rgba(255, 255, 255, 0.85);
      font-size: 14px;
      margin-top: 12px;
      text-align: center;
    }

    /* ══════════════════════════════════════
       MENU FLUTUANTE DE ATALHO RÁPIDO
    ══════════════════════════════════════ */
    .quick-fab-btn {
      position: fixed;
      bottom: 24px;
      right: 20px;
      background: var(--gaia-vinho);
      color: white;
      border: none;
      width: 52px;
      height: 52px;
      border-radius: 50%;
      box-shadow: 0 6px 20px rgba(133, 59, 80, 0.35);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 22px;
      z-index: 99;
      transition: transform 0.2s;
    }
    .quick-fab-btn:hover {
      transform: scale(1.08);
      background: var(--gaia-primaria);
    }

    .quick-drawer {
      display: none;
      position: fixed;
      bottom: 86px;
      right: 20px;
      width: min(340px, 90vw);
      max-height: 70vh;
      background: #FFFFFF;
      border: 1px solid var(--gaia-borda);
      border-radius: 16px;
      box-shadow: 0 12px 35px rgba(0,0,0,0.18);
      z-index: 99;
      overflow-y: auto;
      padding: 16px;
    }
    .quick-drawer.open {
      display: block;
      animation: fadeIn 0.2s ease;
    }
    .quick-drawer h3 {
      font-size: 14px;
      font-weight: 700;
      color: var(--gaia-vinho);
      margin-bottom: 10px;
      padding-bottom: 6px;
      border-bottom: 1px solid var(--gaia-borda);
    }
    .quick-drawer-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .quick-drawer-link {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 6px 8px;
      border-radius: 8px;
      color: var(--gaia-texto);
      text-decoration: none;
      font-size: 13px;
      transition: background 0.15s;
    }
    .quick-drawer-link:hover {
      background: #FDF2F5;
      color: var(--gaia-vinho);
    }
    .quick-drawer-link .q-num {
      background: #EEDCDC;
      color: var(--gaia-vinho);
      font-size: 11px;
      font-weight: 800;
      padding: 2px 6px;
      border-radius: 4px;
    }

    /* Animações e Utilitários */
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .toast-msg {
      position: fixed;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%);
      background: #2D2427;
      color: white;
      padding: 10px 20px;
      border-radius: 30px;
      font-size: 13.5px;
      font-weight: 600;
      box-shadow: 0 4px 15px rgba(0,0,0,0.25);
      z-index: 2000;
      display: none;
    }
  </style>
</head>
<body>

  <!-- TOAST NOTIFICATION -->
  <div id="toast" class="toast-msg">Mensagem</div>

  <!-- HEADER HERO -->
  <header class="header-hero">
    <div class="header-content">
      <div class="brand-tag"><span></span> Gaia Medicina Integrada · Outubro 2026</div>
      <h1>Outubro Rosa & Calendário Oficial</h1>
      <p>Portal exclusivo para navegação, revisão clínica e aprovação individual de cada carrossel da programação de Outubro.</p>
      
      <div class="hero-badges">
        <div class="hero-badge">📅 <b>15</b> Carrosséis Prontos</div>
        <div class="hero-badge">🎨 <b>106</b> Cards Finalizados</div>
        <div class="hero-badge">🌸 <b>4</b> Datas Fixas</div>
        <div class="hero-badge">💬 <b>Aprovação 100% via WhatsApp</b></div>
      </div>
    </div>
  </header>

  <!-- BARRA DE NAVEGAÇÃO STICKY -->
  <nav class="sticky-nav">
    <div class="sticky-nav-inner">
      <div class="nav-tabs">
        <a href="#calendario" class="nav-tab-btn active" onclick="setActiveTab(this)">📅 Calendário Sugerido</a>
        <a href="#carrosseis" class="nav-tab-btn" onclick="setActiveTab(this)">📱 Ver Carrosséis (15)</a>
      </div>
      <a href="https://api.whatsapp.com/send?text=Ol%C3%A1%21%20Revisei%20o%20Calend%C3%A1rio%20Geral%20de%20Publica%C3%A7%C3%B5es%20de%20Outubro%20da%20Gaia%20Medicina%20Integrada%20%2815%20pe%C3%A7as%2C%2012%2F10%20a%2031%2F10%29%20e%20est%C3%A1%20APROVADO%20para%20publica%C3%A7%C3%A3o%21" target="_blank" class="nav-quick-btn">
        ✅ Aprovar Calendário no WhatsApp
      </a>
    </div>
  </nav>

  <main class="container">

    <!-- ══════════════════════════════════════════════════════
         SEÇÃO: CALENDÁRIO SUGERIDO DE PUBLICAÇÕES
    ══════════════════════════════════════════════════════ -->
    <section id="calendario" class="section-card">
      <div class="section-header">
        <div class="section-header-left">
          <h2>📅 Calendário Sugerido de Publicações</h2>
          <p>Sequência cronológica completa dos 15 carrosséis com datas, capas e responsáveis pela revisão clínica.</p>
        </div>
      </div>

      <!-- CARD DE APROVAÇÃO DO CALENDÁRIO GERAL VIA WHATSAPP -->
      <div class="calendario-aprovacao-box">
        <div class="cal-box-header">
          <div class="cal-box-icon">📋</div>
          <div class="cal-box-title">
            <h3>Aprovação do Calendário Completo de Outubro</h3>
            <p>As 4 datas comemorativas são fixas no calendário; as demais publicações podem ser ajustadas conforme a preferência da equipe clínica.</p>
          </div>
        </div>
        <div class="cal-box-actions">
          <a href="https://api.whatsapp.com/send?text=Ol%C3%A1%21%20Revisei%20o%20Calend%C3%A1rio%20Geral%20de%20Publica%C3%A7%C3%B5es%20de%20Outubro%20da%20Gaia%20Medicina%20Integrada%20%2815%20pe%C3%A7as%2C%2012%2F10%20a%2031%2F10%29%20e%20est%C3%A1%20APROVADO%20para%20publica%C3%A7%C3%A3o%21" 
             target="_blank" 
             class="btn-wpp-calendario">
            ✅ Aprovar Calendário Completo no WhatsApp
          </a>
          <a href="https://api.whatsapp.com/send?text=Ol%C3%A1%21%20Sobre%20o%20Calend%C3%A1rio%20de%20Publica%C3%A7%C3%B5es%20de%20Outubro%20da%20Gaia%2C%20gostaria%20de%20sugerir%20o%20seguinte%20ajuste%20de%20data%3A%20" 
             target="_blank" 
             class="btn-wpp-ajuste">
            💬 Sugerir Mudança de Data no WhatsApp
          </a>
        </div>
      </div>

      <!-- SEMANA 1 -->
      <div class="semana-group">
        <div class="semana-title">
          <span>Semana 1 · 12 a 18 de Outubro</span>
          <span>6 publicações</span>
        </div>
        <div class="timeline-list">
"""

# Group items into weeks
# Semana 1: 12 to 18
# Semana 2: 19 to 25 (20, 21, 22, 24)
# Semana 3: 26 to 31 (27, 28, 29, 30, 31)

def render_timeline_item(c):
    return f"""          <div class="timeline-item">
            <div class="time-dia-box">
              <div class="time-dia-num">{c['dia_mes'][:2]}</div>
              <div class="time-dia-sem">{c['dia_semana'][:3]}</div>
            </div>
            <img src="outubro-rosa/{c['id']}/1.jpg" alt="Capa Carrossel {c['id']}" class="timeline-thumb" onclick="irParaCarrossel('{c['id']}')" title="Clique para ver o carrossel"/>
            <div class="timeline-info">
              <div style="display:flex; gap:6px; flex-wrap:wrap; align-items:center;">
                <span class="badge-linha {c['pilar_slug']}">{c['pilar_badge']}</span>
                {'<span class="badge-fixa">Data Fixa</span>' if c['data_fixa'] else ''}
              </div>
              <h4>{html.escape(c['titulo'])}</h4>
              <div class="timeline-meta">Revisão: <b>{html.escape(c['medica'])}</b> · Carrossel {c['id']} · {c['num_slides']} cards</div>
            </div>
            <div class="timeline-btn-col">
              <button class="btn-ir-carrossel" onclick="irParaCarrossel('{c['id']}')">Ver Cards &rarr;</button>
            </div>
          </div>"""

# Append items
s1 = [c for c in carousels_by_date if c['data_ordem'] <= '2026-10-18']
s2 = [c for c in carousels_by_date if '2026-10-19' <= c['data_ordem'] <= '2026-10-25']
s3 = [c for c in carousels_by_date if c['data_ordem'] >= '2026-10-26']

for c in s1:
    html_content += render_timeline_item(c) + "\n"

html_content += """        </div>
      </div>

      <!-- SEMANA 2 -->
      <div class="semana-group">
        <div class="semana-title">
          <span>Semana 2 · 20 a 24 de Outubro</span>
          <span>4 publicações</span>
        </div>
        <div class="timeline-list">
"""

for c in s2:
    html_content += render_timeline_item(c) + "\n"

html_content += """        </div>
      </div>

      <!-- SEMANA 3 -->
      <div class="semana-group">
        <div class="semana-title">
          <span>Semana 3 · 27 a 31 de Outubro</span>
          <span>5 publicações</span>
        </div>
        <div class="timeline-list">
"""

for c in s3:
    html_content += render_timeline_item(c) + "\n"

html_content += """        </div>
      </div>
    </section>

    <!-- ══════════════════════════════════════════════════════
         SEÇÃO: CONTROLES & FILTROS DE CARROSSÉIS
    ══════════════════════════════════════════════════════ -->
    <section id="carrosseis" class="controls-wrapper">
      <div class="search-box-row">
        <input type="text" id="searchInput" class="search-input" placeholder="Buscar carrossel por título, tema, palavra da legenda ou número..." oninput="filtrarCarrosseis()"/>
      </div>
      
      <div class="filter-chips-label">Filtrar por Médica Revisora:</div>
      <div class="filter-chips-row">
        <button class="filter-chip active" data-filter="all" onclick="filtrarPorMedica('all', this)">Todas as Médicas (15)</button>
        <button class="filter-chip" data-filter="andrea" onclick="filtrarPorMedica('andrea', this)">Dra. Andrea / Mastologia (6)</button>
        <button class="filter-chip" data-filter="katia" onclick="filtrarPorMedica('katia', this)">Dra. Katia (5)</button>
        <button class="filter-chip" data-filter="nathalia" onclick="filtrarPorMedica('nathalia', this)">Dra. Nathalia (3)</button>
        <button class="filter-chip" data-filter="equipe" onclick="filtrarPorMedica('equipe', this)">Equipe Gaia (2)</button>
      </div>

      <div class="filter-chips-label">Filtrar por Linha Editorial / Pilar:</div>
      <div class="filter-chips-row">
        <button class="filter-chip active" data-pilar="all" onclick="filtrarPorPilar('all', this)">Todos os Pilares</button>
        <button class="filter-chip" data-pilar="rosa" onclick="filtrarPorPilar('rosa', this)">🌸 Outubro Rosa</button>
        <button class="filter-chip" data-pilar="katia" onclick="filtrarPorPilar('katia', this)">🧸 Dicas da Tia Katia</button>
        <button class="filter-chip" data-pilar="hpv" onclick="filtrarPorPilar('hpv', this)">🔬 Ginecologia & HPV</button>
        <button class="filter-chip" data-pilar="adol" onclick="filtrarPorPilar('adol', this)">🌱 Adolescência</button>
        <button class="filter-chip" data-pilar="inst" onclick="filtrarPorPilar('inst', this)">🩺 Institucional</button>
      </div>

      <div class="controls-footer">
        <div>Mostrando <b id="countVisiveis">15</b> de <b>15</b> carrosséis</div>
        <div>
          <label for="sortSelect">Ordenar por: </label>
          <select id="sortSelect" class="sort-select" onchange="reordenarCarrosseis(this.value)">
            <option value="cronologica">Data de Publicação (Cronológica)</option>
            <option value="numero">Número do Carrossel (01 a 15)</option>
          </select>
        </div>
      </div>
    </section>

    <!-- ══════════════════════════════════════════════════════
         LISTA DOS 15 CARROSSÉIS INDIVIDUAIS
    ══════════════════════════════════════ -->
    <div id="carrosseisContainer">
"""

# Function to render individual carousel block
def render_carousel_card(c):
    cid = c['id']
    num_slides = c['num_slides']
    titulo_escaped = html.escape(c['titulo'])
    medica_escaped = html.escape(c['medica'])
    data_escaped = html.escape(c['data'])
    legenda_escaped = html.escape(c['legenda'])
    
    # Pre-encoded WhatsApp approval text
    msg_aprovar = (
        f"Olá! Acabei de revisar o Carrossel {cid} da Gaia ({c['titulo']} - {c['data']}) "
        f"e está APROVADO para publicação sem alterações! Revisora: {c['medica']}."
    )
    import urllib.parse
    wpp_aprovar_url = f"https://api.whatsapp.com/send?text={urllib.parse.quote(msg_aprovar)}"

    # Generate slides HTML
    slides_html = ""
    thumbs_html = ""
    for i in range(1, num_slides + 1):
        img_src = f"outubro-rosa/{cid}/{i}.jpg"
        slides_html += f"""            <div class="slider-slide">
              <img src="{img_src}" alt="Card {i} - Carrossel {cid}" loading="lazy" onclick="abrirZoom('{img_src}', 'Card {i} de {num_slides} · Carrossel {cid}')"/>
            </div>\n"""
        thumbs_html += f"""          <div class="slider-thumb-dot {'active' if i == 1 else ''}" onclick="irParaSlide('{cid}', {i - 1})">
            <img src="{img_src}" alt="Thumb {i}"/>
          </div>\n"""

    return f"""
      <article id="carrossel-{cid}" 
               class="carrossel-card" 
               data-id="{cid}" 
               data-medica="{c['medica_tag']}" 
               data-pilar="{c['pilar_slug']}" 
               data-data="{c['data_ordem']}">
        <div class="carrossel-header">
          <div class="carrossel-header-top">
            <div class="carrossel-num-data">
              <span class="num-badge">Carrossel #{cid}</span>
              <span>📅 {data_escaped}</span>
            </div>
            <div style="display:flex; gap:6px; align-items:center;">
              <span class="badge-linha {c['pilar_slug']}">{c['pilar_badge']}</span>
              {'<span class="badge-fixa">Data Fixa</span>' if c['data_fixa'] else ''}
            </div>
          </div>
          <h3 class="carrossel-title">{titulo_escaped}</h3>
          <div class="carrossel-subinfo">
            <span>Revisão Clínica: <b>{medica_escaped}</b></span>
            <span>·</span>
            <span>Total: <b>{num_slides} cards</b></span>
            <span>·</span>
            <span>Origem: <i>{html.escape(c['origem'])}</i></span>
          </div>
          {f'<div class="nota-clinica-alert"><span>⚠️</span> <div><b>Atenção clínica:</b> {html.escape(c["nota"])}</div></div>' if c['nota'] else ''}
        </div>

        <div class="carrossel-body">
          <!-- VISUALIZADOR SLIDER -->
          <div class="slider-container" id="slider-{cid}">
            <div class="slider-zoom-badge" onclick="abrirZoom('outubro-rosa/{cid}/1.jpg', 'Card 1 de {num_slides} · Carrossel {cid}')">
              🔍 Expandir
            </div>
            <div class="slider-counter-badge" id="counter-{cid}">
              Card 1 de {num_slides}
            </div>
            <button class="slider-btn prev" onclick="mudarSlide('{cid}', -1)">&lsaquo;</button>
            <div class="slider-track" id="track-{cid}">
{slides_html}            </div>
            <button class="slider-btn next" onclick="mudarSlide('{cid}', 1)">&rsaquo;</button>
          </div>

          <!-- MINIATURAS THUMBS -->
          <div class="slider-thumbs-strip" id="thumbs-{cid}">
{thumbs_html}          </div>

          <!-- ÁREA DE APROVAÇÃO WHATSAPP -->
          <div class="action-approval-box">
            <div class="action-header-text">
              <span>💬</span> Ação de Revisão para este Carrossel:
            </div>
            <div class="approval-buttons-row">
              <a href="{wpp_aprovar_url}" target="_blank" class="btn-aprovar-wpp">
                ✅ Aprovar Carrossel #{cid} no WhatsApp
              </a>
              <button type="button" class="btn-ajustes-toggle" onclick="togglePainelAjustes('{cid}')">
                ✏️ Solicitar Ajustes
              </button>
            </div>

            <!-- PAINEL RETRÁTIL PARA AJUSTES -->
            <div class="panel-ajustes" id="painel-ajustes-{cid}">
              <textarea class="textarea-ajustes" id="texto-ajustes-{cid}" placeholder="Digite aqui o que você gostaria de ajustar neste carrossel (ex: revisar frase do slide 3, trocar termo clínico...)..."></textarea>
              <button type="button" class="btn-enviar-ajustes-wpp" onclick="enviarAjustesWpp('{cid}', '{html.escape(c['titulo'])}', '{c['data']}', '{html.escape(c['medica'])}')">
                📲 Enviar Ajustes via WhatsApp
              </button>
            </div>
          </div>

          <!-- ACCORDION LEGENDA SUGERIDA -->
          <div class="legenda-accordion" id="legenda-acc-{cid}">
            <div class="legenda-accordion-header" onclick="toggleLegenda('{cid}')">
              <div class="legenda-header-title">
                <span>📝</span> Legenda Sugerida da Postagem (Copy)
              </div>
              <div class="legenda-header-actions">
                <button type="button" class="btn-copiar-legenda" onclick="copiarLegenda('{cid}', event)">
                  📋 Copiar Legenda
                </button>
                <span class="legenda-chevron">&or;</span>
              </div>
            </div>
            <div class="legenda-content-body" id="legenda-text-{cid}">{legenda_escaped}</div>
          </div>
        </div>
      </article>"""

# Render all carousels sorted chronologically
for c in carousels_by_date:
    html_content += render_carousel_card(c) + "\n"

html_content += """    </div>
  </main>

  <!-- MODAL DE ZOOM LIGHTBOX -->
  <div class="modal-zoom" id="modalZoom" onclick="fecharZoom()">
    <button class="modal-close-btn" onclick="fecharZoom()">&times;</button>
    <img src="" alt="Zoom" id="modalZoomImg" class="modal-zoom-img" onclick="event.stopPropagation()"/>
    <div class="modal-caption" id="modalZoomCaption"></div>
  </div>

  <!-- MENU FLUTUANTE DE ATALHO RÁPIDO -->
  <button class="quick-fab-btn" onclick="toggleQuickDrawer()" title="Ir rápido para um carrossel">
    ☰
  </button>
  <div class="quick-drawer" id="quickDrawer">
    <h3>Pular para o Carrossel:</h3>
    <ul class="quick-drawer-list">
"""

for c in carousels_by_date:
    html_content += f"""      <li>
        <a href="#carrossel-{c['id']}" class="quick-drawer-link" onclick="toggleQuickDrawer()">
          <span class="q-num">#{c['id']}</span>
          <span>{c['dia_mes']} · {html.escape(c['titulo'][:28])}...</span>
        </a>
      </li>\n"""

html_content += """    </ul>
  </div>

  <!-- JAVASCRIPT DE INTERATIVIDADE -->
  <script>
    // Estado de cada carrossel
    const carrosselState = {};
    const totalSlides = {
"""

for c in carousels:
    html_content += f"      '{c['id']}': {c['num_slides']},\n"

html_content += """    };

    // Inicialização
    document.addEventListener('DOMContentLoaded', () => {
      Object.keys(totalSlides).forEach(id => {
        carrosselState[id] = 0;
        configurarSwipeTouch(id);
      });
    });

    // Mudar slide via botões
    function mudarSlide(id, delta) {
      const total = totalSlides[id];
      let atual = carrosselState[id] || 0;
      atual = (atual + delta + total) % total;
      irParaSlide(id, atual);
    }

    // Ir para slide específico
    function irParaSlide(id, index) {
      carrosselState[id] = index;
      const track = document.getElementById(`track-${id}`);
      if (track) {
        track.style.transform = `translateX(-${index * 100}%)`;
      }
      // Atualizar contador
      const counter = document.getElementById(`counter-${id}`);
      if (counter) {
        counter.textContent = `Card ${index + 1} de ${totalSlides[id]}`;
      }
      // Atualizar miniaturas
      const thumbs = document.getElementById(`thumbs-${id}`);
      if (thumbs) {
        const dots = thumbs.querySelectorAll('.slider-thumb-dot');
        dots.forEach((d, i) => {
          d.classList.toggle('active', i === index);
        });
      }
      // Atualizar zoom badge
      const slider = document.getElementById(`slider-${id}`);
      if (slider) {
        const zoomBadge = slider.querySelector('.slider-zoom-badge');
        if (zoomBadge) {
          zoomBadge.onclick = () => abrirZoom(`outubro-rosa/${id}/${index + 1}.jpg`, `Card ${index + 1} de ${totalSlides[id]} · Carrossel ${id}`);
        }
      }
    }

    // Suporte a swipe no mobile
    function configurarSwipeTouch(id) {
      const container = document.getElementById(`slider-${id}`);
      if (!container) return;
      let startX = 0;
      let endX = 0;

      container.addEventListener('touchstart', (e) => {
        startX = e.touches[0].clientX;
      }, { passive: true });

      container.addEventListener('touchend', (e) => {
        endX = e.changedTouches[0].clientX;
        const diff = startX - endX;
        if (Math.abs(diff) > 40) {
          if (diff > 0) {
            mudarSlide(id, 1);
          } else {
            mudarSlide(id, -1);
          }
        }
      }, { passive: true });
    }

    // Navegar até o carrossel a partir do calendário
    function irParaCarrossel(id) {
      const el = document.getElementById(`carrossel-${id}`);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'start' });
        el.style.transition = 'box-shadow 0.4s';
        el.style.boxShadow = '0 0 0 3px #B12A38, 0 14px 40px rgba(133,59,80,0.2)';
        setTimeout(() => {
          el.style.boxShadow = '';
        }, 1800);
      }
    }

    // Modal de Zoom
    function abrirZoom(src, caption) {
      const modal = document.getElementById('modalZoom');
      const img = document.getElementById('modalZoomImg');
      const cap = document.getElementById('modalZoomCaption');
      img.src = src;
      cap.textContent = caption || '';
      modal.classList.add('active');
    }

    function fecharZoom() {
      document.getElementById('modalZoom').classList.remove('active');
    }

    // Painel de ajustes retrátil
    function togglePainelAjustes(id) {
      const painel = document.getElementById(`painel-ajustes-${id}`);
      if (painel) {
        painel.classList.toggle('open');
        if (painel.classList.contains('open')) {
          const txt = document.getElementById(`texto-ajustes-${id}`);
          if (txt) txt.focus();
        }
      }
    }

    // Enviar ajustes via WhatsApp
    function enviarAjustesWpp(id, titulo, data, medica) {
      const txt = document.getElementById(`texto-ajustes-${id}`);
      const observacao = txt ? txt.value.trim() : '';
      if (!observacao) {
        alert('Por favor, descreva brevemente os ajustes solicitados antes de enviar no WhatsApp.');
        return;
      }
      const msg = `Olá! Sobre o Carrossel ${id} da Gaia ("${titulo}", previsto para ${data}), gostaria de solicitar os seguintes ajustes:\n\n${observacao}\n\nRevisora: ${medica}.`;
      const url = `https://api.whatsapp.com/send?text=${encodeURIComponent(msg)}`;
      window.open(url, '_blank');
    }

    // Accordion da Legenda
    function toggleLegenda(id) {
      const acc = document.getElementById(`legenda-acc-${id}`);
      if (acc) {
        acc.classList.toggle('open');
      }
    }

    // Copiar Legenda com 1 clique
    function copiarLegenda(id, event) {
      event.stopPropagation();
      const textEl = document.getElementById(`legenda-text-${id}`);
      if (textEl) {
        const text = textEl.innerText;
        navigator.clipboard.writeText(text).then(() => {
          mostrarToast('✅ Legenda copiada para a área de transferência!');
        }).catch(() => {
          mostrarToast('Erro ao copiar legenda.');
        });
      }
    }

    // Toast de notificação
    function mostrarToast(msg) {
      const t = document.getElementById('toast');
      t.textContent = msg;
      t.style.display = 'block';
      setTimeout(() => {
        t.style.display = 'none';
      }, 2500);
    }

    // Menu rápido gaveta
    function toggleQuickDrawer() {
      const d = document.getElementById('quickDrawer');
      d.classList.toggle('open');
    }

    // Tabs do topo
    function setActiveTab(el) {
      document.querySelectorAll('.nav-tab-btn').forEach(btn => btn.classList.remove('active'));
      el.classList.add('active');
    }

    // FILTROS
    let filtroMedicaAtual = 'all';
    let filtroPilarAtual = 'all';

    function filtrarPorMedica(medica, btn) {
      filtroMedicaAtual = medica;
      const container = btn.parentElement;
      container.querySelectorAll('.filter-chip').forEach(c => c.classList.remove('active'));
      btn.classList.add('active');
      aplicarFiltros();
    }

    function filtrarPorPilar(pilar, btn) {
      filtroPilarAtual = pilar;
      const container = btn.parentElement;
      container.querySelectorAll('.filter-chip').forEach(c => c.classList.remove('active'));
      btn.classList.add('active');
      aplicarFiltros();
    }

    function filtrarCarrosseis() {
      aplicarFiltros();
    }

    function aplicarFiltros() {
      const query = (document.getElementById('searchInput').value || '').toLowerCase().trim();
      const cards = document.querySelectorAll('.carrossel-card');
      let visiveis = 0;

      cards.forEach(card => {
        const medica = card.getAttribute('data-medica');
        const pilar = card.getAttribute('data-pilar');
        const textContent = card.innerText.toLowerCase();

        const matchMedica = (filtroMedicaAtual === 'all') || (medica === filtroMedicaAtual);
        const matchPilar = (filtroPilarAtual === 'all') || (pilar === filtroPilarAtual);
        const matchQuery = !query || textContent.includes(query);

        if (matchMedica && matchPilar && matchQuery) {
          card.style.display = 'block';
          visiveis++;
        } else {
          card.style.display = 'none';
        }
      });

      document.getElementById('countVisiveis').textContent = visiveis;
    }

    // Reordenar carrosséis
    function reordenarCarrosseis(criterio) {
      const container = document.getElementById('carrosseisContainer');
      const cards = Array.from(container.querySelectorAll('.carrossel-card'));

      cards.sort((a, b) => {
        if (criterio === 'cronologica') {
          return a.getAttribute('data-data').localeCompare(b.getAttribute('data-data'));
        } else {
          return parseInt(a.getAttribute('data-id'), 10) - parseInt(b.getAttribute('data-id'), 10);
        }
      });

      cards.forEach(c => container.appendChild(c));
    }
  </script>
</body>
</html>
"""

# Write file in proposta/preview-carrosseis-outubro.html
output_file = os.path.join(os.path.dirname(__file__), 'preview-carrosseis-outubro.html')
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Successfully generated {output_file} ({len(html_content)} bytes)")

# Also create outubro-rosa.html as identical copy for convenience
copy_file = os.path.join(os.path.dirname(__file__), 'outubro-rosa.html')
with open(copy_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

# Also create local copy in CRIACAO - CARROSEL/Outubro Rosa 2026/
local_dest = r'g:\00 - CLIENTES\02_GAIA\CRIACAO - CARROSEL\Outubro Rosa 2026\preview-carrosseis-outubro.html'
with open(local_dest, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("All files generated and synced successfully!")
