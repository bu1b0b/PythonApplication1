zavoz = ''
excavator = []

def ifPeremesh(line):
    line = line.replace(' -', '')
    line = line.replace('ОФ №', 'ОФ')
    line = line.replace('ОФ ', 'ОФ')
    line = line.replace('/ Шт №', 'Шт')
    line = line.replace('\n', ' ')

    sklad = line.split(' ')[:2][0].replace('№', '') + '/'
    shtabelPeremesh = '-' + line.split(' ')[:2][1].replace('Шт', '')

    fabrika = line.split(' ')[2:][0].replace('№', '') + '\t'
    shtabelFabrika = line.split(' ')[2:][1].replace('№', '') + '\t'
    tonn = line.split(' ')[2:][2].replace('№', '') + '\n'

    t1 = ''.join(sklad)
    t1 = t1 + shtabelPeremesh + '\t' + fabrika + shtabelFabrika + tonn
    return t1


def addExcavator(line):
    exc = line.split(' ')[:2][1]
    exc.replace('\n', '')
    exc = exc.replace('Э', '')
    if '0' in exc[0]:
        exc = exc.replace('0', '', 1)
    if exc not in excavator:
        excavator.append(exc)
        print('добавлен новый экскаватор №', exc)


with open('экскаваторы.txt', 'r', encoding='utf-8') as file3:
    for line in file3:
        excavator.append(line.replace('\n',''))
    print('список экскаваторов загружен: ', excavator.__len__(), ' единиц')
    print(excavator)

with open('СМС_Автовесы.txt', 'r', encoding='utf-8') as file1:
    for line in file1:
        if 'ОФ' in line:
            if 'БМТС' not in line:
                if 'СГП' not in line:

                    if 'экс' in line:
                        addExcavator(line)

                    if '№' in line[0]:
                        line = ifPeremesh(line)

                    zavoz = zavoz + line.replace('экс ', '')
                    zavoz = zavoz.replace(' -', '')
                    zavoz = zavoz.replace('ОФ №', 'ОФ')
                    zavoz = zavoz.replace('ОФ ', 'ОФ')
                    zavoz = zavoz.replace('/ Шт №', 'Шт')

with open('Готовые_Данные.txt', 'w', encoding='utf-8') as file2:

    zavoz = zavoz.replace(' ', '_')
    zavoz = zavoz.replace('_', '\t')
    zavoz = zavoz.replace('Э', '')
    zavoz = zavoz.replace('ОФ', '')
    zavoz = zavoz.replace('Шт', '')

    zavoz = '№ экс\t' + '№ ОФ\t' + '№ шт\t' + 'Тонн' + '\n' + zavoz
    file2.write(zavoz)
    print('завоз сохранен')

with open('экскаваторы.txt', 'w', encoding='utf-8') as file3:
    s = '\n'.join(excavator)
    s = s + '\n'
    file3.write(s)
    print('список экскаваторов сохранен: ', excavator.__len__(), ' единиц')

print('программа выполнена')

