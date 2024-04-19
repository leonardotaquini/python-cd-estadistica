import pandas as pd

def csv_to_data_frame(datos:str):
    if len(datos) == 0:
        return 'Debe ingresar el nombre del archivo csv'
    data_frame = pd.read_csv(datos)
    data_frame["fi"] = data_frame.groupby("edades")["edades"].transform("count")
    data_frame["Fi"] = data_frame["fi"].cumsum()
    data_frame["ri"] = data_frame["fi"] / data_frame["fi"].sum()
    data_frame["Ri"] = data_frame["ri"].cumsum()
    data_frame["pi%"] = data_frame["ri"] * 100
    data_frame["Pi%"] = data_frame["pi%"].cumsum()

    return data_frame


def analisis_estadistico(datos: list):
    validacion = validar_lista_numerica(datos)
    if not validacion:
        return 'La lista debe ser numerica'
    data_frame = pd.DataFrame( datos, columns=["x"] )
    data_frame = data_frame.groupby("x").size().reset_index(name='fi')
    data_frame["Fi"] = data_frame["fi"].cumsum()
    data_frame["ri"] = data_frame["fi"] / data_frame["fi"].sum()
    data_frame["Ri"] = data_frame["ri"].cumsum()
    data_frame["pi%"] = data_frame["ri"] * 100
    data_frame["Pi%"] = data_frame["pi%"].cumsum()

    return data_frame


def validar_lista_numerica(datos: list):
    if type(datos) != list:
        return False
    if len(datos) == 0:
        return False
    for i in range(len(datos)):
        if type(datos[i]) != int:
            return False
    return True

