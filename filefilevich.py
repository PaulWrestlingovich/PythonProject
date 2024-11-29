#запрашиваем коэффициенты
first_ratio = int(input('a = ', ))
second_ratio = int(input('b = ', ))
third_ratio = int(input('c = ', ))

# решение по сокращенной формуле, т.к. b - четное
if (first_ratio != 0
    and second_ratio % 2 == 0
    and third_ratio != 0):
        k = second_ratio / 2
        d1 = k ** 2 - first_ratio*third_ratio
        k1 = (-k + d1 ** 0.5) / first_ratio
        k2 = (-k - d1 ** 0.5) / first_ratio
        print('так как коэффициент b - четное число, решаем по сокращенной формуле')
        print(f'k1 = {k1}')
        print(f'k2 = {k2}')


if (first_ratio != 0
    and second_ratio % 2 != 0
    and third_ratio != 0):     # решение полного уравнения
        d = (second_ratio**2) - (4*first_ratio*third_ratio)
        if d > 0:
            k1 = (-second_ratio + (d**0.5)) / (2*first_ratio)
            print(f'дискриминант равен: {d}')
            print(f'первый корень равен: {round(k1, 2)}')
            k2 = (-second_ratio - (d**0.5)) / (2*first_ratio)
            print(f'второй корень равен: {round(k2, 2)}')
        elif d < 0:
            print(f'так как дискриминант меньше нуля и равен: {d}')
            print('действительных корней нет')
        else:
            k = -second_ratio / (2*first_ratio)
            print(f'уравнение имеет один корень: {k}')


if first_ratio != 0 and third_ratio != 0 and second_ratio == 0:        # решение уравнения при b = 0
    if (- third_ratio / first_ratio) >= 0:
                k1 = (-third_ratio / first_ratio) ** 0.5
                print(f'первый корень равен: {k1}')
                k2 = (-1) * (( -third_ratio / first_ratio ) ** 0.5)
                print(f'второй корень равен: {k2}')


    if ( - third_ratio / first_ratio ) < 0:
            print(f' -third_ratio / first_ratio = : {-third_ratio / first_ratio}, т.е. < 0, поэтому действительных корней нет')


if first_ratio != 0 and third_ratio== 0 and second_ratio != 0:     # решение уравнения при с = 0
    print(f'корень уравнения равен либо нулю, либо {-second_ratio / first_ratio}')


if first_ratio != 0 and second_ratio == 0 and third_ratio == 0:     # решение уравнения при b = 0 и c = 0
    print(f'корни уравнения равны нулю, first_ratio * x ** 2 = 0')



