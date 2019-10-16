import requests


def api(tamaño):
    url = 'http://www.cs.utep.edu/cheon/ws/sudoku/new/?level=1&size='
    url += str(tamaño)
    resp = requests.get(url)
    
    if tamaño == 9:
        lista = [["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x"]]
    elif tamaño == 4:
        lista = [["x", "x", "x", "x"],
                 ["x", "x", "x", "x"],
                 ["x", "x", "x", "x"],
                 ["x", "x", "x", "x"]]
    for item in resp.json()["squares"]:
        lista[item["y"]][item["x"]] = str(item["value"])

    return lista