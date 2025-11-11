todo=input('Escriba todo lo que quiera ("salir" para parar): ')
arrayTodo=[]
arrayTodo.insert(0,todo)
count=1
while todo != "salir":
    todo=input('Escriba todo lo que quiera ("salir" para parar): ')
    arrayTodo.insert(count,todo)
    count=count+1

for x in arrayTodo:
    print(x)