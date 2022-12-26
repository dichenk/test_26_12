import json, pandas as pd, pathlib

'''читаем json'''
data = pd.read_json(pathlib.Path(__file__).parent / '..//test_26_12//operations.json')
data[['date', 'time']] = data.date.apply(lambda x: pd.Series(str(x).split(' ')))
data = data.sort_values(by='date', ascending=False)
data = data.dropna()
data = data.iloc[:5]

'''функция приведения даты в требуемый вид'''
def datte(item):
    item = item.split('-')
    item[0], item[1], item[2] = item[2], item[1], item[0]
    return '.'.join(item)


'''функция приведения источника перевода в требуемый вид'''
def fromm(item):
    item = item.split(' ')
    item[-1] = item[-1][:4] + ' ' + item[-1][5:6] + '** **** ' + item[-1][-4:]
    return ' '.join(item)

'''функция приведения приемщика перевода в требуемый вид'''
def to(item):
    item = item.split(' ')
    item[-1] = ' **' + item[-1][-4:]
    return ''.join(item)
 
def run():
    for i in range(len(data)):
        local_date = datte(data.iloc[i]['date'])
        local_description = data.iloc[i]['description']
        local_from = fromm(data.iloc[i]['from'])
        local_to = to(data.iloc[i]['to'])
        local_amount = data.iloc[i]['operationAmount']['amount']
        local_currency = data.iloc[i]['operationAmount']['currency']['name']

        print(local_date, local_description)
        print(local_from, '->', local_to)
        print(local_amount, local_currency)
        print()

run()
