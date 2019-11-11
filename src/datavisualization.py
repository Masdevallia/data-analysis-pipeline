
# Exploratory Data Visualization Charts related functions:

def pie_chart_stars(valuecounts,labels,state,sort_legend = True):    
    import matplotlib.pyplot as plt
    import numpy as np
    import random
    x = np.array([str(e)+' *' for e in labels])
    y = np.array(valuecounts)
    porcent = 100.*y/y.sum()   
    selected_colors = []
    while len(selected_colors) < len(labels):
        r = random.choice(['rosybrown','firebrick','indianred','darkgrey'])
        if r not in selected_colors: selected_colors.append(r)              
    fig1, ax1 = plt.subplots()
    explode = tuple([random.choice([0.01,0.01,0.01]) for i in range(len(labels))])
    patches, texts, autotexts = ax1.pie(y, labels = x, colors=selected_colors, autopct='%1.1f%%',startangle=90, pctdistance=0.85, explode=explode)
    ax1.axis('equal')
    fig1.set_size_inches(5,5)
    labels = ['{0}   {1:1.1f} %'.format(i,j) for i,j in zip(x, porcent)]
    if sort_legend:
        patches, labels, dummy =  zip(*sorted(zip(patches, labels, y), key=lambda x: x[2],reverse=True))
    plt.legend(patches, labels, loc='center left', bbox_to_anchor=(-0.6, 0.5),fontsize=12)
    fig1.suptitle('{} {}'.format('  Michelin stars in', state), fontsize=16)
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)   
    plt.savefig('./output/piechart_stars.png',bbox_inches='tight',dpi=300)


def pie_chart_cuisine(valuecounts,labels,state,sort_legend = True):    
    import matplotlib.pyplot as plt
    import numpy as np
    import random
    x = np.array([str(e)+' *' for e in labels])
    y = np.array(valuecounts)
    porcent = 100.*y/y.sum()   
    selected_colors = []
    while len(selected_colors) < len(labels):
        r = random.choice(['black','dimgrey','grey','darkgrey','lightgrey','whitesmoke','rosybrown','lightcoral','indianred','brown','firebrick','maroon','darkred','red','mistyrose','salmon','tomato','darksalmon','coral','orangered','lightsalmon','sienna','chocolate','saddlebrown','sandybrown','peachpuff','peru'])
        if r not in selected_colors: selected_colors.append(r)              
    fig1, ax1 = plt.subplots()
    explode = tuple([random.choice([0.01]*26) for i in range(len(labels))])
    patches, texts = ax1.pie(y, colors=selected_colors, startangle=90, pctdistance=0.85, explode=explode)
    ax1.axis('equal')
    fig1.set_size_inches(5,5)
    labels = ['{0}   {1:1.1f} %'.format(i,j) for i,j in zip(x, porcent)]
    if sort_legend:
        patches, labels, dummy =  zip(*sorted(zip(patches, labels, y), key=lambda x: x[2],reverse=True))
    plt.legend(patches, labels, loc='center left', bbox_to_anchor=(-1, 0.5),fontsize=12)
    fig1.suptitle('{} {}'.format('  Cuisine types in', state), fontsize=16)
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)   
    plt.savefig('./output/piechart_cuisine.png',bbox_inches='tight',dpi=300)



'''
OLD VERSION

def pie_chart_stars(valuecounts,labels,state,sort_legend = True):
    import matplotlib.pyplot as plt
    import numpy as np
    x = np.array(labels)
    y = np.array(valuecounts)
    porcent = 100.*y/y.sum()
    fig = plt.gcf()
    fig.set_size_inches(5,5)
    patches, texts = plt.pie(y, startangle=90)
    labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(x, porcent)]
    if sort_legend:
        patches, labels, dummy =  zip(*sorted(zip(patches, labels, y),key=lambda x: x[2],reverse=True))
    plt.legend(patches, labels, loc='center left', bbox_to_anchor=(-0.6, 0.5),fontsize=12)
    fig.suptitle('{} - {}'.format('Restaurant stars', state), fontsize=16)
    # plt.show()
    plt.savefig('./output/piechart_stars.png',bbox_inches='tight',dpi=300)
'''

'''
OLD VERSION

def pie_chart_cuisine(valuecounts,labels,state,sort_legend = True):
    import matplotlib.pyplot as plt
    import numpy as np
    x = np.array(labels)
    y = np.array(valuecounts)
    porcent = 100.*y/y.sum()
    fig = plt.gcf()
    fig.set_size_inches(5,5)
    patches, texts = plt.pie(y, startangle=90)
    labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(x, porcent)]
    if sort_legend:
        patches, labels, dummy =  zip(*sorted(zip(patches, labels, y),key=lambda x: x[2],reverse=True))
    plt.legend(patches, labels, loc='center left', bbox_to_anchor=(-1, 0.5),fontsize=12)
    fig.suptitle('{} - {}'.format('Cuisine type', state), fontsize=16)
    # plt.show()
    plt.savefig('./output/piechart_cuisine.png',bbox_inches='tight',dpi=300)
'''
