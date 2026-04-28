from openai import OpenAI
import pdfplumber  # PyMuPDF
#pdf = pdfplumber.open(r"C:\Users\isaac\OneDrive\Documentos\Futura Demo\Demo\Futura_Talent_Growth_Plan_1year.pdf")

def read_eval(pdfdir):
    pdf = pdfplumber.open(pdfdir)
    full_text = ""
    
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"
    
    
        
    client = OpenAI(
      base_url="https://openrouter.ai/api/v1",
      api_key="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",
    )
    
    # First API call with reasoning
    response = client.chat.completions.create(
      model="openai/gpt-oss-120b:free",
      messages=[
              {
                "role": "user",
                "content": "Summarize the following:" + full_text,
              }
            ],
      
    )
    
    # Extract the assistant message with reasoning_details
    response = response.choices[0].message
    
    # Preserve the assistant message with reasoning_details
    messages = [
      {"role": "user", "content": "How many r's are in the word 'strawberry'?"},
      {
        "role": "assistant",
        "content": response.content,
        "reasoning_details": response.reasoning_details  # Pass back unmodified
      },
      {"role": "user", "content": "Are you sure? Think carefully."}
    ]
    
    response2 = client.chat.completions.create(
      model="openai/gpt-oss-120b:free",
      messages=messages,
      extra_body={"reasoning": {"enabled": True}}
    )
    
    return(response)
