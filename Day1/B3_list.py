list_a = [123, 'abc' , 456, 'donny', 100.09]
list_b = list_a[:-1]
list_a += [789, 200.44]
list_b.append('Hello')
list_a.reverse()
nestList=[[1,2,3],
          [4,5,6],
          [7,8,9]]
col2 = [ col[2] for col in nestList]








print(list_a)
print(list_b)
print(col2)