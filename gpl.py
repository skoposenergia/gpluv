import json
import requests
from pathlib import Path
import datetime as dt
from getpass import getpass
from src.functionsPluviaAPI import *

user = input("Usuário: ")
psswd = getpass("Senha: ")

token = authenticatePluvia(user, psswd)

maps = getIdsOfPrecipitationsDataSource()
models = getIdsOfForecastModels()

id_maps = [x["id"] for x in maps]
id_models = [x["id"] for x in models]

curr_day = dt.datetime.today()

forecastdate = curr_day.strftime("%d/%m/%Y")
form_dir = curr_day.strftime("%Y-%m-%d")

dir_download = Path('Arquivos/%s/' % form_dir)
if not (dir_download.exists()):
    Path.mkdir(dir_download)

forecasts = getForecasts(forecastdate, id_maps,
                         id_models, '', '', [curr_day.year], [])

for forecast in forecasts:
    downloadForecast(forecast['prevsId'], dir_download, forecast['nome'] + ' - ' + forecast['membro'] + ' - Prevs.zip')
    # downloadForecast(forecast['enaId'], dir_download, forecast['nome'] + ' - ' + forecast['membro'] + '- ENA.zip')
    # downloadForecast(forecast['vnaId'], dir_download, forecast['nome'] + ' - ' + forecast['membro'] + '- VNA.csv')
    # downloadForecast(forecast['strId'], dir_download, forecast['nome'] + ' - ' + forecast['membro'] + '- STR.zip')
