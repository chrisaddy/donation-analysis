FROM ubuntu:16.04
FROM python:3.6.3
FROM r-base:3.5.1

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

WORKDIR /app
ADD . /app

# install python modules
RUN pip install --trusted-host pypi.python.org -r requirements.txt
# install R libraries
# RUN Rscript -e "install.packages('versions')" \
	# Rscript -e "versions::install.versions('dplyr', '0.7.5')"

CMD ['app.py']
