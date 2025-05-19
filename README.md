def calcular_métricas(VP, VN, FP, FN):
    # Cálculo das métricas
    acuracia = (VP + VN) / (VP + VN + FP + FN)
    sensibilidade = VP / (VP + FN)  # recall
    especificidade = VN / (VN + FP)
    precisao = VP / (VP + FP)
    f_score = 2 * ((precisao * sensibilidade) / (precisao + sensibilidade))

    # Impressão dos resultados
    print(f"Acurácia: {acuracia:.2f}")
    print(f"Sensibilidade (Recall): {sensibilidade:.2f}")
    print(f"Especificidade: {especificidade:.2f}")
    print(f"Precisão: {precisao:.2f}")
    print(f"F-Score: {f_score:.2f}")

# Exemplo com valores arbitrários para matriz de confusão
VP = 80
VN = 50
FP = 10
FN = 5

calcular_métricas(VP, VN, FP, FN)
