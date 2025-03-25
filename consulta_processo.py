from playwright.sync_api import sync_playwright
from datetime import datetime
from constants.entities import Tramitacao, Tramitacoes

def buscar_processo(n_processo:str) -> Tramitacoes:
    with sync_playwright() as p:
        # Iniciar o navegador (modo headless)
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Acessar a página
        page.goto(f"https://suite.ce.gov.br/consultar-processo/{n_processo}")

        page.wait_for_timeout(3500)  # Aguarda 3.5 segundos (3500 milissegundos)

        # Esperar o carregamento do 'timeline-container'
        page.wait_for_selector(".timeline-container", state="visible")

        # Capturar os elementos 'timeline-panel'
        panels = page.query_selector_all(".timeline-panel")

        print(f"Número de tramitações: {len(panels)}")
        n_tramitacoes = len(panels)

        tramitacoes = Tramitacoes()
        for i, panel in enumerate(panels, start=1):
            
            data_hora_processo = panel.query_selector("h4") 
            tempo_permanencia_setor = panel.query_selector("div.timeline-heading > h5 > span")
            nome_setor = panel.query_selector("div.timeline-body > div > p:nth-child(2) > span:nth-child(2)")

            situacao = panel.query_selector("div.timeline-body > div > p:nth-child(1)")
            tramitacao = Tramitacao()
            if data_hora_processo:

                data_inicio, hora_inicio = data_hora_processo.inner_text().split('-')
                datetime_inicio = datetime.strptime(data_inicio + " " + hora_inicio, "%d/%m/%Y %H:%M")
                
                tramitacao.setor = nome_setor.inner_text()
                tramitacao.inicio = datetime_inicio
                tramitacao.situacao = situacao.inner_text().split(':')[1]
                
                if n_tramitacoes != 1:
                    tramitacao.tempo_permanencia = tempo_permanencia_setor.inner_text()

            else:
                print(f"O processo não tem tramitações em aberto.")
            
            tramitacoes.adicionar_tramitacao(tramitacao)
            n_tramitacoes = n_tramitacoes -1

        tramitacoes.listar_tramitacoes()
        browser.close()
        return tramitacoes