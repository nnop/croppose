import matplotlib.pyplot as plt

def draw_bbox(ax, bbox, text='', color='r', linewidth=2):
    xmin, ymin, xmax, ymax = bbox
    coords = (xmin, ymin), xmax-xmin+1, ymax-ymin+1
    ax.add_patch(plt.Rectangle(*coords, fill=False, edgecolor=color, 
        linewidth=linewidth))
    ax.text(xmin, ymin, text, size='x-small',
            bbox={'facecolor': color, 'alpha': 0.5})
