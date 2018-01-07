#Шахов Кирилл Ивт
«»»
Этот модуль тестирует функцию шифрования алгоритмом rot13
«»»

from rot_13 import  *
import pytest

@ pytest.mark.parametrize ( " count, expected " , [
  ( « привет » , « uryyb » ),
  ( « uryyb » , « привет » )])

def  test_summ ( подсчет , ожидаемый ):
	assert (rot13 (count) == ожидается)
