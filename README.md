# Ixc api projeto
Dashboard de monitoramento de ordens de serviço dos técnicos, com atualização em tempo real via API do IXC ERP, utilizando Redis como camada de cache.

## Technologies
* `Python`
* `Redis`
* `Docker`
* `Streamlit`
* `python-dotenv`
* `requests`

## Running the Project
1. Clone o repository
2. Crie um ambiente virtual:
    ```python3 -m venv venv```   

3. Ative seu ambiente virtual:
    *Linux e Mac*
    ```source venv/bin/activate```
    *Windows*:
    ```venv\Scripts\activate```  

4. Instale todas as dependências necessária:
    ```python3 -m pip install -r requirements.txt``` ou 
    ```pip install -r requirements.txt```  

5. Crie uma variavel de ambiente `.env` basedado `.env.example` e preeca com suas credencias.  

6. Rode `worker.py` primeiro depois rode `view.py` usando stream:
    ```python3 worker.py```
    ```python3 -m streamlit run view.py``` ou
    ```streamlit run view.py```
   
## Preview


https://github.com/user-attachments/assets/ec952dda-022e-4440-9a91-9ee9e208989d




