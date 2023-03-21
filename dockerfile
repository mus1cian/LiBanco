FROM python:3.9

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instalar requisitos previos de Oracle
RUN apt-get update && apt-get install -y libaio1 wget unzip && \
    mkdir /opt/oracle

# Descargar el archivo ZIP de Oracle Instant Client
RUN wget https://download.oracle.com/otn_software/linux/instantclient/199000/instantclient-basic-linux.x64-19.9.0.0.0dbru.zip \
    -O /opt/oracle/instantclient-basic-linux.x64-19.9.0.0.0dbru.zip

# Descomprimir el archivo ZIP de Oracle Instant Client
RUN cd /opt/oracle && \
    unzip instantclient-basic-linux.x64-19.9.0.0.0dbru.zip && \
    rm instantclient-basic-linux.x64-19.9.0.0.0dbru.zip && \
    echo /opt/oracle/instantclient_19_9 > /etc/ld.so.conf.d/oracle-instantclient.conf && \
    ldconfig

COPY . /app

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]