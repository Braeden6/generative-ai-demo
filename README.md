# Hallucination Demo using LangChain
This demo downloads a pdf file from the internet and converts it into [embeddings](https://developers.google.com/machine-learning/crash-course/embeddings/video-lecture#:~:text=An%20embedding%20is%20a%20relatively,like%20sparse%20vectors%20representing%20words.). These embeddings are then used to find relevant section of the pdf based on your question using [FAISS](https://engineering.fb.com/2017/03/29/data-infrastructure/faiss-a-library-for-efficient-similarity-search/). The relevant section is then used to generate answers to your question using [GPT-4](https://openai.com/gpt-4).

Used Tools:
1) [LangChain](https://python.langchain.com/docs/get_started/introduction.html): For simplifying the generative AI application building process
2) [FAISS](https://pypi.org/project/faiss/): For finding the most similar embeddings
3) Pickl: For saving and loading embeddings
4) OpenAI: For generating answers to questions
5) PyPDF: For extracting text from pdf
6) [Text Splitter](https://github.com/hwchase17/langchain/blob/master/langchain/text_splitter.py): For splitting text into sections for embeddings
7) Prompt Engineering: Technique for improving the quality of answers generated

## Guide using VSCode and Jupyter Notebook
### Set up Virtual Environment
[Link](https://code.visualstudio.com/docs/python/environments)
1) Ctrl + Shift + P
2) Environment Type: Venv
3) Select the virtual environment (hallucinationDemo or the name of the workspace folder)
4) Select the python interpreter
5) Add requirements.txt in drop down or run `pip install -r requirements.txt` in terminal
### Add Kernel to Jupyter Notebook
[Link](https://code.visualstudio.com/docs/datascience/jupyter-kernel-management)
1) Open Jupyter Notebook File
2) Select the Kernel (top right corner)
