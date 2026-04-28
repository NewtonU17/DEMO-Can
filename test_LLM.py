from openai import OpenAI
import pdfplumber  # PyMuPDF
#pdf = pdfplumber.open(r"C:\Users\isaac\OneDrive\Documentos\Futura Demo\Demo\Futura_Talent_Growth_Plan_1year.pdf")
import os




def read_eval(pdfdir):
    secret = os.environ.get("THAT_ONE")
    pdf = pdfplumber.open(pdfdir)
    full_text = ""
    
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"
    
    
        
    client = OpenAI(
      base_url="https://openrouter.ai/api/v1",
      api_key=secret,
    )
    
    # First API call with reasoning
    response = client.chat.completions.create(
      model="openai/gpt-oss-120b:free",
      messages=[
              {
                "role": "user",
                "content": "List keywords in the following:" + full_text,
              }
            ],
      
    )
    
    # Extract the assistant message with reasoning_details
    response = response.choices[0].message
    
  
    
    return(response)
