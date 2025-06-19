# Setting up venv
To create the virtual environment, run the following command in the terminal:
```python
python -m venv ai4Good
```

Next activate the virtual environment:
- On Windows:
  
```python 
.\venv\Scripts\activate
```

Next, install the required packages:
```python
 pip install -r requirements.txt
```
To deactivate the virtual environment, run:
```python
 deactivate
 ```
Follow the component/readme.md and install the required npm dependencies for the frontend on the same venv
# Running streamlit app
To run the Streamlit app, use the following command:
```python
 streamlit run APP_NAME.py
 ```
Replace `APP_NAME.py` with the name of your Streamlit app file.