#!/usr/bin/env python
import matplotlib.pyplot as plt
import pandas as pd

#res = pd.read_csv('results.csv')

#print res.head()

def create_plot(results):
    res = pd.DataFrame(results)
    res.to_csv('results.csv', index=False)
    rank_map = {}
    for index, pid in enumerate(res['pid'].unique()):
        rank_map[pid] = index

    num_engines = len(res.groupby('pid').size())
    #print num_engines

    tmax = int(res['start_time'].max())
    #print tmax

    fig, ax = plt.subplots(figsize=(10, 8))
        
    tmin = res['start_time'].min()  
    tmax = res['end_time'].max() - tmin
    for i in res.index:
        x_start = res.ix[i]['start_time'] - tmin
        x_end = res.ix[i]['end_time'] - tmin - x_start
        x_id = float(res.ix[i]['pid'])
        #print x_start, x_end, rank_map[x_id]/float(num_engines)
        x_id = rank_map[x_id]/float(num_engines)
        ax.add_patch(plt.Rectangle((x_start, x_id),x_end,0.03,alpha=0.7, color='#4DAF4A'))
    ax.set_xlim(0, tmax)
    ax.set_ylabel("Worker")
    ax.set_xlabel("seconds")

