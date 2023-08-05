FROM pytorch/pytorch:latest

WORKDIR /project

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# RUN pip install --no-cache-dir jupyterlab

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--no-browser"]