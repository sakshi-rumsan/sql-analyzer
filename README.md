#### inspired from privategpt

#### Step 1: Step a Virtual Environment
virtualenv -p python3.11 myenv
# Activate the virtual environment
# On Windows
myenv\Scripts\activate
# On macOS/Linux
source myenv/bin/activate


#### Step 2: Install the Requirements
```
pip install -r requirements.txt



```
#### install streamlit
pip install streamlit


#### Step 3: Pull the models (if you already have models loaded in Ollama, then not required)
#### Make sure to have Ollama running on your system from https://ollama.ai || can be done with any model 
```
ollama pull mistral
```

#### Step 4: put your files in the source_documents folder after making a directory
```
mkdir source_documents
```

#### Step 5: Ingest the files (use python3 if on mac)
```
python ingest.py
```

#### step 6: streamlit run app.py
streamlit run app.py
```
sqlAnalyzer is for teminal answer questions


```

## Add more files

Put any and all your files into the `source_documents` directory

The supported extensions are:

- `.csv`: CSV,
- `.docx`: Word Document,
- `.doc`: Word Document,
- `.enex`: EverNote,
- `.eml`: Email,
- `.epub`: EPub,
- `.html`: HTML File,
- `.md`: Markdown,
- `.msg`: Outlook Message,
- `.odt`: Open Document Text,
- `.pdf`: Portable Document Format (PDF),
- `.pptx` : PowerPoint Document,
- `.ppt` : PowerPoint Document,
- `.txt`: Text file (UTF-8),
# sql-analyzer
# sql-analyzer
# sql-analyzer
