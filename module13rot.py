# Шахов
# кирилл
# Задание - На основе кода с выполнением предыдущего задания 
# реализуйте получение JSON с удаленного хоста и красивый вывод информации на экран.


def  rot13 ( s ):    "" " сдвиг на нужную позицию (тут на 13) " ""
    result =  " "

    для v в s:
        c =  ord (v)

        если c > =  ord ( ' a ' ) и c <=  ord ( ' z ' ):
            если c >  ord ( ' m ' ):
                c - =  13
            Остальное :
                c + =  13
        elif c > =  ord ( ' A ' ) и c <=  ord ( ' Z ' ):
            если c >  ord ( ' M ' ):
                c - =  13
            Остальное :
                c + =  13

        результат + =  chr (c)
    результат возврата


def  rot13_file ( имя_файла ):    "" " Открытие файла в режиме чтения " ""
    попробуйте :
        file  =  open (имя_файла, ' r ' )
    кроме :
        print ( " Ошибка открытия файла " )
        вернуть

    попробуйте :
        data =  file .read ()
    кроме :
        print ( " Ошибка считывания файла " )
        вернуть
    наконец :
        файл .close ()

    file  =  open (имя_файла, ' w ' )   "" " Запись ответа " ""

    попробуйте :
        файл .write (rot13 (данные))
    кроме :
        print ( " Ошибка Записи " )
        вернуть
    наконец :
        файл .close ()

    print ( " Зашифрованный файл " )


если  __name__  ==  " __main__ " :

    menu =  "" "
    1. Поработаем в консоли
    2. Поработаем в файле
    3. Драпаем (выход)
    
       ВЫБИРАЙ ...
    «»»
    в то время как  True :
        в то время как  True :
            попробуйте :
                choice =  int ( вход (меню))
                если выбор ==  1  или выбор ==  2  или выбор ==  3 :
                    ломать
            кроме :
                print ( " что-то пошло не так - ошибка вывода " )

        если выбор ==  1 :
            print ( " Итог: " , rot13 ( ввод ( " Введите строку: " )))
        elif choice ==  2 :
            rot13_file ( input ( " Вы файл (закодированный): " ))
        elif choice ==  3 :
            ломать
