import csv
import json

def in_dictlist(key, value, my_dictlist):
    for this in my_dictlist:
        if this[key] == value:
            return this
    return False


with open('b19-expenditure-data.csv', newline='', encoding='Windows-1252') as csvfile:
    budgetReader = csv.reader(csvfile)
    data={'name':'budget', 'children':[]}

    for row in budgetReader:
        if not (row[11]=='2019'):
          continue
        department = row[0]
        vote = row[1]
        appro = row[4]
        category = row[5]
        function = row[9]
        amount = row[10]

        functionRecord = False
        functionRecord = in_dictlist('name',function,data['children'])
        if not (functionRecord):
          functionRecord={'name': function, 'children':[]}
          data['children'].append(functionRecord)

        departmentRecord = False
        departmentRecord = in_dictlist('name',department,functionRecord['children'])
        if not (departmentRecord):
          departmentRecord={'name': department, 'children':[]}
          functionRecord['children'].append(departmentRecord)

        voteRecord = False
        voteRecord = in_dictlist('name',vote,departmentRecord['children'])
        if not (voteRecord):
          voteRecord={'name': vote, 'children':[]}
          departmentRecord['children'].append(voteRecord)

        approRecord = False
        approRecord = in_dictlist('name',appro,voteRecord['children'])
        if not (approRecord):
          approRecord={'name': appro, 'children':[]}
          voteRecord['children'].append(approRecord)

        categoryRecord = False
        categoryRecord = in_dictlist('name',category,approRecord['children'])
        if not (categoryRecord):
          categoryRecord={'name': category, 'value': int(amount)}
          approRecord['children'].append(categoryRecord)
        else:
          categoryRecord['value']=categoryRecord['value']+int(amount)

    print(json.dumps(data))