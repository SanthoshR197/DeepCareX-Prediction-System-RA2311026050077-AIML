FROM python:3.10

RUN apt update -y
RUN pip install --no-cache-dir numpy pandas scikit-learn matplotlib scipy seaborn xgboost joblib flask tensorflow groq python-dotenv db-sqlite3

ENV TF_ENABLE_ONEDNN_OPTS=0
ENV FLASK_APP=main.py
ENV FLASK_DEBUG=1

WORKDIR /DeepCareX

ADD Website Website/
ADD Models Models/
ADD medical_agent.py .
ADD secret.env .

EXPOSE 5000

WORKDIR /DeepCareX/Website/database/
RUN python3 database.py

WORKDIR /DeepCareX/Website
ENV FLASK_APP=main.py

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
