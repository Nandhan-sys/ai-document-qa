 AI document q&a app

Simple ai application to read pdf documents. Ask any question about their content. Developed during bisidq solutions' ai intern shortlisting task.


 how to run

1. Clone this repository
Git clone https://github.com/your_username/YOUR_REPO_NAME.git
Cd YOUR_REPO_NAME
2. Install packages required by the project
Pip install Streamlit pypdf groq
3. Launch the Streamlit application
Streamlit run app.py
4. Access the application
The application should launch at `http://localhost:8501`.



Tools & APIs Used

Streamlit – Used to create the file upload form, input box, and button for asking questions.
pypdf – Extracts text from uploaded PDF files.
Groq API – Sends the question and document content to the AI model.
LLaMA 3.1 (8B) – Reads the document content and generates answers based on the questions.
Python – Programming language used to build the application.



How it works

1. User uploads pdf.
2. All text from pdf is extracted by pypdf.
3. User enters a question.
4. The question and document are sent to the llama model through the Groq API.
5. Llama reads the document content and responds to the users question.
6. The response is displayed on screen.



Project directory layout


Project/
│
├── app.py main application file.
└── readme.md this file.

Features

- can accept any pdf file
- can ask any question about the document
- responses are generated using only the content of the uploaded pdf
- can handle large PDFs (automatically truncates to fit within llama's limits)
- displays clear error message if no text is extractible from the pdf.

Api key configuration

The application uses **Groq API** (free).
Follow these steps to obtain your own:

1. Visit [console.groq.com](https://console.groq.com)
2. Create a free account
3. Generate an api key
4. Update the api key in 'app.py`
