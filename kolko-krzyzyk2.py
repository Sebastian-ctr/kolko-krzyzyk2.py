from tabulate import tabulate
import random



def main():
    # tabela do wyświetlenia
    tabela = [
        [' ', '|', ' ', '|', ' ', ' '],
        ['-', '-', '-', '-', '-', ],
        [' ', '|', ' ', '|', ' ', ' '],
        ['-', '-', '-', '-', '-', ],
        [' ', '|', ' ', '|', ' ', ' ']
    ]

    gra = False
    multiplayer = False
    singlepayer = False

    class pola(object):
        def __init__(self, value):
            self.value = value

        def x_wybor(self):
            self.value = 10

        def o_wybor(self):
            self.value = 1

        def zero_value(self):
            self.value = 0

        def return_value(self):
            return self.value


        @staticmethod
        def up_suma():
            return up_left.return_value() + up_mid.return_value() + up_right.return_value()

        @staticmethod
        def mid_suma():
            return mid_left.return_value() + mid_mid.return_value() + mid_right.return_value()

        @staticmethod
        def down_suma():
            return dow_left.return_value() + down_mid.return_value() + down_right.return_value()

        @staticmethod
        def left_suma():
            return up_left.return_value() + mid_left.return_value() + dow_left.return_value()

        @staticmethod
        def mid_mid_suma():
            return up_mid.return_value() + mid_mid.return_value() + down_mid.return_value()

        @staticmethod
        def rigth_suma():
            return up_right.return_value() + mid_right.return_value() + down_right.return_value()

        @staticmethod
        def left_right_suma():
            return up_left.return_value() + mid_mid.return_value() + down_right.return_value()

        @staticmethod
        def right_left_suma():
            return up_right.return_value() + mid_mid.return_value() + dow_left.return_value()



    # zmienne, wewnętrzne wartości

    up_left = pola(10)
    up_mid = pola(0)
    up_right = pola(0)
    mid_left = pola(0)
    mid_mid = pola(0)
    mid_right = pola(0)
    dow_left = pola(0)
    down_mid = pola(0)
    down_right = pola(0)

    data = [up_left, up_mid, up_right, mid_left, mid_mid, mid_right, dow_left, down_mid, down_right]

    suma_list = [pola.up_suma(), pola.mid_suma(), pola.down_suma(), pola.left_suma(), pola.mid_mid_suma(), pola.rigth_suma(), pola.left_right_suma(), pola.right_left_suma() ]


    #wpisane wyboru do tabeli i pamięci

    def change_table(row, columns, add):
        tabela[row][columns] = 'X' #wpisanie w tabelę
        data[add - 1].x_wybor() #dodanie wartości

    def second_pl_change(row, columns, add):
        tabela[row][columns] = 'O'
        data[add - 1].o_wybor()

    def Print():
        print(tabulate(tabela))

    #sprawdzanie sumy dla komputera

    def check_comp():
        print('check jest')
        print(suma_list)
        for i in range(0, 8):
            def check(i):
                if suma_list[i] == 10:
                    print('działa')

    #kończenie gry
    def end_game_loop():

            gra = False
            end_game = str(input('Koniec gry, wygrałeś, chcesz zagrać jeszcze raz?\ntak/nie: '))
            while True:
                try:
                    if end_game == 'nie':
                        break
                        gra = False
                        print('KONIEC GRY')

                    elif end_game == 'tak':
                        break
                        gra = True

                    else:
                        print('wpisz poprawnie: ')

                except ValueError:
                    print('wpisz poprwanie')

    def end_game():
        if suma_list[0] == 30:
            end_game_loop()
        elif suma_list[1] == 30:
            pass





    gra = True

    #wybór trybu
    while True:
        try:
            game_mode = int(input('Wybierz tryb gry 1 (gra z komputerem) lub 2 (gra z drugim graczem): '))
            #end_game()

            #Print()
            if game_mode == 1:
                singlepayer = True
                gra = True
                print('singleplayer')
                Print()
                break
            elif game_mode == 2:
                multiplayer = True
                gra = True
                print('multiplayer')
                Print()
                break
            else:
                print('Nie ma takiego trybu gry')
        except ValueError:
            print('ups...wygląda na to, że źle coś wpisałeś')

    # główna pętla gry
    while gra:
        if singlepayer:
            while True:
                try:
                    field_choose = int(input('Wybierz pole'))

                    if data[field_choose - 1].return_value() == 0:
                        if field_choose == 1 or field_choose == 2 or field_choose == 3:
                            change_table(0, (field_choose - 1) * 2, field_choose)
                            Print()
                            print(' ')
                            break
                        elif field_choose == 4 or field_choose == 5 or field_choose == 6:
                            change_table(2, (-6 + (field_choose - 1) * 2), field_choose)
                            Print()
                            print(' ')
                            break
                        elif field_choose == 7 or field_choose == 8 or field_choose == 9:
                            change_table(4, (-12 + (field_choose - 1) * 2), field_choose)
                            Print()
                            print(' ')
                            break
                        else:
                            print('Nie ma takiego pola, wybierz poprawną wartość od 1 do 9')
                    else:
                        print('To pole jest zajęte, wybierz inne')
                except ValueError:
                    print('wpisz poprawną wartość')
            #wybór komputera

            check_comp()
        elif multiplayer:
            #gracz pierwszy
            while True: #pętla do try
                try:
                    field_choose = int(input('Wybierz pole, gracz pierwszy: '))
                    if data[field_choose - 1].return_value() == 0:
                        if field_choose == 1 or field_choose == 2 or field_choose == 3:
                            change_table(0, (field_choose - 1) * 2, field_choose)
                            Print()
                            print(' ')
                            break
                        elif field_choose == 4 or field_choose == 5 or field_choose == 6:
                            change_table(2, (-6 + (field_choose - 1) * 2), field_choose)
                            Print()
                            print(' ')
                            break
                        elif field_choose == 7 or field_choose == 8 or field_choose == 9:
                            change_table(4, (-12 + (field_choose - 1) * 2), field_choose)
                            Print()
                            print(' ')
                            break
                        else:
                            print('Nie ma takiego pola, wybierz poprawną wartość od 1 do 9')
                    else:
                        print('To pole jest zajęte, wybierz inne')
                except ValueError:
                    print('Wygląda na to, że coś źle wpisałeś. Wartości od 1 do 9')
            while True:
                #gracz drugi, pętla do try
                try:
                    field_choose = int(input('Wybierz pole, drugi gracz: '))
                    if data[field_choose - 1].return_value() == 0:
                        if field_choose == 1 or field_choose == 2 or field_choose == 3:
                            second_pl_change(0, (field_choose - 1) * 2, field_choose)
                            Print()
                            print(' ')
                            break
                        elif field_choose == 4 or field_choose == 5 or field_choose == 6:
                            second_pl_change(2, (-6 + (field_choose - 1) * 2), field_choose)
                            Print()
                            print(' ')
                            break
                        elif field_choose == 7 or field_choose == 8 or field_choose == 9:
                            second_pl_change(4, (-12 + (field_choose - 1) * 2), field_choose)
                            Print()
                            print(' ')
                            break
                        else:
                            print('Nie ma takiego pola, wybierz poprawną wartość od 1 do 9')
                    else:
                        print('To pole jest zajęte, wybierz inne')
                except ValueError:
                    print('Wygląda na to, że źle coś wpisałeś.')



            #Print()

        #break


if __name__ == '__main__':
    main()
