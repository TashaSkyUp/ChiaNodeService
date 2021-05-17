import numpy as np
from geneticalgorithm import geneticalgorithm as ga
disks =6
parts = 3
tot_parts = disks*parts
def f(X,detail=False):
    r=[]
    XO=[]
    #print(len(X))
    for d in range(disks):
        start_idx = d*(parts-1)
        end_idx = (d*(parts-1))+(parts-1)
        disk = X[start_idx:end_idx]
        s = np.sum(disk)

        left_over = 247-int(s)
        if left_over < 0:
            disk[1]= disk[1]+left_over
            left_over=0
        #print(XO,disk,[left_over])
        if XO==[]:
            XO=list(disk)
            XO += [left_over]
            #print("r")
        else:
            XO += list(disk)
            XO += [left_over]
        #print(XO)
    XO=XO+list(X[-10:])
    #print (len(XO))


    for i in range(5):

        p1idx = int(XO[tot_parts+i])
        p2idx = int(XO[tot_parts + i +1])
        p1r = XO[p1idx]
        p2r = XO[p2idx]
        XO[p1idx]=0
        XO[p2idx]=0
        if detail:
            print(p1r+p2r)
        r += [p1r+p2r]

    score =0
    for rs in r:
        new_score = rs-265

        if detail:
            print(new_score)

        if new_score >= 0:
            score += 265-new_score
        else:
            score += new_score

    #print(score)
    high =229*5
    low = -1325
    rng = high-low
    score_out = (score-low)/rng
    if detail:
        print(score_out)
    return 1-score_out

l1 = [[0,247]]*(disks*(parts-1))
l2 = [[0,tot_parts]]*10
l=[]+l1+l2
print (l)
varbound=np.array(l)
print(varbound.shape)

iters = 100000
algorithm_param = {'max_num_iteration': iters,
                   'population_size':100,
                   'mutation_probability':0.1,
                   'elit_ratio': 0.02,
                   'crossover_probability': 0.1,
                   'parents_portion': 0.5,
                   'crossover_type':'uniform',
                   'max_iteration_without_improv':iters/1}

model=ga(function=f,
         dimension=(6*2)+10,
         variable_type='int',
         variable_boundaries=varbound,
         algorithm_parameters=algorithm_param)

model.run()

f(model.best_variable,detail=True)