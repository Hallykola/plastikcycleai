FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 500
COPY . .
ENTRYPOINT ["sh", "entrypoint.sh"]	
