import streamlit as st
import pandas as pd
import numpy as np
import evaluacion


st.title('Demo Candidates')
#['tyc', 'gaia', 'hyg', 'hip', 'hd', 'hr', 'gl', 'flam', 'ra','dec',  'mag', 'ci', 'rv', "con"]
col1, col2= st.columns([1,1])

with col1:
    catalog = st.multiselect(
    "¿Qué Producto/s desea predecir?",
    ('10-20-30-1-1 BULTO X 50 KGS', '13-26-6 BULTO X 50 KGS',
       '15-15-15 BULTO X 50 KGS', '31-8-8-2-3 (POTREROS) BULTO X 50 KGS',
       'ARPON BOTELLA X 1 LTR', 'BURIL BOL  X 100 GR',
       'CITROEMULSION ENVASE X 1 LTS',
       'FOSFATO DIAMONICO (DAP) BULTO X 50 KGS', 'GRUYA BOTELLA X 1 LTR',
       'IMPERIUS BOTELLA X 1 LTR', 'NOVAPLANT CA-B-ZN X LITRO',
       'PREDOSTAR BOL X 300 GR - GLY', 'PRODUCCION 17-6-18-2 BTO X 50 KG',
       'SUPERPRODUCCION 25-4-24 BTO X 50 KG', 'UREA GRANULADA X 50 KILOS',
       'otro'),
)
    prods = np.zeros(16)
    catag = np.array(['10-20-30-1-1 BULTO X 50 KGS', '13-26-6 BULTO X 50 KGS',
       '15-15-15 BULTO X 50 KGS', '31-8-8-2-3 (POTREROS) BULTO X 50 KGS',
       'ARPON BOTELLA X 1 LTR', 'BURIL BOL  X 100 GR',
       'CITROEMULSION ENVASE X 1 LTS',
       'FOSFATO DIAMONICO (DAP) BULTO X 50 KGS', 'GRUYA BOTELLA X 1 LTR',
       'IMPERIUS BOTELLA X 1 LTR', 'NOVAPLANT CA-B-ZN X LITRO',
       'PREDOSTAR BOL X 300 GR - GLY', 'PRODUCCION 17-6-18-2 BTO X 50 KG',
       'SUPERPRODUCCION 25-4-24 BTO X 50 KG', 'UREA GRANULADA X 50 KILOS',
       'otro'])
    for cons in catalog:
        num = np.where(catag == cons)
        prods[num] = 1
        
    catalogcl = st.multiselect(
    "¿Qué Cliente/s desea predecir?",
    ('DISTRIBUIDORA SURTIVEL S.A.S', 'RENDON LUZ AIDE', 'AGROBOLIVAR SG SAS',
       'LA CASA DEL AGRO MCU SAS', 'AGROTIENDA TONE SAS',
       'ZULUAGA VELASQUEZ LUIS EDUARDO', 'COOPERATIVA AGROMULTIACTIVA SAN BAR',
       'CASTAÑEDA SANCHEZ GLORIA PATRICIA', 'VALLEJO TOBON JULIO CESAR',
       'BODEGA CAMPESINA SAS', 'AGROEQUIPOS EL SEMBRADOR SAS ZOMAC',
       'REGIONAGRO SAS', 'ALMACENES AGROSUROESTE S.A.S', 'general',
       'ZULUAGA HOYOS GERARDO DE JESUS', 'RODRIGUEZ GONZALEZ LUIS ALBERTO',
       'AGROPECUARIA LUIS E RENDON B Y CIA', 'CANO DUQUE WILMAR HERNAN',
       'AGROINSUMOS CON LOS MEJORES PRECIOS', 'YEPES BETANCURT RUBEN DARIO',
       'PIEDRAHITA BEDOYA YOAN FELIPE', 'RUA MESA JHON JAIRO',
       'DISTRIBUCIONES MUNDO AGRO ANTIOQUIA', 'ALMACEN AGRICOLA CAMPESINO SAS',
       'ASO GANADEROS DEL ALTIPLANO NORTE D', 'ALMACENES CONSTRUAGRO SAS',
       'RENDON FRANCISCO JAVIER', 'FED COLOMBIANA DE PRODUCTORES DE PA',
       'AGROSANDER DON JORGE S.A.S', 'GIRALDO ARBELAEZ JOSE RAMON',
       'AGROBOLIVAR FLOWERS SAS'),
)
    clients = np.zeros(31)
    catagcl = np.array(['DISTRIBUIDORA SURTIVEL S.A.S', 'RENDON LUZ AIDE', 'AGROBOLIVAR SG SAS',
       'LA CASA DEL AGRO MCU SAS', 'AGROTIENDA TONE SAS',
       'ZULUAGA VELASQUEZ LUIS EDUARDO', 'COOPERATIVA AGROMULTIACTIVA SAN BAR',
       'CASTAÑEDA SANCHEZ GLORIA PATRICIA', 'VALLEJO TOBON JULIO CESAR',
       'BODEGA CAMPESINA SAS', 'AGROEQUIPOS EL SEMBRADOR SAS ZOMAC',
       'REGIONAGRO SAS', 'ALMACENES AGROSUROESTE S.A.S', 'general',
       'ZULUAGA HOYOS GERARDO DE JESUS', 'RODRIGUEZ GONZALEZ LUIS ALBERTO',
       'AGROPECUARIA LUIS E RENDON B Y CIA', 'CANO DUQUE WILMAR HERNAN',
       'AGROINSUMOS CON LOS MEJORES PRECIOS', 'YEPES BETANCURT RUBEN DARIO',
       'PIEDRAHITA BEDOYA YOAN FELIPE', 'RUA MESA JHON JAIRO',
       'DISTRIBUCIONES MUNDO AGRO ANTIOQUIA', 'ALMACEN AGRICOLA CAMPESINO SAS',
       'ASO GANADEROS DEL ALTIPLANO NORTE D', 'ALMACENES CONSTRUAGRO SAS',
       'RENDON FRANCISCO JAVIER', 'FED COLOMBIANA DE PRODUCTORES DE PA',
       'AGROSANDER DON JORGE S.A.S', 'GIRALDO ARBELAEZ JOSE RAMON',
       'AGROBOLIVAR FLOWERS SAS'])
    for cons in catalogcl:
        num = np.where(catagcl == cons)
        clients[num] = 1

    catalogmark = st.multiselect(
    "¿A qué marcas pertenecen los productos seleccionados?",
    ('ALTRIA', 'ECOFERTIL', 'INTEROC', 'JARDINES SIERRA', 'KIMITEC',
       'NUTRIMON', 'PROBELTE', 'STOLLER COLOMBIA',
       'SUPERFERTILIZANTES'),
)
    marks = np.zeros(10)
    catagmark = np.array(['ALTRIA', 'ECOFERTIL', 'INTEROC', 'JARDINES SIERRA', 'KIMITEC',
       'NUTRIMON', 'PRECISAGRO', 'PROBELTE', 'STOLLER COLOMBIA',
       'SUPERFERTILIZANTES'])
    for cons in catalogmark:
        num = np.where(catagmark == cons)
        marks[num] = 1
    
    
    catalogmats = st.multiselect(
    "¿A qué grupos de materiales pertenecen los productos seleccionados?",
    ('AGROQUIMICOS ESTRUCT', 'FERTILIZANTES ESTRUC', 'CORRECTIVOS ESTRUCTU'),
)
    mats = np.zeros(3)
    catagmats = np.array(['AGROQUIMICOS ESTRUCT', 'FERTILIZANTES ESTRUC', 'CORRECTIVOS ESTRUCTU'])
    for cons in catalogmats:
        num = np.where(catagmats == cons)
        mats[num] = 1
    
    catalogsect = st.multiselect(
    "¿A qué sectores pertenecen los clientes seleccionados?",
    ('P. RC NORTE LEJANO', 'P. RC AGRICOLA V.A', 'P. RC CÓRDOBA',
       'RTC VALLE DE ABURRA', 'P. RC AGR.NORTE', 'RTC ORIENTE A', 'RTC SUR',
       'P. RC AGR.ORIEN.A', 'RTC CORDOBA', 'P. RC AGR.ORIEN B', 'RTC URABA',
       'RTC ORIENTE B', 'RTC NORTE', 'P. RC AGRICOLA B.CAU', 'P. RC URABA',
       'P. RC AGR. SUROESTE'),
)
    sect = np.zeros(16)
    catagsect = np.array(['P. RC NORTE LEJANO', 'P. RC AGRICOLA V.A', 'P. RC CÓRDOBA',
       'RTC VALLE DE ABURRA', 'P. RC AGR.NORTE', 'RTC ORIENTE A', 'RTC SUR',
       'P. RC AGR.ORIEN.A', 'RTC CORDOBA', 'P. RC AGR.ORIEN B', 'RTC URABA',
       'RTC ORIENTE B', 'RTC NORTE', 'P. RC AGRICOLA B.CAU', 'P. RC URABA',
       'P. RC AGR. SUROESTE'])
    for cons in catalogsect:
        num = np.where(catagsect == cons)
        sect[num] = 1
    
    catalogofi = st.multiselect(
    "¿Con qué oficina se asocian los sectores seleccionados?",
    ('P. AGRICOLA ITAGUI', 'P. AGRICOLA STA ROSA'),
)
    ofi = np.zeros(2)
    catagofi = np.array(['P. AGRICOLA ITAGUI', 'P. AGRICOLA STA ROSA'])
    for cons in catalogofi:
        num = np.where(catagofi == cons)
        ofi[num] = 1
    
with col2:
    day = st.number_input(f'Ingrese el día', min_value=0, max_value=31, value=10)
    mes = st.number_input(f'Ingrese el mes', min_value=0, max_value=12, value=10)
    year = st.number_input(f'Ingrese el año', min_value=2020, max_value=2028, value=2025)
    precio = st.number_input(f'Ingrese el precio al que se vende una unidad', min_value=0, max_value=300000, value=100000)
    peso = st.number_input(f'Ingrese el peso de una unidad', min_value=0, max_value=100, value=25)
    lluvia = st.number_input(f'Ingrese los mm de precipitación del día', min_value=0, max_value=35, value=5)
    TRM = st.number_input(f'Ingrese el valor promedio de la TRM para el día', min_value=0, max_value=6000, value=4200)
    IPC = st.number_input(f'Ingrese el valor del IPP para el mes a predecir', min_value=0, max_value=400, value=288)
values = np.concatenate(([year,mes,day,precio,peso,lluvia,TRM, IPC],clients,sect,ofi,mats,marks,prods))
values = evaluacion.preparacion(values)
dist = evaluacion.prediccion(values)[0]
if dist < 0: dist = 0
st.write(f"La venta introducida será de {round(dist)} unidades según el modelo")
