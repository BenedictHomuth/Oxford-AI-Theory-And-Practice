FROM continuumio/anaconda3:2022.05

RUN conda update --all --yes
RUN conda install jupyter -y --quiet
RUN conda install pytorch -y 
RUN conda install numpy -y
RUN pip install notebook==6.5.6

# setup working dir
RUN mkdir -p /opt/notebooks