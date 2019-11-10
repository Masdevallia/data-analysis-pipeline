
# Exploratory Data Visualization Charts related functions:

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

