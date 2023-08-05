# Assuming that docker container is running on a OS system with a CUDA GPU.
FROM tensorflow/tensorflow:latest-gpu

WORKDIR /project

RUN pip install -U jupyterlab pandas matplotlib

EXPOSE 8888

ENTRYPOINT ["jupyter", "lab","--ip=0.0.0.0","--allow-root","--no-browser"]
