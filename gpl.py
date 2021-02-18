import datetime as dt
from getpass import getpass
from pathlib import Path

from gpluv.src.functionsPluviaAPI import *

user = input("Usuário: ") # Recebe usuário
psswd = getpass("Senha: ") # Recebe senha sem mostrar o input no terminaç

id_maps = [] # Recebe os IDs dos mapas de interesse da API
id_models = [] # Recebe os IDs dos data sources de interesse da API

token = authenticatePluvia(user, psswd) # Função de autenticação. O retorno do token é desnecessário, foi feito para debug e nunca retirado

precipitationDataSources = ["GEFS", "ECMWF_ENS", "ONS", "ETA", "Prec. Zero"] # Define os modelos a serem baixados
specs = ["ENSEMBLE", "ENSEMBLE", "", "", ""] # Define os membros a serem baixados
forecastModels = ['IA+SMAP'] # Define o que será IA, SMAP ou IA+SMAP

for precipitationDataSource in precipitationDataSources:
    id_maps.append(getIdOfPrecipitationDataSource(precipitationDataSource)) # Recupera o ID de todos os mapas de interesse

for forecastModel in forecastModels:
    id_models.append(getIdOfForecastModel(forecastModel)) # Recupera os IDs de todos os modelos de interesse

curr_day = dt.datetime.today() # Cria objeto de data do dia de hoje

forecastdate = curr_day.strftime("%d/%m/%Y") # Transforma o objeto de data em string para enviar para a API
form_dir = curr_day.strftime("%Y-%m-%d") # Transforma o objeto de data em string para criar o diretório de download

dir_download = Path('entradas')
if not (dir_download.exists()):
    Path.mkdir(dir_download) # Se inexistente, cria o diretório de download

forecasts = getForecasts(forecastdate, id_maps,
                         id_models, '', '', [curr_day.year], [])

for forecast in forecasts:
    # downloadForecast(forecast['prevsId'], dir_download,
    #                  forecast['nome'] + ' - ' + forecast['membro'] + ' - Prevs.zip') # Faz o download dos prevs do pluvia
    downloadForecast(forecast['enaId'], dir_download,
                     forecast['nome'] + ' - ' + forecast['membro'] + '- ENA.zip') # Faz download dos ENA do pluvia
    # downloadForecast(forecast['vnaId'], dir_download, forecast['nome'] + ' - ' + forecast['membro'] + '- VNA.csv') # Faz o download dos VNA do pluvia
    # downloadForecast(forecast['strId'], dir_download, forecast['nome'] + ' - ' + forecast['membro'] + '- STR.zip') # Faz o download dos STR do pluvia
