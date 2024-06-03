#!/bin/bash

python3 amg_plot.py /home/yhz/DCSIM_Improve/data_out/ibm_data_cq/ibmpg1/ibmpg.G.txt ibmpg1.G.png || true 
python3 amg_plot.py /home/yhz/DCSIM_Improve/data_out/ibm_data_cq/ibmpg2/ibmpg.G.txt ibmpg2.G.png || true 
python3 amg_plot.py /home/yhz/DCSIM_Improve/data_out/ibm_data_cq/ibmpg3/ibmpg.G.txt ibmpg3.G.png || true 
python3 amg_plot.py /home/yhz/DCSIM_Improve/data_out/ibm_data_cq/ibmpg4/ibmpg.G.txt ibmpg4.G.png || true 
python3 amg_plot.py /home/yhz/DCSIM_Improve/data_out/ibm_data_cq/ibmpg5/ibmpg.G.txt ibmpg5.G.png || true 
python3 amg_plot.py /home/yhz/DCSIM_Improve/data_out/ibm_data_cq/ibmpg6/ibmpg.G.txt ibmpg6.G.png || true 

# python3 amg_plot_2.py /home/yhz/AMGCL_KT/amgcl_data/thupg1/thupg.G.txt thupg1.G.png || true 
# python3 amg_plot_2.py /home/yhz/AMGCL_KT/amgcl_data/thupg2/thupg.G.txt thupg2.G.png || true 
# python3 amg_plot_2.py /home/yhz/AMGCL_KT/amgcl_data/thupg3/thupg.G.txt thupg3.G.png || true 
# python3 amg_plot_2.py /home/yhz/AMGCL_KT/amgcl_data/thupg4/thupg.G.txt thupg4.G.png || true 
# python3 amg_plot_2.py /home/yhz/AMGCL_KT/amgcl_data/thupg5/thupg.G.txt thupg5.G.png || true 
# python3 amg_plot_2.py /home/yhz/AMGCL_KT/amgcl_data/thupg6/thupg.G.txt thupg6.G.png || true 

# for ((i=1; i<=100; i++));do
#     python3 amg_plot.py ../../CNN_L/build/csr_dataset/train_dataset/$i.txt build/$i.png
#     echo $i.png
# done
# 
