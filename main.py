# This is the main module for running and testing your visualizer functions.

from medical_data_visualizer import draw_cat_plot, draw_heat_map

# Test the draw_cat_plot function
cat_plot = draw_cat_plot()
cat_plot.savefig('catplot.png')

# Test the draw_heat_map function
heat_map = draw_heat_map()
heat_map.savefig('heatmap.png')
