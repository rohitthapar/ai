def toH(n,from_rod,aux_rod,to_rod):
    if n==0:
        return
    toH(n-1,from_rod,aux_rod,to_rod)
    print(f'Move {n} from {from_rod} to rod {to_rod}')
    toH(n-1,aux_rod,to_rod,from_rod)

n=5
toH(n,'A','C','B')

