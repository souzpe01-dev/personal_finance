import os
import json
from datetime import datetime
from io import BytesIO
import plotly.express as px
import matplotlib.ticker as ticker
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import locale
import numpy as np

st.title('DashBoard Controle de Custos')

# ============================================
#               Leitura
# ============================================


df_2024_dez_raw = pd.read_csv(
    "C:\\Users\\pedro\\OneDrive\\Desktop\\ControleGastos\\Nubank_2024-12-01.csv",  sep=',')
df_2024_dez_raw['year_month'] = 202412

df_2025_jan_raw = pd.read_csv(
    "C:\\Users\\pedro\\OneDrive\\Desktop\\ControleGastos\\Nubank_2025-01-01.csv",  sep=',')
df_2025_jan_raw['year_month'] = 202501

df_2025_fev_raw = pd.read_csv(
    "C:\\Users\\pedro\\OneDrive\\Desktop\\ControleGastos\\Nubank_2025-02-01.csv",  sep=',')
df_2025_fev_raw['year_month'] = 202502

df_2025_mar_raw = pd.read_csv(
    "C:\\Users\\pedro\\OneDrive\\Desktop\\ControleGastos\\Nubank_2025-03-01.csv",  sep=',')
df_2025_mar_raw['year_month'] = 202503

df_2025_abr_raw = pd.read_csv(
    "C:\\Users\\pedro\\OneDrive\\Desktop\\ControleGastos\\Nubank_2025-04-01.csv",  sep=',')
df_2025_abr_raw['year_month'] = 202504

df_2025_mai_raw = pd.read_csv(
    "C:\\Users\\pedro\\OneDrive\\Desktop\\ControleGastos\\Nubank_2025-05-01.csv",  sep=',')
df_2025_mai_raw['year_month'] = 202505

df_2025_jun_raw = pd.read_csv(
    "C:\\Users\\pedro\\OneDrive\\Desktop\\ControleGastos\\Nubank_2025-06-01.csv",  sep=',')
df_2025_jun_raw['year_month'] = 202506

df_2025_jul_raw = pd.read_csv(
    "C:\\Users\\pedro\\OneDrive\\Desktop\\ControleGastos\\Nubank_2025-07-01.csv",  sep=',')
df_2025_jul_raw['year_month'] = 202507

df_2025_ago_raw = pd.read_csv(
    "C:\\Users\\pedro\\OneDrive\\Desktop\\ControleGastos\\Nubank_2025-08-01.csv",  sep=',')
df_2025_ago_raw['year_month'] = 202508

# =========== Uniom

df_unified = pd.concat([df_2024_dez_raw, df_2025_jan_raw, df_2025_fev_raw, df_2025_mar_raw,
                       df_2025_abr_raw, df_2025_mai_raw, df_2025_jun_raw, df_2025_jul_raw, df_2025_ago_raw])
df_unified = df_unified[df_unified['amount'] > 0]


# ======================================== CLASSIFICAÇÂO ========================================

# --------------------------------------------------
#                   RESTAURANTES
# --------------------------------------------------

RESTAURANTES = 'Restaurantes'
# --- SUB
ADELIA = 'Adelia'
RESTANDORINHA = 'Restaurantes Andorinha'
ALEATORIOS = 'Aleatorios'
DELIVERY = 'DELIVERY'


# --------------------------------------------------
#                   ASSINATURAS
# --------------------------------------------------

# ====== CAT
ASSINATURAS = 'Assinaturas'
# ---SUB
AMAZONPRIME = 'Amazon Prime'
AMAZONMUSIC = 'Amazon Music'
AMAZONALUGUEL = 'Amazon Prime Aluguel'
AMAZONCANAIS = 'Amazon Prime Canais'
HBOMAX = 'HBO'
NETFLIX = 'Netflix'
APPLETV = 'Apple TV'
DISNEY = 'Disney TV'
YTMUSIC = 'YT Music Premium'
TCL = 'TLC'
GYMPASS = 'GYMPASS'
IFOODCLUB = 'IfoodClub'
UBERONE = 'Uber One'
IV10 = 'Investidor10'
ALURA = 'Alura'
DATING = 'Dating'
STREAMING = 'Streaming'
AVAST = 'Avast'

# --------------------------------------------------
#                   ROLES
# --------------------------------------------------

# ====== CAT
ROLES = 'Roles'
# ---SUB
BARESREST = 'Barzinho e Restaurantes'
BEBIDAS = 'Compra de Bebidas'
PASSEIO = 'Passeio'
HOSPEDAGEM = 'Hospedagem'

# --------------------------------------------------
#                   BARBEIRO
# --------------------------------------------------

# ====== CAT
BARBEIRO = 'Barbeiro'
# ---SUB
LAUZANGELES = 'Lauzangeles'
BARBEMP = 'Barbearia Imperial'

# --------------------------------------------------
#                   CARRO
# --------------------------------------------------

# ====== CAT
CARRO = 'Carro'
# ---SUB
REVISAO = 'Revisao'
SEGURO = 'Seguro'
PNEU = 'Pneu'
ABASTECIMENTO = 'Abastecimento'
ESTACIONAMENTOS = 'Estacionamento'
LAVARAPIDO = 'Lava Rapido'
FUNILARIA = 'Funilaria'
MERCADOCAR = 'MercadoCar'
BORRACHARIA = 'Borracharia'
SEMPARAR = 'Sem Parar'


# --------------------------------------------------
#                   MERCADO
# --------------------------------------------------

# ====== CAT
MERCADO = 'Mercado'
# ---SUB
SUPERMERCADO = 'Supermercado'
SWIFT = 'Swift'
MINIEXTRA = 'MiniExtra'
ACOUGUE = 'Açougue'
MERCADINHOCOND = 'Mercadinho Condominio'

# --------------------------------------------------
#                   ESPORTES
# --------------------------------------------------

# ====== CAT
ESPORTES = 'Esportes'

# ---SUB
ACESSORIOSCICLISMO = 'Acessorios Ciclismo'
HIDR = 'Hidratação'
COMPRABIKE = 'Compra da Bike'

# --------------------------------------------------
#                   COMPRAS
# --------------------------------------------------

# ====== CAT
COMPRAS = 'Compras'

# ---SUB
ROUPAS = 'Roupas'
PARCELATV = 'Parcela TV'
PRESENTES = 'Presentes'
OUTROS = 'Outros'
PARCELACELULAR = 'Parcela Celular'

# --------------------------------------------------
#                   SAUDE
# --------------------------------------------------

# ====== CAT
SAUDE = 'Saude'

# ---SUB
FARMACIA = 'Farmacia'
SUPLEMENTOS = 'SUPLEMENTOS'

# --------------------------------------------------
#                   SAUDE
# --------------------------------------------------

TRANSPORTE = 'Transporte'
UBER = 'Uber'

MAP = [

    # ============ Restaurantes ===============
    ['Casa de Adelia-Restau', RESTAURANTES, ADELIA],
    ['Burger King', RESTAURANTES, ALEATORIOS],
    ['Buzzini Comercio de Al', RESTAURANTES, RESTANDORINHA],
    ['Casa da Esfiha', RESTAURANTES, ALEATORIOS],
    ['Charles Dogs', RESTAURANTES, ALEATORIOS],
    ['Gigantedaserra', RESTAURANTES, ALEATORIOS],
    ['Ifd*52628155 Aislan Ap', RESTAURANTES, DELIVERY],
    ['Ifd*54406237 Manoel Le', RESTAURANTES, DELIVERY],
    ['Ifd*Cs Ferreira Burgue', RESTAURANTES, DELIVERY],
    ['Ifd*Parada do Sushi ', RESTAURANTES, DELIVERY],
    ['Ifd*Poke You Restauran ', RESTAURANTES, DELIVERY],
    ['Ifd*Vr Restaurante', RESTAURANTES, DELIVERY],
    ['Ifd*Sajiki Mandaqui de', RESTAURANTES, DELIVERY],
    ['Padaria Sao Bento', ROLES, ALEATORIOS],
    ['Padaria Tagua', ROLES, ALEATORIOS],
    ['Sgm Delivery', RESTAURANTES, DELIVERY],
    ['Piacevole', RESTAURANTES, ALEATORIOS],
    ['Tauste', RESTAURANTES, ALEATORIOS],
    ['Panificadorasabor', RESTAURANTES, ALEATORIOS],
    ['Yu-Ya Sushi', RESTAURANTES, ALEATORIOS],
    ['O Filhotao', RESTAURANTES, ALEATORIOS],
    ['Ifd*Poke You Restauran', RESTAURANTES, DELIVERY],
    ['Sukiya', RESTAURANTES, ALEATORIOS],
    ['Ifd*Parada do Sushi', RESTAURANTES, DELIVERY],
    ['Mister Sheik Andorinha', RESTAURANTES, RESTANDORINHA],
    ['Sabor da Vovo', RESTAURANTES, RESTANDORINHA],
    ['Rest Frangoassado Cas', RESTAURANTES, ALEATORIOS],
    ['Posto Mariental', RESTAURANTES, ALEATORIOS],
    ['Frango Assado Posto Ca', RESTAURANTES, ALEATORIOS],
    ['Rest Frangoassado Caj', RESTAURANTES, ALEATORIOS],
    ['Subway Bc Barra Sul', RESTAURANTES, ALEATORIOS],
    ['Ifood *Ifood', RESTAURANTES, DELIVERY],
    ['Ifd*Sgm Delivery', RESTAURANTES, DELIVERY],
    ['Fhr Restaurante Ltda e', RESTAURANTES, ALEATORIOS],
    ['Boali - Santana Park', RESTAURANTES, ALEATORIOS],
    ['Ifd*e J Alimentos', RESTAURANTES, DELIVERY],
    ['Ifd*Tarbil Comercio de', RESTAURANTES, DELIVERY],
    ['Baked Potato C Norte', RESTAURANTES, ALEATORIOS],
    ['Panificadora Panicente', RESTAURANTES, ALEATORIOS],
    ['Bb Dog Itavuvu', RESTAURANTES, ALEATORIOS],
    ['Carnivore Steakhouse', RESTAURANTES, ALEATORIOS],
    ['Valmir Verus Restaura', RESTAURANTES, ALEATORIOS],
    ['Cozinhaasveia', RESTAURANTES, ALEATORIOS],
    ['Pizzaria Jefferson', RESTAURANTES, ALEATORIOS],
    ['Lanchonete', RESTAURANTES, ALEATORIOS],
    ['Chateau Fast Food', RESTAURANTES, ALEATORIOS],
    ['Lanchesdoremiltda', RESTAURANTES, ALEATORIOS],
    ['Nashi*Restaurante', RESTAURANTES, ALEATORIOS],
    ['Braz Leme Point', RESTAURANTES, ALEATORIOS],
    ['Panificadorae', RESTAURANTES, ALEATORIOS],
    ['Restaurante Querubim', RESTAURANTES, ALEATORIOS],
    ['de Vo Comercio de Ali', RESTAURANTES, ALEATORIOS],
    ['Restaurante Querubim', RESTAURANTES, ALEATORIOS],
    ['Suculentassabores', RESTAURANTES, ALEATORIOS],
    ['Suculentas', RESTAURANTES, ALEATORIOS],

    # ============ Assinaturas ===============
    ['Amazon Music', ASSINATURAS, AMAZONMUSIC],
    ['Amazonprimebr', ASSINATURAS, STREAMING],
    ['Apple.Com/Bill', ASSINATURAS, STREAMING],
    ['Google Wm Max Llc', ASSINATURAS, STREAMING],
    ['Google Youtube Music', ASSINATURAS, YTMUSIC],
    ['Netflix.Com', ASSINATURAS, STREAMING],
    ['Vindi *Capper', ASSINATURAS, TCL],
    ['Wellhub Gympass Br Gym', ASSINATURAS, GYMPASS],
    ['Google Disney Mobile', ASSINATURAS, STREAMING],
    ['Ifd*Ifood Club', ASSINATURAS, IFOODCLUB],
    ['Amazon Prime Aluguel', ASSINATURAS, AMAZONALUGUEL],
    ['Amazon Prime Canais', ASSINATURAS, AMAZONALUGUEL],
    ['Assinatura Max desconto Nubank', ASSINATURAS, STREAMING],
    ['Uber Uber *One Help.Ub', ASSINATURAS, UBERONE],

    ['Vindi *Investidor10 - Parcela 1/12', ASSINATURAS, IV10],
    ['Vindi *Investidor10 - Parcela 2/12', ASSINATURAS, IV10],
    ['Vindi *Investidor10 - Parcela 3/12', ASSINATURAS, IV10],
    ['Vindi *Investidor10 - Parcela 4/12', ASSINATURAS, IV10],
    ['Vindi *Investidor10 - Parcela 5/12', ASSINATURAS, IV10],
    ['Vindi *Investidor10 - Parcela 6/12', ASSINATURAS, IV10],
    ['Vindi *Investidor10 - Parcela 7/12', ASSINATURAS, IV10],
    ['Vindi *Investidor10 - Parcela 812', ASSINATURAS, IV10],
    ['Vindi *Investidor10 - Parcela 912', ASSINATURAS, IV10],
    ['Vindi *Investidor10 - Parcela 1012', ASSINATURAS, IV10],
    ['Vindi *Investidor10 - Parcela 1112', ASSINATURAS, IV10],
    ['Vindi *Investidor10 - Parcela 1212', ASSINATURAS, IV10],
    ['Alura - Parcela 4/12', ASSINATURAS, ALURA],
    ['Alura - Parcela 5/12', ASSINATURAS, ALURA],
    ['Alura - Parcela 6/12', ASSINATURAS, ALURA],
    ['Alura - Parcela 7/12', ASSINATURAS, ALURA],
    ['Alura - Parcela 8/12', ASSINATURAS, ALURA],
    ['Alura - Parcela 9/12', ASSINATURAS, ALURA],
    ['Alura - Parcela 10/12', ASSINATURAS, ALURA],
    ['Alura - Parcela 11/12', ASSINATURAS, ALURA],
    ['Alura - Parcela 12/12', ASSINATURAS, ALURA],
    ['Google Tinder', ASSINATURAS, DATING],
    ['Dl*Google Tinder', ASSINATURAS, DATING],
    ['Google Tinder Dating', ASSINATURAS, DATING],
    ['Google Bumble Dating', ASSINATURAS, DATING],
    ['Google Badoo Dating A', ASSINATURAS, DATING],
    ['Dl*Google Joyrid', ASSINATURAS, DATING],
    ['Google Joyride Gmbh', ASSINATURAS, DATING],
    ['Google Bumble', ASSINATURAS, DATING],
    ['Dl*Google Bumble', ASSINATURAS, DATING],
    ['Google Disney', ASSINATURAS, STREAMING],
    ['Netflix Entretenimento', ASSINATURAS, STREAMING],
    ['Dl*Google Wm Max', ASSINATURAS, STREAMING],
    ['Google Youtube', ASSINATURAS, STREAMING],
    ['Google Badoo', ASSINATURAS, DATING],
    ['Google Youtube', ASSINATURAS, STREAMING],
    ['Google Youtube', ASSINATURAS, STREAMING],
    ['Google Avast Software', ASSINATURAS, AVAST],


    # ============ Carro ===============
    ['Amazonas Leste - Parcela 1/10', CARRO, REVISAO],
    ['Amazonas Leste - Parcela 2/10', CARRO, REVISAO],
    ['Amazonas Leste - Parcela 3/10', CARRO, REVISAO],
    ['Amazonas Leste - Parcela 4/10', CARRO, REVISAO],
    ['Amazonas Leste - Parcela 5/10', CARRO, REVISAO],
    ['Amazonas Leste - Parcela 6/10', CARRO, REVISAO],
    ['Amazonas Leste - Parcela 7/10', CARRO, REVISAO],
    ['Amazonas Leste - Parcela 8/10', CARRO, REVISAO],
    ['Amazonas Leste - Parcela 9/10', CARRO, REVISAO],
    ['Amazonas Leste - Parcela 10/10', CARRO, REVISAO],
    ['Auto Posto Anhembi', CARRO, ABASTECIMENTO],
    ['sem Parar * Abastece', CARRO, ABASTECIMENTO],
    ['Shell Triunfo 24 Hs', CARRO, ABASTECIMENTO],
    ['Autopostoe', CARRO, ABASTECIMENTO],
    ['Autopostoroseira', CARRO, ABASTECIMENTO],
    ['Fixpark', CARRO, ESTACIONAMENTOS],
    ['Rede Papa', CARRO, ABASTECIMENTO],
    ['Gramadopostode', CARRO, ABASTECIMENTO],
    ['Posto Irmao da Estrada', CARRO, ABASTECIMENTO],
    ['Posto Papacidero', CARRO, ABASTECIMENTO],
    ['Posto Jardim 10', CARRO, ABASTECIMENTO],
    ['Auto Posto Joti', CARRO, ABASTECIMENTO],
    ['Jr Auto Posto', CARRO, ABASTECIMENTO],
    ['Posto Beira Rio I', CARRO, ABASTECIMENTO],
    ['G & G Auto Posto', CARRO, ABASTECIMENTO],
    ['Posto Lagoa', CARRO, ABASTECIMENTO],
    ['Autopostorvm', CARRO, ABASTECIMENTO],
    ['Pneustore Cpx - Parcela 1/6', CARRO, PNEU],
    ['Pneustore Cpx - Parcela 2/6', CARRO, PNEU],
    ['Pneustore Cpx - Parcela 3/6', CARRO, PNEU],
    ['Pneustore Cpx - Parcela 4/6', CARRO, PNEU],
    ['Pneustore Cpx - Parcela 5/6', CARRO, PNEU],
    ['Pneustore Cpx - Parcela 6/6', CARRO, PNEU],
    ['Welton Barros Silva', CARRO, LAVARAPIDO],
    ['Circuit Park Estaciona', CARRO, ESTACIONAMENTOS],
    ['Ess Estacionamentos', CARRO, ESTACIONAMENTOS],
    ['Estacionamento', CARRO, ESTACIONAMENTOS],
    ['Pg *Ton Estacionamen', CARRO, ESTACIONAMENTOS],
    ['Eagles Pinturas Esp', CARRO, FUNILARIA],
    ['Mercadocar - Parcela 1/2', CARRO, MERCADOCAR],
    ['Mercadocar - Parcela 2/2', CARRO, MERCADOCAR],
    ['Borracharia da Ponte P', CARRO, BORRACHARIA],
    ['Posto Castelinho Sor', CARRO, ABASTECIMENTO],
    ['Auto Posto 3 Meninas', CARRO, ABASTECIMENTO],
    ['Autopostonovoluz', CARRO, ABASTECIMENTO],
    ['Berlinf*Auto Posto Cae', CARRO, ABASTECIMENTO],
    ['Berlinf*Auto Posto Lei', CARRO, ABASTECIMENTO],
    ['Epar Estacionamentos', CARRO, ESTACIONAMENTOS],
    ['sem Parar', CARRO, SEMPARAR],


    # ============ Roles ===============
    ['Assai Atacadista Lj64', ROLES, BEBIDAS],
    ['Biergarten Usinamalte', ROLES, BARESREST],
    ['Letts Road', ROLES, BARESREST],
    ['Bambergexpress', ROLES, BARESREST],
    ['Casa Bar', ROLES, BARESREST],
    ['Chale das Flores', ROLES, BARESREST],
    ['Churras e Assados Pinh', ROLES, BARESREST],
    ['Dogdojoao', ROLES, BARESREST],
    ['Drogaria Santa Barbara', ROLES, BEBIDAS],
    ['Drogarias Nissei', ROLES, BEBIDAS],
    ['Emporio do Largo', ROLES, BEBIDAS],
    ['Espaco Gastronomico', ROLES, BEBIDAS],
    ['Esquadraodos', ROLES, PASSEIO],
    ['Depois Bar', ROLES, BARESREST],
    ['Flaine Jane Amp Cia', ROLES, BEBIDAS],
    ['Frogpay*Np Treinamento', ROLES, BEBIDAS],
    ['Zig*Balsa Bar', ROLES, BARESREST],
    ['Oxxo Martins', ROLES, BEBIDAS],
    ['Oxxo Alberto Savoy', ROLES, BEBIDAS],
    ['Oxxo Della', ROLES, BEBIDAS],
    ['Oxxo Barbar', ROLES, BEBIDAS],
    ['Vila do Samba', ROLES, BARESREST],
    ['Syscashtycket', ROLES, BARESREST],
    ['Matias Dumke', ROLES, BARESREST],
    ['Sheridans Restaurant', ROLES, BARESREST],
    ['Quintal da Maria', ROLES, BARESREST],
    ['Zig*Gaz Burning', ROLES, BARESREST],
    ['Letts Burger And Bar', ROLES, BARESREST],
    ['Postonovobatel', ROLES, BEBIDAS],
    ['Sr Caipira', ROLES, BARESREST],
    ['P R Carvalho Filho Bar', ROLES, BARESREST],
    ['Miles Wine Bar', ROLES, BARESREST],
    ['Pizzaria Francisca Ju', ROLES, BARESREST],
    ['Babo Domenico Costelar', ROLES, BARESREST],
    ['Alpen Snack Bar', ROLES, BARESREST],
    ['Bodega Beco Ltda', ROLES, BARESREST],
    ['Infoco', ROLES, BARESREST],
    ['Rest Sitio Cana do Rei', ROLES, BARESREST],
    ['Prainhadobecobare', ROLES, BARESREST],
    ['Rancho da Tirolesa', ROLES, BARESREST],
    ['Select Algodoal', ROLES, BARESREST],
    ['Piracicaba Drive', ROLES, BARESREST],
    ['Dolores Bar', ROLES, BARESREST],
    ['Doloreshouse', ROLES, BARESREST],
    ['Teresinhapacheco', ROLES, BARESREST],
    ['Pesqueiro Pekos', ROLES, BARESREST],
    ['Plbareeventosltda', ROLES, BARESREST],
    ['Condesso Emp Hotelei', ROLES, BARESREST],
    ['Buteco do Fortao', ROLES, BARESREST],
    ['Escort Auto Posto', ROLES, BEBIDAS],
    ['Quiosque do Miro', ROLES, BARESREST],
    ['Alecrim Ilhabela Resta', ROLES, BARESREST],
    ['Ohio Drink Store', ROLES, BARESREST],
    ['Mercadinho Costa Norte', ROLES, BEBIDAS],
    ['Manoel C.S Barbosa', ROLES, BARESREST],
    ['Fazendao', ROLES, BARESREST],
    ['Mp *Chur', ROLES, BARESREST],
    ['A F T Restaurante', ROLES, BARESREST],
    ['Airbnb * Hmwr5maf38', ROLES, HOSPEDAGEM],
    ['Barrel Surf Shop', ROLES, BARESREST],
    ['Aline Cerqueira Santo', ROLES, BEBIDAS],
    ['Giovanemamprinmaz', ROLES, BEBIDAS],
    ['Centroautomotivo', ROLES, BARESREST],
    ['Padaria e Lanchonete', ROLES, BARESREST],
    ['Rochinha Boicucanga', ROLES, BARESREST],
    ['Elizabethschmitz', ROLES, HOSPEDAGEM],
    ['Portaldopeixe', ROLES, BARESREST],
    ['Condesso Emp Hotelei', ROLES, BEBIDAS],
    ['Tasquinhadaserra', ROLES, BARESREST],
    ['Oxxo Bernacedo', ROLES, BEBIDAS],
    ['Allanmassulafortu', ROLES, BARESREST],
    ['Miles Bar', ROLES, BARESREST],
    ['Zig*Arcos', ROLES, BARESREST],
    ['Boomagen', ROLES, BARESREST],
    ['Prcarvalhofilho', ROLES, BARESREST],
    ['Oxxo Rospet', ROLES, BEBIDAS],
    ['Brassbrew Cervejaria L', ROLES, BARESREST],
    ['Atlantico', ROLES, BARESREST],
    ['Top Gas', ROLES, BARESREST],
    ['Campo Arte', ROLES, BARESREST],
    ['Seven Pratapolis', ROLES, BARESREST],
    ['Quintaldacanastra', ROLES, BARESREST],
    ['Lagoa Azul', ROLES, BARESREST],
    ['Elisangela Maria da Si', ROLES, BARESREST],
    ['Sao Joao Supermercados', ROLES, BEBIDAS],
    ['Posto Tigrao', ROLES, BEBIDAS],
    ['Choppdortmund', ROLES, BARESREST],
    ['Jmw Bebidas', ROLES, BEBIDAS],
    ['San Telmo', ROLES, BARESREST],
    ['Bar da Cachoeira', ROLES, BARESREST],
    ['Quiosque', ROLES, BARESREST],
    ['Hotel At Booking.Com', ROLES, HOSPEDAGEM],
    ['Airbnb * Hmded4pzep', ROLES, HOSPEDAGEM],
    ['Airbnb * Hmb2ssj998', ROLES, HOSPEDAGEM],
    ['Pousada e Campimg do C', ROLES, HOSPEDAGEM],
    ['Jackpub', ROLES, BARESREST],
    ['Assai Atacadista Lj263', ROLES, BEBIDAS],
    ['Bubble Tea Sorocaba', ROLES, BARESREST],
    ['Little Paul', ROLES, BARESREST],
    ['Jaques Cafe', ROLES, BARESREST],
    ['Florivento', ROLES, BARESREST],
    ['Ticketmais', ROLES, PASSEIO],
    ['Beto Carrero*Beto Carr', ROLES, PASSEIO],
    ['Atoanajoa', ROLES, BARESREST],
    ['Quiosquinhoba', ROLES, BARESREST],
    ['Quiosquedajoaca', ROLES, BARESREST],
    ['Brava Conveniencia', ROLES, BARESREST],
    ['Ponto 128 da Le', ROLES, BARESREST],
    ['Zig*Led Lounge Bar', ROLES, BARESREST],
    ['Supermercado Chico', ROLES, BEBIDAS],
    ['Vinicola Durigan', ROLES, BARESREST],
    ['41 Brooklyn', ROLES, BARESREST],
    ['Irmaos Madalosso', ROLES, BARESREST],
    ['Berlinf*Curitiba Turis', ROLES, BARESREST],
    ['Pelanda Conveniencia', ROLES, BEBIDAS],
    ['Marcoscesarafonso', ROLES, BEBIDAS],
    ['Soy Loco Por Ti Gastro', ROLES, BARESREST],
    ['Chori Getulio', ROLES, BARESREST],
    ['Blood Bar', ROLES, BARESREST],
    ['Airbnb * Hmchpm34xx', ROLES, HOSPEDAGEM],
    ['Airbnb * Hmscfhzc5j	', ROLES, HOSPEDAGEM],
    ['Airbnb * Hmkjajf8km', ROLES, HOSPEDAGEM],
    ['Purple Blues Pub', ROLES, BARESREST],
    ['Hard Rock Curitiba', ROLES, BARESREST],
    ['Guilherme Inacio Morei', ROLES, BEBIDAS],
    ['Curitiba Sunset', ROLES, BARESREST],
    ['Margaretebalparda', ROLES, BARESREST],
    ['Hortifruti e Supermer', ROLES, BEBIDAS],
    ['Zig*Amiiici', ROLES, BARESREST],
    ['Zig*Cremaclub', ROLES, BARESREST],
    ['Dalben', ROLES, BEBIDAS],
    ['Santa Helena Arte Bras', ROLES, BARESREST],
    ['Beer Praia', ROLES, BARESREST],
    ['Deck', ROLES, BARESREST],
    ['Serras Cafe', ROLES, BARESREST],
    ['Zig*Ledloungebar', ROLES, BARESREST],
    ['Lago dos Sonhos', ROLES, BARESREST],
    ['Estancia da Estacao', ROLES, BARESREST],
    ['Sitiosempressatur', ROLES, BARESREST],
    ['Santorini Bar', ROLES, BARESREST],
    ['Ssbar', ROLES, BEBIDAS],
    ['Bar Praia Grande', ROLES, BARESREST],
    ['Nashi*Restaurante', ROLES, BARESREST],
    ['Petisqueira', ROLES, BARESREST],
    ['Rescam Lanchonete', ROLES, BARESREST],
    ['Beto Carrero World', ROLES, BEBIDAS],
    ['Mercearia Sao Sebastia', ROLES, BEBIDAS],
    ['4everconsultoria', ROLES, BEBIDAS],
    ['Cicerofranciscode', ROLES, BEBIDAS],
    ['Ruggiero Ramos Comerc', ROLES, BEBIDAS],
    ['Posto Farol 48 da Cast', ROLES, BEBIDAS],
    ['Posto Fl', ROLES, BEBIDAS],
    ['Autopostohldlltda', ROLES, BEBIDAS],
    ['Supermercado Uniao', ROLES, BEBIDAS],
    ['Claudio Lazarin', ROLES, BEBIDAS],
    ['V L Gimenez Calheiros', ROLES, BARESREST],
    ['Rclservicos', ROLES, BARESREST],
    ['Luizapaivadelima', ROLES, BARESREST],
    ['Sou Funcional', ROLES, BARESREST],
    ['Sombrero', ROLES, BARESREST],
    ['Barra Beach', ROLES, BARESREST],
    ['Choripandashopia', ROLES, BARESREST],
    ['Mercado Juninho', ROLES, BEBIDAS],
    ['Pousadadaluana', ROLES, BEBIDAS],
    ['Luanamariade', ROLES, BEBIDAS],
    ['Autopostom6ltda', ROLES, BEBIDAS],
    ['Pointdoalemao', ROLES, BEBIDAS],
    ['Posto Z5', ROLES, BEBIDAS],
    ['Mp *Guicheweb', ROLES, PASSEIO],




    # ============ SAUDE ===============
    ['Farmaconde', SAUDE, FARMACIA],
    ['Raia194', SAUDE, FARMACIA],
    ['Mp *Growthsupplements', SAUDE, SUPLEMENTOS],
    ['Mp *Growthsupplements - Parcela 1/2', SAUDE, SUPLEMENTOS],
    ['Mp *Growthsupplements - Parcela 2/2', SAUDE, SUPLEMENTOS],
    ['Mp *Growthsupplements - Parcela 1/6', SAUDE, SUPLEMENTOS],
    ['Mp *Growthsupplements - Parcela 2/6', SAUDE, SUPLEMENTOS],
    ['Mp *Growthsupplements - Parcela 3/6', SAUDE, SUPLEMENTOS],
    ['Mp *Growthsupplements - Parcela 4/6', SAUDE, SUPLEMENTOS],
    ['Mp *Growthsupplements - Parcela 5/6', SAUDE, SUPLEMENTOS],
    ['Mp *Growthsupplements - Parcela 6/6', SAUDE, SUPLEMENTOS],
    ['Promofarma', SAUDE, FARMACIA],
    ['Pp *Growthsuppl', SAUDE, SUPLEMENTOS],
    ['Drogasil3486', SAUDE, FARMACIA],
    ['Raia340', SAUDE, FARMACIA],
    ['Drogaria Sao Paulo', SAUDE, FARMACIA],
    ['Oficial*Oficialfarma - Parcela 1/2', SAUDE, SUPLEMENTOS],
    ['Oficial*Oficialfarma - Parcela 2/2', SAUDE, SUPLEMENTOS],
    ['Oficial*Oficialfarma', SAUDE, SUPLEMENTOS],



    # ============ Barbeiro ===============
    ['51.510.029 Felipe Mat', BARBEIRO, LAUZANGELES],
    ['Barbearia Imperial', BARBEIRO, BARBEMP],
    ['Felipeferreirades', BARBEIRO, LAUZANGELES],
    ['Zp*Barbearia Pierre', BARBEIRO, ALEATORIOS],
    ['Elias Ladislau Cardoso	', BARBEIRO, ALEATORIOS],


    # ============ Mercado ===============
    ['Andorinha Hiper', MERCADO, SUPERMERCADO],
    ['Casa de Carnes Ultram', MERCADO, ACOUGUE],
    ['Spinola Supermercado', MERCADO, SUPERMERCADO],
    ['Mini Extra', MERCADO, SUPERMERCADO],
    ['Swift Horto', MERCADO, SUPERMERCADO],
    ['Pao de Acucar-2380', MERCADO, SUPERMERCADO],
    ['Inovapina', MERCADO, MERCADINHOCOND],
    ['Carnes Ultramarino', MERCADO, SUPERMERCADO],
    ['Trimais Supermercados', MERCADO, SUPERMERCADO],
    ['Stalo Supermercados Lo', MERCADO, SUPERMERCADO],
    ['Supermercados Koch', MERCADO, SUPERMERCADO],



    # ============ Esportes ===============
    ['Agua de Coco Horto', ESPORTES, HIDR],
    ['Vera Doces', ESPORTES, HIDR],
    ['Restaurante e Lanchone', ESPORTES, HIDR],
    ['Point Santana', ESPORTES, HIDR],
    ['Agua de Coco Verde do', ESPORTES, HIDR],
    ['Decathlon - Parcela 1/12', ESPORTES, ACESSORIOSCICLISMO],
    ['Decathlon - Parcela 2/12', ESPORTES, ACESSORIOSCICLISMO],
    ['Decathlon - Parcela 3/12', ESPORTES, ACESSORIOSCICLISMO],
    ['Decathlon - Parcela 4/12', ESPORTES, ACESSORIOSCICLISMO],
    ['Decathlon - Parcela 5/12', ESPORTES, ACESSORIOSCICLISMO],
    ['Decathlon - Parcela 6/12', ESPORTES, ACESSORIOSCICLISMO],
    ['Decathlon - Parcela 7/12', ESPORTES, ACESSORIOSCICLISMO],
    ['Decathlon - Parcela 8/12', ESPORTES, ACESSORIOSCICLISMO],
    ['Decathlon - Parcela 9/12', ESPORTES, ACESSORIOSCICLISMO],
    ['Decathlon - Parcela 10/12', ESPORTES, ACESSORIOSCICLISMO],
    ['Decathlon - Parcela 11/12', ESPORTES, ACESSORIOSCICLISMO],
    ['Decathlon - Parcela 12/12', ESPORTES, ACESSORIOSCICLISMO],
    ['Mp *Aliexpress - Parcela 1/2', ESPORTES, ACESSORIOSCICLISMO],
    ['Mp *Aliexpress - Parcela 2/2', ESPORTES, ACESSORIOSCICLISMO],
    ['Pedal Place - Parcela 1/12', ESPORTES, COMPRABIKE],
    ['Pedal Place - Parcela 2/12', ESPORTES, COMPRABIKE],
    ['Pedal Place - Parcela 3/12', ESPORTES, COMPRABIKE],
    ['Pedal Place - Parcela 4/12', ESPORTES, COMPRABIKE],
    ['Pedal Place - Parcela 5/12', ESPORTES, COMPRABIKE],
    ['Pedal Place - Parcela 6/12', ESPORTES, COMPRABIKE],
    ['Pedal Place - Parcela 7/12', ESPORTES, COMPRABIKE],
    ['Pedal Place - Parcela 8/12', ESPORTES, COMPRABIKE],
    ['Pedal Place - Parcela 9/12', ESPORTES, COMPRABIKE],
    ['Pedal Place - Parcela 10/12', ESPORTES, COMPRABIKE],
    ['Pedal Place - Parcela 11/12', ESPORTES, COMPRABIKE],
    ['Pedal Place - Parcela 12/12', ESPORTES, COMPRABIKE],
    ['Mercadopago *Freeforc - Parcela 1/5', ESPORTES, ACESSORIOSCICLISMO],
    ['Mercadopago *Freeforc - Parcela 2/5', ESPORTES, ACESSORIOSCICLISMO],
    ['Mercadopago *Freeforc - Parcela 3/5', ESPORTES, ACESSORIOSCICLISMO],
    ['Mercadopago *Freeforc - Parcela 4/5', ESPORTES, ACESSORIOSCICLISMO],
    ['Mercadopago *Freeforc - Parcela 5/5', ESPORTES, ACESSORIOSCICLISMO],
    ['Marcolas Bike Shop Bic', ESPORTES, ACESSORIOSCICLISMO],
    ['Marcolas Bike Shop Bic - Parcela 1/3', ESPORTES, ACESSORIOSCICLISMO],
    ['Marcolas Bike Shop Bic - Parcela 2/3', ESPORTES, ACESSORIOSCICLISMO],
    ['Marcolas Bike Shop Bic - Parcela 3/3', ESPORTES, ACESSORIOSCICLISMO],



    # ============ Compras ===============
    ['Brs*Sheincom', COMPRAS, ROUPAS],
    ['Casas Bahia - Parcela 1/12', COMPRAS, PARCELATV],
    ['Casas Bahia - Parcela 2/12', COMPRAS, PARCELATV],
    ['Casas Bahia - Parcela 3/12', COMPRAS, PARCELATV],
    ['Casas Bahia - Parcela 4/12', COMPRAS, PARCELATV],
    ['Casas Bahia - Parcela 5/12', COMPRAS, PARCELATV],
    ['Casas Bahia - Parcela 6/12', COMPRAS, PARCELATV],
    ['Casas Bahia - Parcela 7/12', COMPRAS, PARCELATV],
    ['Casas Bahia - Parcela 8/12', COMPRAS, PARCELATV],
    ['Casas Bahia - Parcela 9/12', COMPRAS, PARCELATV],
    ['Casas Bahia - Parcela 10/12', COMPRAS, PARCELATV],
    ['Casas Bahia - Parcela 11/12', COMPRAS, PARCELATV],
    ['Casas Bahia - Parcela 12/12', COMPRAS, PARCELATV],
    ['Cea Sor 175 Ecpc - Parcela 2/2', COMPRAS, ROUPAS],
    ['Cea Sor 175 Ecpc - Parcela 1/2', COMPRAS, ROUPAS],
    ['Hs Esplanada Shopping - Parcela 1/2', COMPRAS, ROUPAS],
    ['Hs Esplanada Shopping - Parcela 2/2', COMPRAS, ROUPAS],
    ['Havan Bal Camboriu Cen - Parcela 1/2', COMPRAS, ROUPAS],
    ['Havan Bal Camboriu Cen - Parcela 2/2', COMPRAS, ROUPAS],
    ['Pp *Salvino Sto - Parcela 1/10', COMPRAS, ROUPAS],
    ['Pp *Salvino Sto - Parcela 2/10', COMPRAS, ROUPAS],
    ['Pp *Salvino Sto - Parcela 3/10', COMPRAS, ROUPAS],
    ['Pp *Salvino Sto - Parcela 4/10', COMPRAS, ROUPAS],
    ['Pp *Salvino Sto - Parcela 5/10', COMPRAS, ROUPAS],
    ['Pp *Salvino Sto - Parcela 6/10', COMPRAS, ROUPAS],
    ['Pp *Salvino Sto - Parcela 7/10', COMPRAS, ROUPAS],
    ['Pp *Salvino Sto - Parcela 8/10', COMPRAS, ROUPAS],
    ['Pp *Salvino Sto - Parcela 9/10', COMPRAS, ROUPAS],
    ['Pp *Salvino Sto - Parcela 10/10', COMPRAS, ROUPAS],
    ['Acasa Objeto e Decorac', COMPRAS, ROUPAS],
    ['Hub Fin*Magazineluiza - Parcela 10/10', COMPRAS, OUTROS],
    ['Mercadolivre*Berveenx - Parcela 1/2', COMPRAS, OUTROS],
    ['Mercadolivre*Berveenx - Parcela 2/2', COMPRAS, OUTROS],
    ['Mp *Softroniccomercia - Parcela 1/2', COMPRAS, OUTROS],
    ['Mp *Softroniccomercia - Parcela 2/2', COMPRAS, OUTROS],
    ['Mercadolivre*Ebazarco - Parcela 1/10', COMPRAS, PARCELACELULAR],
    ['Mercadolivre*Ebazarco - Parcela 2/10', COMPRAS, PARCELACELULAR],
    ['Mercadolivre*Ebazarco - Parcela 3/10', COMPRAS, PARCELACELULAR],
    ['Mercadolivre*Ebazarco - Parcela 4/10', COMPRAS, PARCELACELULAR],
    ['Mercadolivre*Ebazarco - Parcela 5/10', COMPRAS, PARCELACELULAR],
    ['Mercadolivre*Ebazarco - Parcela 6/10', COMPRAS, PARCELACELULAR],
    ['Mercadolivre*Ebazarco - Parcela 7/10', COMPRAS, PARCELACELULAR],
    ['Mercadolivre*Ebazarco - Parcela 8/10', COMPRAS, PARCELACELULAR],
    ['Mercadolivre*Ebazarco - Parcela 9/10', COMPRAS, PARCELACELULAR],
    ['Mercadolivre*Ebazarco - Parcela 10/10', COMPRAS, PARCELACELULAR],
    ['Mercadolivre*Ravennaf - Parcela 1/10', COMPRAS, OUTROS],
    ['Mercadolivre*Ravennaf - Parcela 2/10', COMPRAS, OUTROS],
    ['Mercadolivre*Ravennaf - Parcela 3/10', COMPRAS, OUTROS],
    ['Mercadolivre*Ravennaf - Parcela 4/10', COMPRAS, OUTROS],
    ['Mercadolivre*Ravennaf - Parcela 5/10', COMPRAS, OUTROS],
    ['Mercadolivre*Ravennaf - Parcela 6/10', COMPRAS, OUTROS],
    ['Mercadolivre*Ravennaf - Parcela 7/10', COMPRAS, OUTROS],
    ['Mercadolivre*Ravennaf - Parcela 8/10', COMPRAS, OUTROS],
    ['Mercadolivre*Ravennaf - Parcela 9/10', COMPRAS, OUTROS],
    ['Mercadolivre*Ravennaf - Parcela 10/10', COMPRAS, OUTROS],
    ['Mercadolivre*Tudustor - Parcela 1/2', COMPRAS, OUTROS],
    ['Mercadolivre*Tudustor - Parcela 2/2', COMPRAS, OUTROS],
    ['Mercadolivre*Azbuy', COMPRAS, OUTROS],
    ['Mercadolivre*Nrutilid - Parcela 1/7', COMPRAS, OUTROS],
    ['Mercadolivre*Nrutilid - Parcela 2/7', COMPRAS, OUTROS],
    ['Mercadolivre*Nrutilid - Parcela 3/7', COMPRAS, OUTROS],
    ['Mercadolivre*Nrutilid - Parcela 4/7', COMPRAS, OUTROS],
    ['Mercadolivre*Nrutilid - Parcela 5/7', COMPRAS, OUTROS],
    ['Mercadolivre*Nrutilid - Parcela 6/7', COMPRAS, OUTROS],
    ['Mercadolivre*Nrutilid - Parcela 7/7', COMPRAS, OUTROS],
    ['Mercadopago *Lasvixel - Parcela 1/2', COMPRAS, OUTROS],
    ['Mercadopago *Lasvixel - Parcela 2/2', COMPRAS, OUTROS],
    ['Lojas Renner Fl - Parcela 1/3', COMPRAS, ROUPAS],
    ['Lojas Renner Fl - Parcela 2/3', COMPRAS, ROUPAS],
    ['Lojas Renner Fl - Parcela 3/3', COMPRAS, ROUPAS],
    ['Lojas Renner Fl - Parcela 1/2', COMPRAS, ROUPAS],
    ['Lojas Renner Fl - Parcela 2/2', COMPRAS, ROUPAS],
    [' Lojas G', COMPRAS, OUTROS],
    ['Sn Bijoterias', COMPRAS, PRESENTES],
    ['Decathlon - Parcela 1/3', COMPRAS, OUTROS],
    ['Decathlon - Parcela 2/3', COMPRAS, OUTROS],
    ['Decathlon - Parcela 3/3', COMPRAS, OUTROS],
    ['Riachuelo 167 Mg Bh Mi - Parcela 1/2', COMPRAS, ROUPAS],
    ['Riachuelo 167 Mg Bh Mi - Parcela 2/2', COMPRAS, ROUPAS],
    ['Lojas G', COMPRAS, OUTROS],
    ['Mercadolivre*Izuecomm', COMPRAS, OUTROS],
    ['Mercadopago *Idealcit - Parcela 1/12', COMPRAS, OUTROS],
    ['Mercadopago *Idealcit - Parcela 2/12', COMPRAS, OUTROS],
    ['Mercadopago *Idealcit - Parcela 3/12', COMPRAS, OUTROS],
    ['Mercadopago *Idealcit - Parcela 4/12', COMPRAS, OUTROS],
    ['Mercadopago *Idealcit - Parcela 5/12', COMPRAS, OUTROS],
    ['Mercadopago *Idealcit - Parcela 6/12', COMPRAS, OUTROS],
    ['Mercadopago *Idealcit - Parcela 8/12', COMPRAS, OUTROS],
    ['Mercadopago *Idealcit - Parcela 9/12', COMPRAS, OUTROS],
    ['Mercadopago *Idealcit - Parcela 10/12', COMPRAS, OUTROS],
    ['Mercadopago *Idealcit - Parcela 11/12', COMPRAS, OUTROS],
    ['Mercadopago *Idealcit - Parcela 12/12', COMPRAS, OUTROS],
    ['Pg *Betterman Comercio - Parcela 1/3', COMPRAS, ROUPAS],
    ['Pg *Betterman Comercio - Parcela 2/3', COMPRAS, ROUPAS],
    ['Pg *Betterman Comercio - Parcela 3/3', COMPRAS, ROUPAS],
    ['Ln Tennis Station Cent - Parcela 1/6', COMPRAS, ROUPAS],
    ['Ln Tennis Station Cent - Parcela 2/6', COMPRAS, ROUPAS],
    ['Ln Tennis Station Cent - Parcela 3/6', COMPRAS, ROUPAS],
    ['Ln Tennis Station Cent - Parcela 4/6', COMPRAS, ROUPAS],
    ['Ln Tennis Station Cent - Parcela 5/6', COMPRAS, ROUPAS],
    ['Ln Tennis Station Cent - Parcela 6/6', COMPRAS, ROUPAS],
    ['Mercadolivre*Amferram', COMPRAS, OUTROS],
    ['Padoca Ultramarino', COMPRAS, OUTROS],
    ['Mercadopago *Xpink', COMPRAS, OUTROS],
    ['Insider Come*Insiderst - Parcela 1/3', COMPRAS, ROUPAS],
    ['Insider Come*Insiderst - Parcela 2/3', COMPRAS, ROUPAS],
    ['Insider Come*Insiderst - Parcela 3/3', COMPRAS, ROUPAS],
    ['Hub Fin*Magazineluiza - Parcela 1/10', COMPRAS, OUTROS],
    ['Hub Fin*Magazineluiza - Parcela 2/10', COMPRAS, OUTROS],
    ['Hub Fin*Magazineluiza - Parcela 3/10', COMPRAS, OUTROS],
    ['Hub Fin*Magazineluiza - Parcela 4/10', COMPRAS, OUTROS],
    ['Hub Fin*Magazineluiza - Parcela 5/10', COMPRAS, OUTROS],
    ['Hub Fin*Magazineluiza - Parcela 6/10', COMPRAS, OUTROS],
    ['Hub Fin*Magazineluiza - Parcela 7/10', COMPRAS, OUTROS],
    ['Hub Fin*Magazineluiza - Parcela 8/10', COMPRAS, OUTROS],
    ['Hub Fin*Magazineluiza - Parcela 9/10', COMPRAS, OUTROS],
    ['Hub Fin*Magazineluiza - Parcela 10/10', COMPRAS, OUTROS],
    ['Mercadolivre*Tapetesm - Parcela 1/7', COMPRAS, OUTROS],
    ['Mercadolivre*Tapetesm - Parcela 2/7', COMPRAS, OUTROS],
    ['Mercadolivre*Tapetesm - Parcela 3/7', COMPRAS, OUTROS],
    ['Mercadolivre*Tapetesm - Parcela 4/7', COMPRAS, OUTROS],
    ['Mercadolivre*Tapetesm - Parcela 5/7', COMPRAS, OUTROS],
    ['Mercadolivre*Tapetesm - Parcela 6/7', COMPRAS, OUTROS],
    ['Mercadolivre*Tapetesm - Parcela 7/7', COMPRAS, OUTROS],
    ['Centauro Ce75 - Parcela 1/5', COMPRAS, ROUPAS],
    ['Centauro Ce75 - Parcela 2/5', COMPRAS, ROUPAS],
    ['Centauro Ce75 - Parcela 3/5', COMPRAS, ROUPAS],
    ['Centauro Ce75 - Parcela 4/5', COMPRAS, ROUPAS],
    ['Centauro Ce75 - Parcela 5/5', COMPRAS, ROUPAS],
    ['Chilli Beans - Parcela 1/8', COMPRAS, PRESENTES],
    ['Chilli Beans - Parcela 2/8', COMPRAS, PRESENTES],
    ['Chilli Beans - Parcela 3/8', COMPRAS, PRESENTES],
    ['Chilli Beans - Parcela 4/8', COMPRAS, PRESENTES],
    ['Chilli Beans - Parcela 5/8', COMPRAS, PRESENTES],
    ['Chilli Beans - Parcela 6/8', COMPRAS, PRESENTES],
    ['Chilli Beans - Parcela 7/8', COMPRAS, PRESENTES],
    ['Chilli Beans - Parcela 8/8', COMPRAS, PRESENTES],
    ['Chelle Beans Senter No - Parcela 1/5', COMPRAS, OUTROS],
    ['Chelle Beans Senter No - Parcela 2/5', COMPRAS, OUTROS],
    ['Chelle Beans Senter No - Parcela 3/5', COMPRAS, OUTROS],
    ['Chelle Beans Senter No - Parcela 4/5', COMPRAS, OUTROS],
    ['Chelle Beans Senter No - Parcela 5/5', COMPRAS, OUTROS],
    ['Luana', COMPRAS, OUTROS],
    ['Mercadolivre*Mercadol', COMPRAS, OUTROS],
    ['Loteriasonlinehpeb', COMPRAS, OUTROS],
    ['Leroy Merlin', COMPRAS, OUTROS],
    ['Mercadolivre*Megabyte - Parcela 1/2', COMPRAS, OUTROS],
    ['Mercadolivre*Megabyte - Parcela 2/2', COMPRAS, OUTROS],
    ['Guaira Loterias', COMPRAS, OUTROS],
    ['Norteplac Madeiras e F', COMPRAS, OUTROS],
    ['Helpa Lauzane Construc', COMPRAS, OUTROS],
    ['Mercadolivre*Firstore', COMPRAS, OUTROS],
    ['Teles Calcados', COMPRAS, PRESENTES],


    # ============ Transporte ===============

    ['Uber* Trip', TRANSPORTE, UBER],
    ['Uber Uber *Trip Help.U', TRANSPORTE, UBER],


]

# Nomes das colunas
columns = ['title', 'category', 'subcategory']

df_mapping = pd.DataFrame(MAP, columns=columns)


df_merged = pd.merge(df_unified, df_mapping, on='title', how='left')
df_merged = df_merged.drop_duplicates()

# ---------------
size = 5

# ============================================
#               Plotagem
# ============================================
st.set_page_config(page_title="Meu Dashboard", layout="wide")

col1, col2 = st.columns(2)

# ----------------------------------------------
#   Gráfico de Barras por mês
# ----------------------------------------------
with col1:
    df_grouped_g1 = df_merged.groupby(['year_month'])['amount'].sum()

    # Formata o índice para 'Mai/2025'
    df_grouped_g1.index = pd.to_datetime(
        df_grouped_g1.index.astype(str), format='%Y%m'
    ).strftime('%b/%Y')

    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = df_grouped_g1.plot(kind='bar', ax=ax, color='royalblue')

    ax.set_title('Gastos por Mês', fontsize=16)
    ax.set_ylabel('Gasto (R$)', fontsize=12)
    ax.set_xlabel('Ano/Mês', fontsize=12)
    ax.tick_params(axis='x', labelrotation=45)
    ax.tick_params(axis='y')

    # Adiciona os valores em cima das barras com separador decimal vírgula
    for i, valor in enumerate(df_grouped_g1.values):
        valor_formatado = f"R$ {valor:,.2f}".replace(
            ",", "X").replace(".", ",").replace("X", ".")
        ax.text(i, valor + max(df_grouped_g1) * 0.01,
                valor_formatado,
                ha='center', va='bottom', fontsize=10)

    # Formatar eixo Y com separador decimal brasileiro
    y_ticks = ax.get_yticks()
    y_labels = [f'{y:,.2f}'.replace(",", "X").replace(
        ".", ",").replace("X", ".") for y in y_ticks]
    ax.set_yticklabels(y_labels)

    plt.tight_layout()

    st.pyplot(fig)

# ----------------------------------------------
#   Gráfico de Barras por categoria por mês
# ----------------------------------------------

with col2:
    df_grouped_g2 = df_merged.groupby(['category', 'year_month'])[
        'amount'].sum().unstack(fill_value=0)

    # Converter colunas (ano/mês) para formato legível
    df_grouped_g2.columns = pd.to_datetime(
        df_grouped_g2.columns.astype(str), format='%Y%m').strftime('%b/%Y')

    # --- Plotar com matplotlib ---
    fig, ax = plt.subplots(figsize=(10, 6))
    df_grouped_g2.plot(kind='bar', ax=ax)

    ax.set_title('Gastos por Categoria e Mês', fontsize=16)
    ax.set_ylabel('Gasto (R$)', fontsize=12)
    ax.set_xlabel('Categoria', fontsize=12)
    ax.legend(title='Ano/Mês', bbox_to_anchor=(1.05, 1), loc='upper left')

    # Linhas horizontais (grades)
    ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.6)

    # Rotacionar rótulos do eixo X
    plt.xticks(rotation=45)

    # Formatar eixo Y com separador decimal brasileiro
    y_ticks = ax.get_yticks()
    y_labels = [f'{y:,.2f}'.replace('.', 'X').replace(
        ',', '.').replace('X', ',') for y in y_ticks]
    ax.set_yticklabels(y_labels)

    plt.tight_layout()

    # --- Mostrar no Streamlit ---
    st.pyplot(fig)


# ----------------------------------------------
#               Total Linhas
# ----------------------------------------------


with col1:
    df_merged['year_month'] = df_merged['year_month'].astype(str)
    df_merged = df_merged.dropna(subset=['category'])

    available_categories = sorted(df_merged['category'].unique())

    selected_categories = st.multiselect(
        "Escolha as categorias que deseja visualizar:",
        options=available_categories,
        default=available_categories,
        key="category_selector"
    )

    filtered_df = df_merged[df_merged['category'].isin(selected_categories)]

    grouped = filtered_df.groupby(['year_month', 'category'])[
        'amount'].sum().reset_index()

    plt.figure(figsize=(12, 6))

    for cat in selected_categories:
        data = grouped[grouped['category'] == cat]
        plt.plot(data['year_month'], data['amount'], label=cat, marker='o')

    plt.title("Total de Gastos por Categoria")
    plt.xlabel("Ano/Mês")
    plt.ylabel("Soma do Amount (R$)")
    plt.legend(title="Categoria")
    plt.grid(True)
    plt.xticks(rotation=45)

    # Formatar o eixo Y em Reais
    ax = plt.gca()
    ax.yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, _: f'R$ {x:,.2f}'.replace(
            ',', 'X').replace('.', ',').replace('X', '.'))
    )

    st.pyplot(plt)

# ----------------------------------------------
#               Stacked
# ----------------------------------------------

with col2:
    # --- Preparação dos dados ---
    df_merged['category'] = df_merged['category'].fillna('Sem Categoria')
    df_merged['subcategory'] = df_merged['subcategory'].fillna(
        'Sem Subcategoria')
    df_merged['year_month_dt'] = pd.to_datetime(
        df_merged['year_month'].astype(str), format='%Y%m')

    # --- Filtro de categoria ---
    categorias_disponiveis = df_merged['category'].unique().tolist()
    categoria_selecionada = st.selectbox(
        "Escolha uma categoria:", categorias_disponiveis)

    # --- Filtrar dados da categoria escolhida ---
    df_filtrado = df_merged[df_merged['category'] == categoria_selecionada]

    # --- Agrupar por mês e subcategoria ---
    df_agrupado = df_filtrado.groupby(['year_month_dt', 'subcategory'])[
        'amount'].sum().unstack(fill_value=0)

    # --- Plot ---
    fig, ax = plt.subplots(figsize=(12, 6))
    bars = df_agrupado.plot(kind='bar', stacked=True, ax=ax)

    # Título e eixos
    ax.set_title(
        f'Gastos por Subcategoria - {categoria_selecionada}', fontsize=16)
    ax.set_xlabel('Mês', fontsize=12)
    ax.set_ylabel('Total Gasto (R$)', fontsize=12)
    ax.set_xticks(range(len(df_agrupado.index)))
    ax.set_xticklabels(df_agrupado.index.strftime('%b/%Y'), rotation=45)
    ax.legend(title='Subcategoria', bbox_to_anchor=(1.05, 1), loc='upper left')

    # Linhas horizontais pontilhadas
    ax.grid(True, axis='y', linestyle='--', linewidth=0.7, alpha=0.6)

    # Formatar eixo Y com separador decimal brasileiro
    y_ticks = ax.get_yticks()
    y_labels = [f'{y:,.2f}'.replace(',', 'X').replace(
        '.', ',').replace('X', '.') for y in y_ticks]
    ax.set_yticklabels(y_labels)

    # --- Adicionar rótulos com valor total no topo de cada barra empilhada ---
    for idx, (i, row) in enumerate(df_agrupado.iterrows()):
        total = row.sum()
        valor_formatado = f'R$ {total:,.2f}'.replace(
            ',', 'X').replace('.', ',').replace('X', '.')
        ax.text(idx, total + max(df_agrupado.sum(axis=1)) * 0.01,  # pequeno deslocamento vertical
                valor_formatado,
                ha='center', va='bottom', fontsize=9, fontweight='bold')

    plt.tight_layout()
    st.pyplot(fig)


# ----------------------------------------------
#               Cumsum
# ----------------------------------------------

with col1:

    df_merged['date'] = pd.to_datetime(df_merged['date'])
    df_merged = df_merged.sort_values('date')

    # --- Filtros opcionais ---
    categorias_disponiveis = df_merged['category'].unique().tolist()
    categorias_selecionadas = st.multiselect(
        "Filtrar por categorias (opcional):",
        options=categorias_disponiveis,
        default=categorias_disponiveis
    )

    # --- Aplicar filtro se necessário ---
    df_filtrado = df_merged[df_merged['category'].isin(
        categorias_selecionadas)]

    # --- Calcular o acumulado ---
    df_filtrado['cumsum'] = df_filtrado['amount'].cumsum()

    # --- Criar gráfico ---
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(df_filtrado['date'], df_filtrado['cumsum'],
            marker='o', color='mediumseagreen')

    # --- Personalizar gráfico ---
    ax.set_title('Gasto Acumulado ao Longo do Tempo', fontsize=16)
    ax.set_xlabel('Data', fontsize=12)
    ax.set_ylabel('Gasto Acumulado (R$)', fontsize=12)
    ax.tick_params(axis='x', rotation=45)

    # --- Linhas horizontais pontilhadas ---
    ax.grid(True, axis='y', linestyle='--', linewidth=0.7, alpha=0.6)

    # --- Separador decimal no eixo Y ---
    y_ticks = ax.get_yticks()
    y_labels = [f'{y:,.2f}'.replace(',', 'X').replace(
        '.', ',').replace('X', '.') for y in y_ticks]
    ax.set_yticklabels(y_labels)

    plt.tight_layout()

    # --- Exibir no Streamlit ---
    st.pyplot(fig)


# ----------------------------------------------
#               TOP
# ----------------------------------------------

with col2:
    # --- Filtro: Top N gastos ---
    top_n = st.slider("Selecionar quantos maiores gastos exibir:",
                      min_value=1, max_value=20, value=5)

    # --- Ordenar e pegar top N ---
    df_top = df_merged.sort_values(by='amount', ascending=False).head(top_n)

    # --- Exibir gráfico de barras dos top gastos ---
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(df_top['title'], df_top['amount'], color='tomato')
    ax.invert_yaxis()
    ax.set_title(f'Top {top_n} Gastos', fontsize=16)
    ax.set_xlabel('Valor (R$)')
    ax.set_ylabel('Descrição')
    for i, v in enumerate(df_top['amount']):
        ax.text(v + 5, i, f'R$ {v:.2f}', va='center')

    plt.tight_layout()
    st.pyplot(fig)

# ----------------------------------------------
#               Contagem
# ----------------------------------------------

with col1:

    # --- Contar transações por year_month ---
    df_count = df_merged.groupby(
        'year_month').size().reset_index(name='num_transacoes')

    # --- Formatar year_month para "MMM/YYYY" para exibir no eixo X ---
    df_count['year_month_fmt'] = pd.to_datetime(
        df_count['year_month'].astype(str), format='%Y%m').dt.strftime('%b/%Y')

    # --- Plotar gráfico ---
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(df_count['year_month_fmt'],
           df_count['num_transacoes'], color='slateblue')

    # --- Personalizar ---
    ax.set_title('Número de Transações por Mês', fontsize=16)
    ax.set_xlabel('Mês', fontsize=12)
    ax.set_ylabel('Quantidade de Transações', fontsize=12)
    ax.grid(axis='y')
    ax.set_ylim(0, df_count['num_transacoes'].max() + 2)

    # Rótulos nas barras
    for i, v in enumerate(df_count['num_transacoes']):
        ax.text(i, v + 0.2, str(v), ha='center', va='bottom', fontsize=10)

    plt.tight_layout()

    # --- Mostrar no Streamlit ---
    st.pyplot(fig)

# ----------------------------------------------
#               Perfis Médios
# ----------------------------------------------

with col2:

    df_merged['year_month'] = df_merged['year_month'].astype(str)

    # Remover categorias nulas
    df_merged = df_merged.dropna(subset=['category'])

    # Lista única de categorias disponíveis
    available_categories = sorted(df_merged['category'].unique())

    # Caixa de seleção de categorias
    selected_categories = st.multiselect(
        "Escolha as categorias que deseja visualizar:",
        options=available_categories,
        default=available_categories  # já seleciona todas por padrão
    )

    # Filtrar o dataframe com as categorias escolhidas
    filtered_df = df_merged[df_merged['category'].isin(selected_categories)]

    # Agrupar e calcular média e erro padrão
    grouped = filtered_df.groupby(['year_month', 'category'])[
        'amount'].agg(['mean', 'sem']).reset_index()

    # Criar gráfico
    plt.figure(figsize=(12, 6))

    # Plotar cada categoria
    for cat in selected_categories:
        data = grouped[grouped['category'] == cat]
        plt.errorbar(data['year_month'], data['mean'],
                     yerr=data['sem'], label=cat, marker='o', capsize=5)

    # Estética do gráfico
    plt.title("Perfil Médio de Gastos por Categoria")
    plt.xlabel("Ano/Mês")
    plt.ylabel("Média do Amount (com erro padrão)")
    plt.legend(title="Categoria")
    plt.grid(True)
    plt.xticks(rotation=45)

    # Exibir no Streamlit
    st.pyplot(plt)


# ----------------------------------------------
#               Pie
# ----------------------------------------------

with col1:
    fig, ax = plt.subplots(figsize=(8, 8))  # proporção mais adequada para pie

    option = st.selectbox('Ano/Mês:', sorted(df_merged['year_month'].unique()))

    df_pie = df_merged[df_merged['year_month'] == option]

    pie_data = df_pie.groupby('category')[
        'amount'].sum().sort_values(ascending=False)

    # Explode opcional para destacar a maior fatia
    explode = [0.05 if i == 0 else 0 for i in range(len(pie_data))]

    # Função para formatar o autopct com vírgula
    def format_pct(pct):
        return f'{pct:.1f}'.replace('.', ',') + '%'

    wedges, texts, autotexts = ax.pie(
        pie_data,
        labels=None,  # não mostrar diretamente para evitar sobreposição
        autopct=format_pct,
        startangle=90,
        explode=explode,
        labeldistance=1.1,
        pctdistance=0.7,
        textprops={'fontsize': 10}
    )

    ax.axis('equal')  # deixa a pizza redonda
    ax.set_title(
        f'Distribuição de Gastos por Categoria - {option}', fontsize=14)

    # Adiciona legenda ao lado
    ax.legend(wedges, pie_data.index, title="Categorias",
              bbox_to_anchor=(1, 1), loc="upper left")

    st.pyplot(fig)

# ==============
df_merged["date"] = pd.to_datetime(df_merged["date"])
df_merged["weekday"] = df_merged["date"].dt.day_name(locale="pt_BR")

# Título
st.title("📊 Gastos por Data com Colunas Empilhadas por Categoria")

# Filtros
col1, col2, col3 = st.columns(3)

with col1:
    selected_category = st.multiselect(
        "Categoria",
        options=sorted(df_merged["category"].dropna().unique()),
        default=sorted(df_merged["category"].dropna().unique())
    )

with col2:
    selected_subcategory = st.multiselect(
        "Subcategoria",
        options=sorted(df_merged["subcategory"].dropna().unique()),
        default=sorted(df_merged["subcategory"].dropna().unique())
    )

with col3:
    selected_weekdays = st.multiselect(
        "Dias da Semana",
        options=df_merged["weekday"].unique(),
        default=df_merged["weekday"].unique()
    )

# Aplica os filtros
filtered_df_merged = df_merged[
    df_merged["category"].isin(selected_category) &
    df_merged["subcategory"].isin(selected_subcategory) &
    df_merged["weekday"].isin(selected_weekdays)
]

# Gráfico de barras empilhadas por categoria
fig = px.bar(
    filtered_df_merged,
    x="date",
    y="amount",
    color="category",
    text="amount",
    hover_data=["weekday", "subcategory"],
    labels={"amount": "Valor (R$)", "date": "Data"},
    title="Gastos Diários Empilhados por Categoria",
    barmode="stack"
)

# Exibe valores no topo das seções
fig.update_traces(
    texttemplate="R$ %{text:.2f}",
    textposition="inside"
)

fig.update_layout(
    yaxis_tickprefix="R$ ",
    xaxis_tickformat="%d/%m",
    height=600
)

st.plotly_chart(fig, use_container_width=True)


# ====

# Criar DataFrame

df_merged["date"] = pd.to_datetime(df_merged["date"])

# Filtro por subcategoria
st.title("📊 Média Diária por Categoria (considerando apenas dias com gasto)")
subcategory_options = sorted(df_merged["subcategory"].dropna().unique())

selected_subcategory = st.multiselect(
    "Filtrar por Subcategoria",
    options=subcategory_options,
    default=subcategory_options
)

# Aplica filtro
filtered_df_merged = df_merged[df_merged["subcategory"].isin(
    selected_subcategory)]

# Agrupa por data e categoria (soma do dia)
daily_totals = filtered_df_merged.groupby(["date", "category"])[
    "amount"].sum().reset_index()

# Calcula a média considerando apenas dias com gasto para cada categoria
category_avg = (
    daily_totals.groupby("category")
    .agg(media_diaria=("amount", "mean"))
    .reset_index()
)

# Gráfico de barras
fig = px.bar(
    category_avg,
    x="category",
    y="media_diaria",
    text="media_diaria",
    labels={"category": "Categoria", "media_diaria": "Média Diária (R$)"},
    title="Média Diária de Gastos por Categoria (apenas dias com gasto)",
)

# Formatação
fig.update_traces(texttemplate="R$ %{text:.2f}", textposition="outside")
fig.update_layout(yaxis_tickprefix="R$ ", height=500)

# Exibir
st.plotly_chart(fig, use_container_width=True)


# ============================== BUDGET


# ------------------------------
# Funções auxiliares de dados
# ------------------------------
CAMINHO_DADOS = "orcamento_data.json"


def carregar_dados():
    if os.path.exists(CAMINHO_DADOS):
        with open(CAMINHO_DADOS, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def salvar_dados(dados):
    with open(CAMINHO_DADOS, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)


def get_dados_mes(dados, mes):
    if mes not in dados:
        dados[mes] = {
            "receita": 10000.0,
            "gastos_fixos": {},
            "gastos_variaveis": {},
            "gastos_realizados": {},
            "fechado": False
        }
    return dados[mes]


def nome_mes(mes_str):
    return pd.to_datetime(mes_str).strftime("%b/%Y")


# ------------------------------
# Inicialização
# ------------------------------
st.set_page_config("Orçamento Mensal", layout="wide")
st.title("📊 Planejador de Orçamento com Investimentos")

# ------------------------------
# Carregar dados persistentes
# ------------------------------
dados = carregar_dados()
for mes in dados:
    if "fechado" not in dados[mes]:
        dados[mes]["fechado"] = False
# ------------------------------
# Seleção de Mês
# ------------------------------
meses = pd.date_range(datetime.today(), periods=12,
                      freq='MS').strftime('%Y-%m').tolist()
mes_selecionado = st.selectbox("📆 Selecione o Mês de Planejamento", meses)
dados_mes = get_dados_mes(dados, mes_selecionado)

# ------------------------------
# Controle de fechamento
# ------------------------------
col_fechar, col_status = st.columns([1, 4])
with col_fechar:
    if not dados_mes.get("fechado", False):
        if st.button("🔒 Fechar Orçamento"):
            dados_mes["fechado"] = True
            st.success("Orçamento fechado com sucesso!")
    else:
        if st.button("🔓 Reabrir Orçamento"):
            dados_mes["fechado"] = False
            st.warning("Orçamento reaberto. Você pode editar os dados.")

with col_status:
    status = "🔒 Fechado" if dados_mes.get(
        "fechado") else "🟢 Aberto para edição"
    st.markdown(f"**Status:** {status}")

# ------------------------------
# Receita
# ------------------------------
st.markdown("### 💰 Receita do Mês")
if not dados_mes["fechado"]:
    dados_mes["receita"] = st.number_input(
        "Informe a receita:", min_value=0.0, step=100.0, value=dados_mes.get("receita", 0.0))
else:
    st.write(f"Receita: R$ {dados_mes['receita']:,.2f}")

# ------------------------------
# Adicionar Categorias
# ------------------------------


def input_categorias(tipo):
    st.subheader(f"➕ Categorias de Gastos {tipo.capitalize()}")
    if f"categorias_{tipo}" not in st.session_state:
        st.session_state[f"categorias_{tipo}"] = list(
            dados_mes[f"gastos_{tipo}"].keys())

    if not dados_mes["fechado"]:
        nova = st.text_input(
            f"Adicionar categoria ({tipo})", key=f"nova_cat_{tipo}")
        if nova and nova not in st.session_state[f"categorias_{tipo}"]:
            st.session_state[f"categorias_{tipo}"].append(nova)

    # Mostrar categorias com opção de remover
    categorias_atuais = st.session_state[f"categorias_{tipo}"]
    categorias_remover = []

    for cat in categorias_atuais:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"- {cat}")
        with col2:
            if not dados_mes["fechado"]:
                if st.button("❌", key=f"remover_{tipo}_{cat}"):
                    categorias_remover.append(cat)

    # Remover categorias após o loop para evitar modificação durante a iteração
    for cat in categorias_remover:
        st.session_state[f"categorias_{tipo}"].remove(cat)
        # Remove da estrutura de dados
        dados_mes[f"gastos_{tipo}"].pop(cat, None)
        if tipo == "variaveis":
            dados_mes["gastos_realizados"].pop(
                cat, None)  # Também remove realizados


input_categorias("fixos")
input_categorias("variaveis")

# ------------------------------
# Input de Gastos Planejados
# ------------------------------


def input_valores(tipo):
    st.markdown(f"### ✏️ Gastos {tipo.capitalize()}")
    entradas = {}
    colunas = st.columns(2)
    for i, cat in enumerate(st.session_state[f"categorias_{tipo}"]):
        with colunas[i % 2]:
            if not dados_mes["fechado"]:
                valor = st.number_input(
                    f"{cat} ({tipo})", min_value=0.0, step=50.0,
                    value=dados_mes[f"gastos_{tipo}"].get(cat, 0.0),
                    key=f"{mes_selecionado}_{tipo}_{cat}"
                )
            else:
                valor = dados_mes[f"gastos_{tipo}"].get(cat, 0.0)
                st.write(f"{cat}: R$ {valor:,.2f}")
            entradas[cat] = valor
    dados_mes[f"gastos_{tipo}"] = entradas


input_valores("fixos")
input_valores("variaveis")

# ------------------------------
# Gastos Realizados
# ------------------------------
st.markdown("### 🧾 Registrar Gastos Realizados (Comparação com Planejado)")
st.markdown(
    "Insira os valores reais gastos nas categorias **variáveis** ao longo do mês.")

realizados = {}
colunas_real = st.columns(2)
for i, cat in enumerate(st.session_state["categorias_variaveis"]):
    with colunas_real[i % 2]:
        if not dados_mes["fechado"]:
            valor = st.number_input(
                f"{cat} (real)", min_value=0.0, step=10.0,
                value=dados_mes.get("gastos_realizados", {}).get(cat, 0.0),
                key=f"{mes_selecionado}_real_{cat}"
            )
        else:
            valor = dados_mes.get("gastos_realizados", {}).get(cat, 0.0)
            st.write(f"{cat}: R$ {valor:,.2f}")
        realizados[cat] = valor
dados_mes["gastos_realizados"] = realizados

# ------------------------------
# Alerta de estouro de orçamento
# ------------------------------
st.markdown("### 🚨 Monitoramento de Gastos Variáveis")

estouro_total = 0.0

for cat, gasto_real in realizados.items():
    previsto = dados_mes["gastos_variaveis"].get(cat, 0.0)
    if previsto == 0:
        continue

    percentual = gasto_real / previsto if previsto > 0 else 0.0

    if percentual >= 1.0:
        excesso = gasto_real - previsto
        estouro_total += excesso
        st.error(
            f"🔴 '{cat}' ultrapassou o previsto! R$ {gasto_real:,.2f} / R$ {previsto:,.2f}")
    elif percentual >= 0.9:
        st.warning(
            f"🟠 '{cat}' chegou a 90% do orçamento. R$ {gasto_real:,.2f} / R$ {previsto:,.2f}")
    else:
        st.success(
            f"✅ '{cat}' dentro do orçamento. R$ {gasto_real:,.2f} / R$ {previsto:,.2f}")

# ------------------------------
# Cálculo de sobra/investimento
# ------------------------------
total_fixos = sum(dados_mes["gastos_fixos"].values())
total_variaveis_planejados = sum(dados_mes["gastos_variaveis"].values())
total_variaveis_reais = sum(dados_mes["gastos_realizados"].values())

if dados_mes["fechado"]:
    total_gastos = total_fixos + total_variaveis_reais
else:
    total_gastos = total_fixos + total_variaveis_planejados + estouro_total

sobra = max(dados_mes["receita"] - total_gastos, 0.0)

st.markdown("### 📈 Resumo Financeiro")
st.write(f"🧾 Gastos Fixos: R$ {total_fixos:,.2f}")
st.write(
    f"🎲 Gastos Variáveis (reais se fechado): R$ {total_variaveis_reais if dados_mes['fechado'] else total_variaveis_planejados:,.2f}")
st.write(f"💥 Estouro de Gastos: R$ {estouro_total:,.2f}")
st.write(f"💸 Total de Gastos: R$ {total_gastos:,.2f}")
st.success(f"📈 Investimento Previsto: R$ {sobra:,.2f}")

# ------------------------------
# Investimento acumulado com CDI
# ------------------------------
cdi_anual = 0.1065
cdi_mensal = (1 + cdi_anual) ** (1 / 12) - 1

historico = {}
for mes, dm in dados.items():
    receita = dm.get("receita", 0.0)
    fixos = sum(dm.get("gastos_fixos", {}).values())

    if dm.get("fechado", False):
        variaveis = sum(dm.get("gastos_realizados", {}).values())
    else:
        variaveis = sum(dm.get("gastos_variaveis", {}).values())
        for cat, real in dm.get("gastos_realizados", {}).items():
            previsto = dm.get("gastos_variaveis", {}).get(cat, 0.0)
            if real > previsto:
                variaveis += real - previsto

    historico[mes] = max(receita - fixos - variaveis, 0.0)

acumulado = 0.0
bruto = 0.0
detalhes = []
for mes in sorted(historico.keys()):
    aporte = historico[mes]
    bruto += aporte
    acumulado = (acumulado + aporte) * (1 + cdi_mensal)
    detalhes.append((nome_mes(mes), aporte, acumulado, bruto))

df_inv = pd.DataFrame(
    detalhes, columns=["Mês", "Aporte", "Acumulado", "Bruto"])

st.markdown("### 📊 Investimento Acumulado (CDI)")
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(px.bar(df_inv, x="Mês", y="Aporte", title="Aportes Mensais")
                    .update_layout(yaxis_tickformat="R$ ,.2f"), use_container_width=True)

with col2:
    fig = px.line(df_inv, x="Mês", y=["Acumulado", "Bruto"],
                  title="Acumulado com CDI vs Bruto", markers=True)
    fig.update_layout(yaxis_tickformat="R$ ,.2f")
    st.plotly_chart(fig, use_container_width=True)

# ------------------------------
# Salvar os dados
# ------------------------------
salvar_dados(dados)
