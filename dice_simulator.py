import time
from dice import roll

def lanzar_dados(amount: int, sides: int) -> list:
    """Lanza 'amount' dados de 'sides' caras."""
    resultados = []
    for _ in range(amount):
        # roll("1d6") devuelve un entero. Para 'sides' caras: roll(f"1d{sides}")
        resultado = roll(f"1d{sides}")
        resultados.append(resultado)
    return resultados

if __name__ == "__main__":
    amount = 5
    sides = 6
    resultados = lanzar_dados(amount, sides)
    for i, valor in enumerate(resultados, start=1):
        print(f"Tirada {i} → resultado: {valor}")
        time.sleep(5)