FROM apache/airflow:2.6.3

USER root
WORKDIR /opt/oracle
RUN apt-get update && apt-get install -y apt-utils build-essential unzip python-dev wget libaio1


RUN apt-get update && apt-get install -y libaio1 
RUN wget https://download.oracle.com/otn_software/linux/instantclient/instantclient-basiclite-linuxx64.zip && \
    unzip instantclient-basiclite-linuxx64.zip && rm -f instantclient-basiclite-linuxx64.zip && \
    cd /opt/oracle/instantclient* && rm -f *jdbc* *occi* *mysql* *README *jar uidrvci genezi adrci && \
    echo /opt/oracle/instantclient* > /etc/ld.so.conf.d/oracle-instantclient.conf && ldconfig

 
USER airflow
COPY requirement.txt /requirement.txt
RUN pip install --user  --upgrade pip
RUN pip install --no-cache-dir --user -r /requirement.txt
RUN pip install requests && pip install retrying
