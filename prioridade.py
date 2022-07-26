from re import I


op = [[21111203, 1, ['R', 'COMP371']], [21113691, 13, ['I', 'COMP401']], [21114092, 18, ['T', 'COMP401', 'COMP370']], [21117122, 30, ['T', 'COMP378', 'COMP371']]]

for i in op:
    operacao = i[2][0]
    
    if (operacao == 'R'):
        materiaRemocao = i[2][1]
        
        for l in op:
            if (l != i):
                if (l[2][0] == 'I'):
                    print(l[2][1])
                    if (l[2][1] == materiaRemocao):
                        i.append({"prioridade": 2})
                
                elif (l[2][0] == 'T'):
                    if (l[2][1] == materiaRemocao):
                        i.append({"prioridade": 1})
        i.append({"prioridade": 3})
    elif (operacao == 'T'):
        i.append({"prioridade": 4})
    elif (operacao == 'I'):
        i.append({"prioridade": 5})
    
for i in op:
    print(i)












# for i in op:
#     # primeiro checamos se é remoção
#     if (i[2][0] == 'R'):
#         materia = i[2][1]
#         # agora vamos iterar através dos outros elementos e ver se a matéria está inclusa em algum deles 
#         for k in op:
#             # remoção que atende a uma inserção
#             if (k[2][0] == 'I'):
#                 for l in k[2][1]:
#                     if (l == materia):
#                         i.append({'prioridade': 2})
#             elif (k[2][0] == 'T'):
#                 for l in k[2][1][1]:
#                     if (l == materia):
#                         i.append({"prioridade": 1})
#             else:
#                 i.append({"prioridade": 3})

#     elif (i[2][0] == 'T'):
#         i.append({"prioridade": 4})
#     elif (i[2][0] == 'I'):
#         i.append({"prioridade": 5})
    
# for i in op:
#     print(i)





