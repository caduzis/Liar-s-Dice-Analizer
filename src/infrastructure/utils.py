import time
from functools import wraps

def time_monitor(func):
    """
    Decorator (Padrão de Projeto) para medir tempo de execução.
    Envolve a função original sem alterar seu comportamento ou sujar seu código interno.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Marca o tempo inicial com o relógio de alta precisão da CPU
        inicio = time.perf_counter()
        
        # 2. Executa a sua função original normalmente
        resultado = func(*args, **kwargs)
        
        # 3. Marca o tempo final
        fim = time.perf_counter()
        
        # 4. Calcula a diferença em milissegundos (ms)
        tempo_ms = (fim - inicio) * 1000
        print(f"⏱️ [Monitor] A função '{func.__name__}' levou {tempo_ms:.2f} ms")
        
        # 5. Devolve o resultado original para que o sistema continue funcionando
        return resultado
        
    return wrapper