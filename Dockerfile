FROM python:3

WORKDIR /Hydrangea-SensiClean

COPY . /Hydrangea-SensiClean

RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x /Hydrangea-SensiClean/debian.sh

CMD ["bash", "./debian.sh"]
