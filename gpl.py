import datetime as dt
from getpass import getpass
from pathlib import Path

from gpluv.src.functionsPluviaAPI import *

user = input("Usuário: ")
psswd = getpass("Senha: ")

id_maps = []
id_models = []

token = authenticatePluvia(user, psswd)

precipitationDataSources = ["ECMWF_ENS", "ECMWF_ENS_EXT"]
specs = ["", ""]
forecastModels = ['IA+SMAP']

for precipitationDataSource in precipitationDataSources:
    id_maps.append(getIdOfPrecipitationDataSource(precipitationDataSource))

for forecastModel in forecastModels:
    id_models.append(getIdOfForecastModel(forecastModel))

curr_day = dt.datetime.today()

forecastdate = curr_day.strftime("%d/%m/%Y")
form_dir = curr_day.strftime("%Y-%m-%d")

dir_download = Path('entradas')
if not (dir_download.exists()):
    Path.mkdir(dir_download)

forecasts = getForecasts(forecastdate, id_maps,
                         id_models, '', '', [curr_day.year], [])

for forecast in forecasts:
    # downloadForecast(forecast['prevsId'], dir_download,
    #                  forecast['nome'] + ' - ' + forecast['membro'] + ' - Prevs.zip')
    downloadForecast(forecast['enaId'], dir_download,
                     forecast['nome'] + ' - ' + forecast['membro'] + '- ENA.zip')
    # downloadForecast(forecast['vnaId'], dir_download, forecast['nome'] + ' - ' + forecast['membro'] + '- VNA.csv')
    # downloadForecast(forecast['strId'], dir_download, forecast['nome'] + ' - ' + forecast['membro'] + '- STR.zip')
