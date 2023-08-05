FROM continuumio/miniconda3:4.12.0

WORKDIR /project

RUN apt-get update && apt-get install -y wget

COPY requirements.txt .

RUN conda install --file requirements.txt

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--no-browser"]