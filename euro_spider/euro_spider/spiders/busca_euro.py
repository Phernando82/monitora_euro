import scrapy
from datetime import datetime
from utils.email_sender import Emailer

USERNAME = 'dev.tokyme@gmail.com'
PASSWORD = 'ewbmiujxjjpwhqsy'


class PriceScraperSpider(scrapy.Spider):
    # identidade
    name = 'eurobot'

    # Request

    def start_requests(self):
        urls = ['https://www.investing.com/currencies/eur-brl']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Response
    def parse(self, response):
        euro = response.xpath(
            "//span[@data-test='instrument-price-last']/text()")[0].get()

        if float(euro) > 5.0441:
            email = Emailer(USERNAME, PASSWORD)
            lista_de_contatos = ['fernandoperesvalverde@gmail.com']
            email.definir_conteudo('Euro está subindo', 'dev.tokyme@gmail.com',
                                   lista_de_contatos,
                                   f'O Euro  acabou de subir para {euro}, favor verificar se agora é um bom momento para comprar Euro.')

            email.enviar_email(30)
